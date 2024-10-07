"""
@Description：数据上传类
@Author：mysondrink@163.com
@Time：2024/2/27 16:14
"""
from PySide2.QtCore import QThread, Signal
import pandas as pd
import numpy as np
import os
import time
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
    import middleware.database as insertdb
    from pic_code.img_main import img_main
except:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractThread import AbstractThread
    import qt0223.middleware.database as insertdb
    from qt0223.pic_code.img_main import img_main


time_to_sleep = 2
trylock_time = -1
failed_code = 404
succeed_code = 202
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'


class UploadThread(AbstractThread):
    finished = Signal()

    def __init__(self, file_path='./res/new_data.xlsx'):
        """
        构造函数
        初始化线程，调用父类方法进行日志记录
        Args:
            file_path: 上传文件的路径
        """
        super().__init__()
        self.file_path = file_path

    def run(self):
        """
        读取文件，将文件中的数据分离处理
        Returns:
            None
        """
        csv_data = []
        id_data = []
        reagent_data = []
        status_data = []
        type_data = []
        input_table = pd.read_excel(self.file_path, sheet_name="Sheet2")
        input_table_rows = input_table.shape[0]
        # input_table_columns = input_table.shape[1]
        # input_table_header = input_table.columns.values.tolist()
        for i in range(input_table_rows):
            input_table_rows_values = input_table.iloc[[i]]
            input_table_rows_values_array = np.array(input_table_rows_values)
            input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            csv_data.append(input_table_rows_values_list)
            id_data.append(input_table_rows_values_list[1])
            reagent_data.append(input_table_rows_values_list[-2])
            status_data.append(input_table_rows_values_list[-1])
            type_data.append(input_table_rows_values_list[5])
        self.insertMysql(id_data, status_data, type_data, *self.filterReagentData(reagent_data))
        # ["序号", "图片名称", "时间", "样本条码", "医生", "类别",
        #  "阵列", "病人名", "病人性别", "病人年龄", "数据", "status"]
        # [id_num, name_pic, cur_time, code_num, doctor, reagent_type,
        #  reagent_matrix, name, gender, age, reagent_matrix_info]

    def filterReagentData(self, data):
        """
        过滤过敏原数据
        Args:
            data: 需要过滤的过敏原数据

        Returns:
            reagent_info_list: 过敏原数据
            points_list: 定位点数据
            gray_aver_list: 像素点数据
        """
        reagent_info_list = []
        points_list = []
        gray_aver_list = []
        for i in data:
            temp = i.split(",")
            points_list.append(",".join(i for i in temp[0:5]))
            reagent_info_list.append(",".join(i for i in temp[5:]))
            b = temp[10:]
            c = [b[k:k+10] for k in [j for j in range(0, 55, 15)]]
            str_list = []
            for j in [i for i in c]:
                str_list = str_list + [i for i in j]
            gray_aver_list.append(",".join(str_list))
        return reagent_info_list, points_list, gray_aver_list

    def insertMysql(self, id_list, status_list, type_list, reagent_info_list, points_list, gray_aver_list):
        """
        进行数据更新
        根据照片名进行数据的更新
        Args:
            id_list: 照片名
            status_list: status状态list
            reagent_info_list: 过敏原数据 60
            points_list: 定位点数据 5
            gray_aver_list: 像素点数据 40

        Returns:
            None
        """
        sum = insertdb.insertMySql(id_list, status_list, reagent_info_list, points_list, gray_aver_list)
        print("update single spline 2 sqlite")
        for i, j in zip(id_list, range(len(id_list))):
            if status_list[j] == 0:
                continue
            flag, concentration_aver_str = self.gray2Conc(points_list[j] + ',' + gray_aver_list[j])
            if flag is not True:
                continue
            flag = insertdb.updateSingleConFromUpload(i, points_list[j] + ',' + gray_aver_list[j], concentration_aver_str)
            if type_list[j][5] in ["A", "B", "C", "D"]:
                # nature_aver_temp = self.gray2NatureNotCalc(points_list[j] + ',' + gray_aver_list[j])
                nature_aver_temp = self.gray2NatureNotCalc(concentration_aver_str)
            else:
                nature_aver_temp = self.gray2Nature(concentration_aver_str)
            flag1 = insertdb.updateNatureAverFromUpload(i, nature_aver_temp)
        print('新增' + str(sum) + "数据")
        time.sleep(0.5)
        self.deleteFile()
        self.finished.emit()

    def deleteFile(self):
        """
        数据更新完后，删除更新文件
        Returns:
            None
        """
        os.remove(self.file_path)

    def gray2Conc(self, data):
        list1 = data.split(",")
        print("list1 len:", len(list1))
        list2 = ['-1' if item == '' else item for item in list1]
        list5 = [list2[i:i+5] for i in range(0, len(list2), 5)]
        # list3 = np.array(list2)
        # list4 = list3.reshape(9, 5)
        print("change num list5: ", list5)
        list5[8][0] = '-1'
        list5[8][4] = '-1'
        Main = img_main()
        # get_data = Main.tempRun(list4, func="model1")
        get_data = Main.tempRun(list5, func="model1")
        _flag = get_data['flag']
        concentration_info = get_data['value']
        w, h = concentration_info.shape
        concentration_list = []
        for i in range(w):
            for j in range(h):
                if i == 0:
                    concentration_list.append('')
                elif (i * w + j) % 2 == 0:
                    concentration_list.append('')
                elif concentration_info[i][j] < 0:
                    concentration_list.append('')
                else:
                    # concentration_list.append(str(water[i][j]))
                    concentration_list.append(f"{concentration_info[i][j]:.2f}")
        concentration_str = ",".join(concentration_list)
        return _flag, concentration_str

    def gray2Nature(self, data):
        nature_aver_list = []
        result_dict = {
            "极高": "&gt;100", "很高": "50-100", "非常高": "17.5-50", "高": "3.5-17.5",
            "中": "0.7-3.5", "低": "0.35-0.7", "检测不到": "&lt;0.35"
        }
        result_dict = {
            "1": "极高", "2": "很高", "3": "非常高", "4": "高",
            "5": "中", "6": "低", "7": "检测不到"
        }
        list1 = data.split(",")
        list2 = ['-1' if item == '' else item for item in list1]
        for i in list2:
            temp = float(i)
            if temp < 0:
                nature_aver_list.append(i)
            elif temp < 0.35:
                nature_aver_list.append(result_dict["7"])
            elif temp < 0.7:
                nature_aver_list.append(result_dict["6"])
            elif temp < 3.5:
                nature_aver_list.append(result_dict["5"])
            elif temp < 17.5:
                nature_aver_list.append(result_dict["4"])
            elif temp < 50:
                nature_aver_list.append(result_dict["3"])
            elif temp < 100:
                nature_aver_list.append(result_dict["2"])
            else:
                nature_aver_list.append(result_dict["1"])
        result = ",".join(nature_aver_list)
        return result

    def gray2NatureNotCalc(self, data):
        # < 0.35: "阴性" "-"
        # 0.35-3.5: "弱阳性" "+"
        # 3.5-17.5: "中阳性" "++"
        # >17.5: "强阳性" "+++"
        nature_aver_list = []
        result_dict = {
            "1": "阴性", "2": "弱阳性", "3": "中阳性", "4": "强阳性"
        }
        list1 = data.split(",")
        list2 = ['-1' if item == '' else item for item in list1]
        for i in list2:
            temp = float(i)
            if temp < 0.35:
                nature_aver_list.append(result_dict["1"])
            elif temp < 3.5:
                nature_aver_list.append(result_dict["2"])
            elif temp < 17.5:
                nature_aver_list.append(result_dict["3"])
            else:
                nature_aver_list.append(result_dict["4"])
        result = ",".join(nature_aver_list)
        return result

