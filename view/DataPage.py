import os
import re
import cv2 as cv
import datetime
import numpy as np
from PySide2.QtCharts import QtCharts
try:
    from view.gui.info import *
    import util.frozen as frozen
    from util import dirs
    from util.report import MyReport
    from util.report_outdate import MyReport as OldTypeReport
    from view.AbstractPage import AbstractPage, ProcessDialog
    from controller.USBController import CheckUSBThread
    import middleware.database as insertdb
    from pic_code.img_main import img_main
    from util.curve import MyCurve
except ModuleNotFoundError:
    from qt0223.view.gui.info import *
    import qt0223.util.frozen as frozen
    from qt0223.util import dirs
    from qt0223.util.report import MyReport
    from util.report_outdate import MyReport as OldTypeReport
    from qt0223.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0223.controller.USBController import CheckUSBThread
    import qt0223.middleware.database as insertdb
    from qt0223.pic_code.img_main import img_main
    from qt0223.util.curve import MyCurve


QChartView = QtCharts.QChartView
QChart = QtCharts.QChart
QSplineSeries = QtCharts.QSplineSeries

class DataPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        继承父类构造函数
        初始化数据展示界面，同时创建记录异常的信息
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self) -> None:
        """
        设置界面相关信息
        Returns:
            None
        """
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(3)  # 取消图片显示
        self.ui.btnPic.hide()
        # self.ui.btnPic.setText("曲线")
        self.setBtnIcon()
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.photoLabel.setText("")
        self.ui.picLabel.setText("")

    def closeEvent(self, event) -> None:
        """
        窗口关闭事件
        Args:
            event: 响应事件，窗口关闭

        Returns:
            None
        """
        self.setParent(None)
        event.accept()  # 表示同意了，结束吧

    def setBtnIcon(self) -> None:
        """
        设置按钮图标
        Returns:
            None
        """
        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnData.setIconSize(QSize(32, 32))
        self.ui.btnData.setIcon(QIcon(confirm_icon_path))

        switch_icon_path = frozen.app_path() + r"/res/icon/switch.png"
        self.ui.btnPic.setIconSize(QSize(32, 32))
        self.ui.btnPic.setIcon(QIcon(switch_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/exe.png"
        self.ui.btnPrint.setIconSize(QSize(32, 32))
        self.ui.btnPrint.setIcon(QIcon(exe_icon_path))

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnReport.setIconSize(QSize(32, 32))
        self.ui.btnReport.setIcon(QIcon(confirm_icon_path))

        exe_icon_path = frozen.app_path() + r"/res/icon/compute.png"
        self.ui.btnDownload.setIconSize(QSize(32, 32))
        self.ui.btnDownload.setIcon(QIcon(exe_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

    # this is a data get slot
    def getData(self, msg) -> None:
        """
        获取信息
        信息来自TestPage和HistoryPage页面，信息包括图片信息和数据库信息
        Args:
            msg: 信号，发送来的信息

        Returns:
            None
        """
        # print(msg['info'])
        print("datapage id: ", id(self))
        flag = 0
        pic_para = 1
        self.info = msg['info']
        self.data = msg['data']
        self.row_exetable = int(self.data['row_exetable'])
        self.column_exetable = int(self.data['column_exetable'])

        # print("row,column:", self.row_exetable, self.column_exetable)
        name_pic = self.data['name_pic']
        cur_time = self.data['time']
        pic_path = self.data['pic_path']
        self.test_time = cur_time[0] + ' ' + cur_time[1]
        reagent_matrix_info = self.data['reagent_matrix_info']
        try:
            curve_id = self.data['pic_name']
            _i = self.data['item_type']
        except Exception as e:
            curve_id = self.data['reagent_photo']
            _i = self.data['item_type']
        self.drawChart(_i, curve_id)
        self.pix_table_model = QStandardItemModel(
            self.row_exetable + int(self.row_exetable / 2), self.column_exetable
        )
        self.pix_table_model_copy = QStandardItemModel(
            self.row_exetable + int(self.row_exetable / 2) + 2,
            self.column_exetable
        )
        # 设置只显示检测点对应结果
        # self.pix_table_model = QStandardItemModel(
        #     self.row_exetable + int(self.row_exetable / 2), self.column_exetable
        # )
        # self.pix_table_model_copy = QStandardItemModel(
        #     self.row_exetable + 2,
        #     self.column_exetable
        # )
        self.ui.tableView.setModel(self.pix_table_model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().close()
        self.ui.tableView.verticalHeader().close()
        # self.ui.tableView.setGridStyle(Qt.NoPen)

        self.ui.tableView_2.setModel(self.pix_table_model_copy)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_2.horizontalHeader().close()
        self.ui.tableView_2.verticalHeader().close()
        self.ui.tableView_2.setGridStyle(Qt.NoPen)

        self.ui.rightLabel.setText(self.test_time)
        self.ui.leftLabel.setText(self.test_time)

        self.allergy_info = reagent_matrix_info
        point_str = self.data['point_str']
        self.showDataView(point_str + ',' + reagent_matrix_info)
        # 设置只显示检测点对应结果
        # self.showDataView(point_str, reagent_matrix_info, self.data['gray_aver_str'], self.data['item_type'])
        # creating a report display
        # 测试
        # self.data['nature_aver_str'] = '检测不到,高,非常高,高,检测不到,非常高,极高,非常高,检测不到,极高,极高,非常高,高,高,非常高,极高,非常高,高,检测不到,高,高,检测不到,高,高,高,非常高,检测不到,非常高,高,极高,非常高,非常高,检测不到,非常高,非常高,高,检测不到,极高,高,检测不到,高,高,检测不到,高,检测不到'
        # 测试结束
        _, concentration_matrix = insertdb.getCurvePoints(self.data['name_pic'])
        self.setTableWidget(self.data['item_type'], self.allergy_info, self.data['nature_aver_str'], concentration_matrix)
        # self.setTableWidget(self.data['item_type'], self.allergy_info, self.data['nature_aver_str'])

    def setTableWidget(self, item_type, reagent_info, nature_aver_str, concentration_matrix):
        """
        设置报告单显示
        Args:
            item_type: 试剂型号
            reagent_info: 过敏原信息
            nature_aver_str: 过敏原中文信息

        Returns:
            None
        """
        v = QVBoxLayout()
        allergen_str = insertdb.selectAllergenMatrixInfo(item_type)
        allergen_list = allergen_str.split(",")
        if item_type in ["A", "B", "C", "D"]:
            text = OldTypeReport().gethtml(item_type, reagent_info, nature_aver_str, allergen_list)
        else:
            text = MyReport().gethtml(item_type, reagent_info, nature_aver_str, concentration_matrix, allergen_list)
        self.myreport = QTextEdit()
        # 姓名，性别，样本号，条码号，样本类型，测试时间，【结果】，打印时间
        # cur_time[0] + ' ' + cur_time[1]
        str_list = [self.data['patient_name'], self.data['patient_gender'], self.data['reagent_id'],
                    self.data['code_num'], self.data['item_type'],
                    self.data['time'][0] + ' ' + self.data['time'][1],
                    text[1], '']
        self.myreport.setHtml(text[0] % tuple(str_list))

        v.addWidget(self.myreport)
        self.ui.tableWidget.setLayout(v)

    def getUSBInfo(self, msg):
        """
        U盘提示信息
        Args:
            msg: U盘信息

        Returns:
            None
        """
        print(msg)
        self.checkUserOperation(True)
        if msg == 202:
            info = "下载完成！"
            self.showInfoDialog(info)
            # obj.deleteLater()
        elif msg == 404:
            info = "U盘未插入或无法访问！"
            self.showInfoDialog(info)
            # obj.deleteLater()
        elif msg == 405:
            info = "图片读取失败或未找到图片！"
            self.showInfoDialog(info)
            # obj.deleteLater()


    def showDataView(self, data):
        """
        数据展示，包括定位点，过敏原，灰度值
        Args:
            data:

        Returns:

        """
        title_list = ["定位点", "", "", "", "定位点"]
        data_copy = re.split(r",", data)
        data_copy = title_list + data_copy
        row = self.pix_table_model_copy.rowCount()
        column = self.pix_table_model_copy.columnCount()
        for i in range(row):
            for j in range(column):
                pix_num = data_copy[i * column + j]
                item = QStandardItem(str(pix_num))
                item.setTextAlignment(Qt.AlignCenter)
                self.pix_table_model_copy.setItem(i, j, item)
        return

    """
    def showDataView(self, points, data, gray_aver, item_type):
        path = frozen.app_path() + r"/res/allergen/"
        with open(path + item_type, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            allergen = [i.rstrip() for i in lines][5:]
        row = 8
        column = 5
        allergen_temp = [allergen[i * column:i * column + column] for i in range(row)]
        # 定位点列表
        _points = [i for i in points.split(",")]
        # 数据点列表
        result_list_points = [i for i in gray_aver.split(",")[5:]]
        list_points_filter = self.filterData(result_list_points, allergen_temp)

        # 过敏原列表
        reagent_info_list_1 = [i for i in data.split(",")]
        reagent_info_list_2 = [reagent_info_list_1[k:k+5] for k in [j for j in range(0, 55, 5)] if k % 15 == 0]
        reagent_info_list_3 = [i for i in sum(reagent_info_list_2, []) if i != '']

        # 需要达到的元素数量
        target_length = 20
        # 计算需要填充的0的数量
        fill_count = target_length - len(list_points_filter)
        # 使用列表的extend方法填充0
        if fill_count > 0:
            list_points_filter.extend([''] * fill_count)
        fill_count = target_length - len(reagent_info_list_3)
        # 使用列表的extend方法填充0
        if fill_count > 0:
            reagent_info_list_3.extend([''] * fill_count)

        row = 4
        column = 5
        list_points_result = [list_points_filter[i * column:i * column + column] for i in range(row)]
        list_allergen_result = [reagent_info_list_3[i * column:i * column + column] for i in range(row)]


        # 新建一个空列表用于存放合并后的结果
        merged_list = []

        # 交叉合并
        for i in range(max(len(list_allergen_result), len(list_points_result))):
            if i < len(list_allergen_result):
                merged_list.append(list_allergen_result[i])
            if i < len(list_points_result):
                merged_list.append(list_points_result[i])

        flat_lst = [item for sublist in merged_list for item in sublist]

        title_list = ["定位点", "", "", "", "定位点"]
        # data_copy = re.split(r",", data)
        data_copy = title_list + _points + flat_lst
        row = self.pix_table_model_copy.rowCount()
        column = self.pix_table_model_copy.columnCount()
        for i in range(row):
            for j in range(column):
                if i * column + j > len(data_copy) - 1:
                    break
                pix_num = data_copy[i * column + j]
                item = QStandardItem(str(pix_num))
                item.setTextAlignment(Qt.AlignCenter)
                self.pix_table_model_copy.setItem(i, j, item)
        return

    # outdate
    def filterData(self, ori_data, para_data):
        row = 8
        column = 5
        ori_data_temp = [ori_data[i * column:i * column + column] for i in range(row)]
        ori_data_corrected = [[b_row[j] if a_row[j] != '' else '' for j in range(len(a_row))]
                              for a_row, b_row in zip(para_data, ori_data_temp)]
        result_data = []
        for i in range(0, len(ori_data_corrected), 2):
            result_data.extend([item for pair in zip(*ori_data_corrected[i:i + 2]) for item in pair if item])
        return result_data
    """
    """
    def showDataView(self, points, data, gray_aver, item_type):

        path = frozen.app_path() + r"/res/allergen/"
        with open(path + item_type, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            allergen = [i.rstrip() for i in lines][5:]
        row = 8
        column = 5
        allergen_temp = [allergen[i * column:i * column + column] for i in range(row)]
        # 定位点列表
        _points = [i for i in points.split(",")]
        # 数据点列表
        result_list_points = [i for i in gray_aver.split(",")[5:]]
        list_points_filter = self.filterData(result_list_points, allergen_temp)

        title_list = ["定位点", "", "", "", "定位点"]
        data_copy = re.split(r",", data)
        data_copy = title_list + data_copy
        row = self.pix_table_model_copy.rowCount()
        column = self.pix_table_model_copy.columnCount()
        for i in range(row):
            for j in range(column):
                pix_num = data_copy[i * column + j]
                item = QStandardItem(str(pix_num))
                item.setTextAlignment(Qt.AlignCenter)
                self.pix_table_model_copy.setItem(i, j, item)
        return

    def filterData(self, ori_data, para_data):
        row = 8
        column = 5
        ori_data_temp = [ori_data[i * column:i * column + column] for i in range(row)]
        ori_data_corrected = [[b_row[j] if a_row[j] != '' else '' for j in range(len(a_row))]
                              for a_row, b_row in zip(para_data, ori_data_temp)]
        result_data = []
        for i in range(0, len(ori_data_corrected), 2):
            result_data.extend([item for pair in zip(*ori_data_corrected[i:i + 2]) for item in pair if item])
        return result_data
    """

    def checkUserOperation(self, flag):
        """
        判断当前状态是否为下载中
        关闭除数据、报告单外的按钮
        Args:
            flag:

        Returns:

        """
        self.ui.btnPrint.setEnabled(flag)
        self.ui.btnDownload.setEnabled(flag)
        self.ui.btnReturn.setEnabled(flag)

    def drawChart(self, item_type, curve_id):
        """
        绘制曲线
        Args:
            item_type: 检测组合
            curve_id: 曲线id号

        Returns:
            None
        """
        light_points, concentration_matrix = insertdb.getCurvePoints(curve_id)
        allergen_str = insertdb.selectAllergenMatrixInfo(item_type)
        allergen_list = allergen_str.split(",")
        fitting_points = MyCurve().filterCurvePoints(item_type, light_points, concentration_matrix, allergen_list)
        sorted_coordinates_1 = sorted(fitting_points, key=lambda x: x[0])  # 按照横坐标进行从小到大排序
        # print(sorted_coordinates_1)
        import matplotlib.pyplot as plt
        # 提取x和y坐标
        x_values = [point[0] for point in sorted_coordinates_1]
        y_values = [point[1] for point in sorted_coordinates_1]
        # 绘制曲线
        plt.figure(figsize=(10, 6))  # 可自定义图形大小
        plt.plot(x_values, y_values)  # 绘制曲线，并标记点
        # plt.xlabel('X Axis Label')
        # plt.ylabel('Y Axis Label')
        # plt.title('拟合曲线')
        # 保存图像到本地文件
        chart_img = '%s/cache/picture/%s' % (frozen.app_path(), curve_id + "曲线.jpeg")
        plt.savefig(chart_img, dpi=300)  # 设置图像分辨率（dots per inch）

    """
    outdate
    def drawChart(self, item_type, curve_id):
        light_points, concentration_matrix = insertdb.getCurvePoints(curve_id)
        fitting_points = MyCurve().filterCurvePoints(item_type, light_points, concentration_matrix)
        sorted_coordinates_1 = sorted(fitting_points, key=lambda x: x[0]) # 按照横坐标进行从小到大排序
        layout = QHBoxLayout()
        self.ui.page_2.setLayout(layout)
        self.ui.tableView.hide()
        chart = QChart()
        # chart.setTitle('Line Chart 1')
        series = QSplineSeries(chart)
        series_1 = QSplineSeries(chart)
        series.setName("主曲线")
        series_1.setName("拟合曲线")
        LIGHT_DATA = [(0.0, 1362), (2.1, 24179), (8.92, 103611), (86.39, 888364), (176.88, 1704084),
                        (371.42, 2849815)]
        sorted_coordinates = sorted(LIGHT_DATA, key=lambda x: x[0]) # 按照横坐标进行从小到大排序
        for i in sorted_coordinates:
            series << QPointF(*i)
        for k in sorted_coordinates_1:
            series_1 << QPointF(*k)
        chart.addSeries(series)
        chart.addSeries(series_1)
        chart.createDefaultAxes()  # 创建默认轴
        # chart.legend().setVisible(False)    # 取消点位显示
        self.chartview = QChartView(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # view.resize(800, 600)
        # view.show()
        layout.addWidget(self.chartview)
        # self.ui.stackedWidget.setCurrentIndex(0)
    """

    @Slot()
    def on_btnPrint_clicked(self):
        """
        槽函数
        打印按钮操作
        Returns:
            None
        """
        info = "打印中。。。"
        dialog = ProcessDialog()
        dialog.setInfo(info)
        dialog.setParent(self)
        dialog.hideBtn()
        dialog.show()
        print("print")
        self.checkUserOperation(False)
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_time = self.test_time
        Data_Base = [self.data['patient_name'], self.data['patient_gender'], self.data['patient_id'],
                    self.data['code_num'], '检测组合' + self.data['item_type'], test_time, time_now]
        gray_aver_str = self.data['gray_aver_str'].split(",")
        nature_aver_str = self.data['nature_aver_str'].split(",")
        _, concentration_matrix = insertdb.getCurvePoints(self.data['name_pic'])
        concentration_matrix_temp = concentration_matrix.split(",")
        concentration_matrix_temp_lst = ['-1' if item == '' else item for item in concentration_matrix_temp]
        array_gray_aver = np.array(gray_aver_str)
        array_nature_aver = np.array(nature_aver_str)
        array_concentration = np.array(concentration_matrix_temp_lst)
        matrix_gray_aver = array_gray_aver.reshape(9, 5)
        matrix_nature_aver = array_nature_aver.reshape(9, 5)
        matrix_concentration = array_concentration.reshape(9, 5)
        Data_Nature = matrix_nature_aver
        Data_Light = matrix_gray_aver
        Data_Water = matrix_concentration
        Main = img_main()
        _ = Main.natPrint_init()
        # 测试
        if Main.natPrint(Data_Base, Data_Nature, Data_Light):
        # 测试结束
        # if Main.natPrint(Data_Base, Data_Nature, Data_Water, Data_Light):
            dialog.closeDialog()
            info = "输出表格成功!"
            self.update_info.emit(info)
        else:
            dialog.closeDialog()
            info = "输出表格失败!"
            self.update_info.emit(info)
        self.checkUserOperation(True)

    @Slot()
    def on_btnDownload_clicked(self):
        """
        槽函数
        下载按钮操作
        Returns:
            None
        """
        print("Download")
        self.checkUserOperation(False)
        name = self.data['name_pic']
        path = self.data['pic_path']
        data = self.data

        # chart_img = '%s/cache/picture/%s' % (frozen.app_path(), name + "曲线.jpeg")
        # width = self.chartview.width()
        # height = self.chartview.height()
        # pixmap = QPixmap(width, height)
        # self.chartview.render(pixmap)
        # success = pixmap.save(chart_img)
        _, concentration_matrix = insertdb.getCurvePoints(self.data['name_pic'])
        usbthread = CheckUSBThread(
            name,
            path,
            data,
            self.data['point_str'] + ',' + self.allergy_info,
            concentration_matrix
        )
        usbthread.update_json.connect(self.getUSBInfo)
        loop = QEventLoop()
        usbthread.update_json.connect(loop.quit)
        # 创建定时器
        self.download_timer = QTimer()
        self.download_timer.timeout.connect(usbthread.start)
        self.download_timer.timeout.connect(self.download_timer.stop)
        # 设置定时器延迟时间，单位为毫秒
        # 延迟1秒跳转
        delay_time = 1000
        self.download_timer.start(delay_time)
        # m_title = ""
        # m_info = "下载中..."
        # infoMessage(m_info, m_title, 300)
        info = "下载中..."
        self.showInfoDialog(info)
        loop.exec_()

    @Slot()
    def on_btnData_clicked(self):
        """
        槽函数
        数据按钮操作，跳转到数据展示页
        Returns:
            None
        """
        # self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(3)

    @Slot()
    def on_btnPic_clicked(self):
        """
        弃用
        槽函数
        图片按钮操作，跳转到图片页
        Returns:
            None
        """
        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def on_btnReport_clicked(self):
        """
        槽函数
        报告单按钮操作，跳转到报告单页面
        Returns:
            None
        """
        self.ui.stackedWidget.setCurrentIndex(2)

    @Slot()
    def on_btnReturn_clicked(self):
        """
        槽函数
        返回按钮操作，跳转到上一页
        Returns:
            None
        """
        if self.info == 201:
            page_msg = 'TestPage'
            self.next_page.emit(page_msg)
        elif self.info == 202:
            page_msg = 'history'
            self.next_page.emit(page_msg)