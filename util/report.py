"""
@Description：报告单格式化方法
@Author：mysondrink@163.com
@Time：2024/3/1 10:47
"""
try:
    import util.frozen as frozen
except:
    import qt0223.util.frozen as frozen


class MyReport():
    def __init__(self):
        self.html_content = '<!doctype html>\
                            <html>\
                            <head>\
                            <meta charset="utf-8">\
                            </head>\
                            <h1 align="center" style="font-size:20px;font-family:fangsong;">过敏原检验报告单</h1>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr align="center">\
                                    <td>姓名：%s</td>\
                                    <td>性别：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>试剂卡编号：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>样本条码：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>样本类型：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>测试时间：%s</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr align="center">\
                                    <td>过敏原</td>\
                                    <td>类别</td>\
                                    <td>参考值</td>\
                                    <td>结果</td>\
                                </tr>\
                                %s\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr>\
                                    <td>注</td>\
                                </tr>\
                                <tr>\
                                    <td>&gt;100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&ensp;极高</td>\
                                </tr>\
                                <tr>\
                                    <td>50 ;-100&nbsp;&nbsp;&ensp;很高</td>\
                                </tr>\
                                <tr>\
                                    <td>17.5-50&nbsp;&nbsp;&ensp;非常高</td>\
                                </tr>\
                                <tr>\
                                    <td>3.5 -17.5&nbsp;高</td>\
                                </tr>\
                                <tr>\
                                    <td>0.7 -3.5 &nbsp;中</td>\
                                </tr>\
                                <tr>\
                                    <td>0.35-0.7 &nbsp;低</td>\
                                </tr>\
                                <tr>\
                                    <td>&lt;0.35&nbsp;&nbsp;&nbsp;&nbsp;&ensp;检测不到</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr>\
                                    <td>打印时间：%s</td>\
                                </tr>\
                                <tr>\
                                    <td>此检验报告只对此标本负责，请结合临床。</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <body>\
                            </body>\
                            </html>\
                            '

        self.html_content = '<!doctype html>\
                            <html>\
                            <head>\
                            <meta charset="utf-8">\
                            </head>\
                            <h1 align="center" style="font-size:20px;font-family:fangsong;">过敏原检验报告单</h1>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr align="center">\
                                    <td>姓名：%s</td>\
                                    <td>性别：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>样本号：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>条码号：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>样本类型：%s</td>\
                                </tr>\
                                <tr align="center">\
                                    <td>测试时间：%s</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr align="center">\
                                    <td>过敏原</td>\
                                    <td>结果</td>\
                                    <td>参考值</td>\
                                    <td>结果解释</td>\
                                </tr>\
                                %s\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr>\
                                    <td>注</td>\
                                </tr>\
                                <tr>\
                                    <td>*检测不到&nbsp;: &lt;0.35IU/ml</td>\
                                </tr>\
                                <tr>\
                                    <td>*低&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 0.35IU/ml-0.7IU/ml</td>\
                                </tr>\
                                <tr>\
                                    <td>*中&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 0.7IU/ml-3.5IU/ml</td>\
                                </tr>\
                                <tr>\
                                    <td>*高&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 3.5IU/ml-17.5IU/ml</td>\
                                </tr>\
                                <tr>\
                                    <td>*非常高&nbsp;&nbsp;: 17.5IU/ml-50IU/ml</td>\
                                </tr>\
                                <tr>\
                                    <td>*很高&nbsp;&nbsp;&nbsp;&nbsp;: 50IU/ml-100IU/ml</td>\
                                </tr>\
                                <tr>\
                                    <td>*极高&nbsp;&nbsp;&nbsp;&nbsp;: &gt;100IU/ml</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <table style="font-size:20px;font-family:fangsong;" border="0" width="800" cellspacing="0" align="center">\
                                <tr>\
                                    <td>打印时间：%s</td>\
                                </tr>\
                                <tr>\
                                    <td>此检验报告只对此标本负责，请结合临床。</td>\
                                </tr>\
                            </table>\
                            <hr />\
                            <body>\
                            </body>\
                            </html>\
                            '
        
    def gethtml(self, item_type, reagent_info, nature_aver_str, concentration_matrix, allergen_list):
        result_dict = {
            "极高": "&gt;100", "很高": "50-100", "非常高": "17.5-50", "高": "3.5-17.5",
            "中": "0.7-3.5", "低": "0.35-0.7", "检测不到": "&lt;0.35"
        }
        # 参考值计算列表 40
        result_list_1 = [result_dict.get(i) for i in nature_aver_str.split(",")[5:]]
        # 高度计算列表 40
        result_list_2 = [i for i in nature_aver_str.split(",")[5:]]
        # 浓度计算列表 40
        result_list_concentration = [i for i in concentration_matrix.split(",")[5:]]

        # 过敏原列表 40
        reagent_info_list_1 = [i for i in reagent_info.split(",")]
        reagent_info_list_2 = [reagent_info_list_1[k:k+5] for k in [j for j in range(0, 55, 5)] if k % 15 == 0]
        reagent_info_list_3 = [i for i in sum(reagent_info_list_2, []) if i != '']

        """
        path = frozen.app_path() + r"/res/allergen/"
        with open(path + item_type, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            allergen = [i.rstrip() for i in lines][5:]
        """
        allergen = allergen_list
        row = 8
        column = 5
        allergen_temp = [allergen[i * column:i * column + column] for i in range(row)]

        allergen_temp_output_list = []
        # 遍历每个子列表
        for sublist in allergen_temp:
            # 从子列表中选取非空字符串并添加到output_list
            allergen_temp_output_list.extend(item for item in sublist if item != '')
        result_list_3 = self.filterData(result_list_1, allergen_temp)
        result_list_4 = self.filterData(result_list_2, allergen_temp)
        list_concentration_filter = self.filterData(result_list_concentration, allergen_temp)

        # + —结果列表
        result_list_3 = [result_list_1[i] for i in range(len(allergen)) if allergen[i] != ""]
        # 阴阳性结果列表
        result_list_4 = [result_list_2[i] for i in range(len(allergen)) if allergen[i] != ""]
        list_concentration_filter_temp = [result_list_concentration[i] for i in range(len(allergen)) if allergen[i] != ""]

        list_concentration_filter = []
        for num_str in list_concentration_filter_temp:
            num = float(num_str)  # 将字符串转换为浮点数以进行比较
            if num > 100:
                list_concentration_filter.append('&gt;100')
            elif num < 0.35:
                list_concentration_filter.append('&lt;0.35')
            else:
                list_concentration_filter.append(str(num))  # 将数字转回字符串保持原样

        # 姓名，性别，样本号，条码号，样本类型，测试时间，【结果】，打印时间
        temp = '<tr align="center">\
                <td>%s</td>\
                <td>%s</td>\
                <td>&lt;0.35</td>\
                <td>%s</td>\
                </tr>'
        temp_str = "".join([temp % (
            str(j + 1) + allergen_temp_output_list[j],
            list_concentration_filter[j],
            result_list_4[j]
        ) for j in range(len(allergen_temp_output_list))])

        # temp_str = "".join([temp % (
        #     str(j + 1) + reagent_info_list_3[j],
        #     list_concentration_filter[j],
        #     result_list_3[j],
        #     result_list_4[j]
        # ) for j in range(len(reagent_info_list_3))])

        # for j in range(len(reagent_info_list_3)):
        #     str_temp = temp
        #     temp_str = temp_str + str_temp % (str(j + 1) + reagent_info_list_3[j], result_list_3[j], result_list_4[j])
        return self.html_content, temp_str

    # outdate
    # def filterData(self, ori_data, para_data):
    #     row = 8
    #     column = 5
    #     ori_data_temp = [ori_data[i * column:i * column + column] for i in range(row)]
    #     ori_data_corrected = [[b_row[j] if a_row[j] != '' else '' for j in range(len(a_row))]
    #                           for a_row, b_row in zip(para_data, ori_data_temp)]
    #     result_data = []
    #     for i in range(0, len(ori_data_corrected), 2):
    #         result_data.extend([item for pair in zip(*ori_data_corrected[i:i + 2]) for item in pair if item])
    #     return result_data

    def filterData(self, ori_data, para_data):
        row = 8
        column = 5
        ori_data_temp = [ori_data[i * column:i * column + column] for i in range(row)]
        ori_data_corrected = [[b_row[j] if a_row[j] != '' else '' for j in range(len(a_row))]
                              for a_row, b_row in zip(para_data, ori_data_temp)]
        output_list = []
        # 遍历每个子列表
        for sublist in ori_data_corrected:
            # 从子列表中选取非空字符串并添加到output_list
            output_list.extend(item for item in sublist if item != '')
        return output_list