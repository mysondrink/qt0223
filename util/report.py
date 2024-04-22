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
                                    <td>&gt;100 极高</td>\
                                </tr>\
                                <tr>\
                                    <td>50-100 很高</td>\
                                </tr>\
                                <tr>\
                                    <td>17.5-50 非常高</td>\
                                </tr>\
                                <tr>\
                                    <td>3.5-17.5 高</td>\
                                </tr>\
                                <tr>\
                                    <td>0.7-3.5 中</td>\
                                </tr>\
                                <tr>\
                                    <td>0.35-0.7 低</td>\
                                </tr>\
                                <tr>\
                                    <td>&lt;0.35 检测不到</td>\
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
        
    def gethtml(self, item_type, reagent_info, nature_aver_str, concentration_matrix):
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

        path = frozen.app_path() + r"/res/allergen/"
        with open(path + item_type, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            allergen = [i.rstrip() for i in lines][5:]
        row = 8
        column = 5
        allergen_temp = [allergen[i * column:i * column + column] for i in range(row)]
        result_list_3 = self.filterData(result_list_1, allergen_temp)
        result_list_4 = self.filterData(result_list_2, allergen_temp)
        list_concentration_filter = self.filterData(result_list_concentration, allergen_temp)
        # + —结果列表
        # result_list_3 = [result_list_1[i] for i in range(len(allergen)) if allergen[i] != ""]
        # 阴阳性结果列表
        # result_list_4 = [result_list_2[i] for i in range(len(allergen)) if allergen[i] != ""]
        # list_concentration_filter = [result_list_concentration[i] for i in range(len(allergen)) if allergen[i] != ""]

        # 姓名，性别，样本号，条码号，样本类型，测试时间，【结果】，打印时间
        temp = '<tr align="center">\
                <td>%s</td>\
                <td>%s</td>\
                <td>%s</td>\
                <td>%s</td>\
                </tr>'
        temp_str = "".join([temp % (
            str(j + 1) + reagent_info_list_3[j],
            list_concentration_filter[j],
            result_list_3[j],
            result_list_4[j]
        ) for j in range(len(reagent_info_list_3))])
        # for j in range(len(reagent_info_list_3)):
        #     str_temp = temp
        #     temp_str = temp_str + str_temp % (str(j + 1) + reagent_info_list_3[j], result_list_3[j], result_list_4[j])
        return self.html_content, temp_str

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