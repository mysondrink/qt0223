"""
@Description：
@Author：mysondrink@163.com
@Time：2024/4/12 15:30
"""
try:
    import util.frozen as frozen
except:
    import qt0223.util.frozen as frozen


class MyCurve():
    def filterCurvePoints(self, item_type, light_info, concentration_info):
        light_info_temp = [i for i in light_info.split(",")][5:]
        concentration_info_temp = [i for i in concentration_info.split(",")][5:]

        path = frozen.app_path() + r"/res/allergen/"
        with open(path + item_type, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()
            allergen = [i.rstrip() for i in lines][5:]
        result_list_1 = [light_info_temp[i] for i in range(len(allergen)) if allergen[i] != ""]
        result_list_2 = [concentration_info_temp[i] for i in range(len(allergen)) if allergen[i] != ""]
        float_list_1 = [float(i) for i in result_list_1]
        float_list_2 = [float(i) for i in result_list_2]
        curve_points = [(i, j) for i, j in zip(float_list_2, float_list_1)]
        return curve_points
