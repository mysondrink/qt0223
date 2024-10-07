"""
@Description：数据库增删改查类
@Author：mysondrink@163.com
@Time：2024/2/28 17:33
"""
import sqlite3
try:
    import util.frozen as frozen
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen

FAILED_CODE = 404
SUCCEED_CODE = 202
SQL_PATH = frozen.app_path() + r'/res/db/orangepi-pi.db'

INSERT_PATIENT_SQL = """
    insert into patient_copy1(name, patient_id, age, gender)
                        values (?, ?, ?, ?)
    """

INSERT_IMG_SQL = """
    INSERT INTO reagent_copy1(
        reagent_type, reagent_photo, gray_aver, nature_aver)
        VALUES (?, ?, ?, ?)
    """

UPDATE_SQL = """
    UPDATE reagent_copy1
    SET patient_id = ?, reagent_time = ?, reagent_code = ?, 
        doctor = ?, depart = ?, reagent_matrix = ?, 
        reagent_time_detail = ?, reagent_matrix_info = ?, patient_name = ?,
        patient_age = ?, patient_gender = ?, points = ?
    WHERE reagent_photo = ?
    """

SET_ID_SQL = """
    UPDATE reagent_copy1 SET id = reagent_id WHERE reagent_photo = ?
    """

SELECT_ALL_REAGENT_SQL = """
    SELECT * FROM reagent_copy1 WHERE reagent_photo = ?
    """

SELECT_ID_ALL_REAGENT_SQL = """
    SELECT * FROM reagent_copy1 WHERE reagent_id = ?
    """

UPLOAD_SQL = """
    UPDATE reagent_copy1 
    SET reagent_matrix_info = ? , gray_aver = ?, points = ? 
    WHERE reagent_photo = ?
    """

UPLOAD_SQL_ADD_MODIFY_TIME = """
    UPDATE reagent_copy1 
    SET reagent_matrix_info = ? , gray_aver = ?, points = ?, reagent_time = ?, reagent_time_detail = ? 
    WHERE reagent_photo = ?
    """

SEARCH_REAGENT_ID = """
    SELECT reagent_id FROM reagent_copy1 WHERE reagent_photo = ?
    """

SEARCH_ALL_USER = """
    SELECT * FROM user_table
    """

INSERT_USER_INFO = """
    INSERT INTO user_table(user_name, user_code) VALUES (?, ?)
    """

INSERT_SPLINE_INFO = """
    INSERT INTO t_spline(spline_id, light_matrix, concentration_matrix) VALUES (?, ?, ?)
    """

UPDATE_SPLINE_INFO = """
    UPDATE t_spline
    SET curve_id = ?
    WHERE spline_id = ?
"""

SEARCH_SPLINE_POINTS = """
    SELECT * FROM t_spline WHERE spline_id = ?
    """


SEARCH_ALL_CURVE = """
    SELECT curve_id FROM t_curve
    """

SEARCH_CURVE_POINTS_VALUE = """
    SELECT * FROM t_curve WHERE curve_id = ?
    """

UPDATE_CURVE_SQL = """
    UPDATE t_curve
    SET s0_glow_value = ?, s0_concentration = ?, s1_glow_value = ?, 
        s1_concentration = ?, s2_glow_value = ?, s2_concentration = ?,
        s3_glow_value = ?, s3_concentration = ?, s4_glow_value = ?,
        s4_concentration = ?, s5_glow_value = ?, s5_concentration = ?
    WHERE curve_id = ?
    """

UPDATE_SPLINE_INFO_FROM_EXCEL = """
    UPDATE t_spline
    SET light_matrix = ?, concentration_matrix = ?
    WHERE spline_id = ?
    """

UPDATE_NATURE_AVER_FROM_EXCEL = """
    UPDATE reagent_copy1
    SET nature_aver = ?
    WHERE reagent_photo = ?
    """

INSERT_ALLERGEN_MATRIX = """
    INSERT INTO matrix_table(reagent_type, reagent_matrix, reagent_matrix_info, status) VALUES (?, ?, ?, ?)
    """

SELECT_ALLERGEN_INFO = """
    SELECT * FROM matrix_table WHERE status = 0
    """

DELETE_ALLERGEN_INFO = """
    UPDATE matrix_table SET STATUS = 1 WHERE reagent_type = ?
    """

UPDATE_ALLERGEN_INFO = """
    UPDATE matrix_table SET reagent_matrix_info = ? WHERE reagent_type= ?
    """

SELECT_ALLERGEN_MATRIX_INFO = """
    SELECT reagent_matrix_info FROM matrix_table WHERE status = 0 AND reagent_type = ?
    """

# 修改数据库试剂卡信息 'UPDATE matrix_table SET reagent_matrix_info = ? WHERE reagent_type= ? AND reagent_matrix = ?'
# 删除数据库试剂卡信息 'UPDATE matrix_table SET STATUS = 1 WHERE reagent_type = ?'
# 读取数据库，获取试剂卡信息 'SELECT * FROM matrix_table WHERE STATUS = 0'
# 插入数据到数据库 'INSERT INTO matrix_table(reagent_type, reagent_matrix, reagent_matrix_info) VALUES (?, ?, ?)'


def insertMySql(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        if len(args) == 1:
            # inserting test allergen info
            print("insert img")
            data = args[0]
            cur.execute(INSERT_IMG_SQL, list(data.values()))
            conn.commit()
        elif len(args) == 2:
            # inserting patient and reagent info
            print("insert and update and set info")
            info = args[0]
            data = args[1]
            cur.execute(INSERT_PATIENT_SQL, list(info.values()))
            cur.execute(UPDATE_SQL, list(data.values()))
            cur.execute(SET_ID_SQL, [data['reagent_photo']])
            conn.commit()
        elif len(args) == 5:
            # uploading data from excel
            print("update info")
            id_list = args[0]
            status_list = args[1]
            reagent_info_list = args[2]
            points_list = args[3]
            gray_aver_list = args[4]
            for i, j in zip(id_list, range(len(id_list))):
                if status_list[j] == 0:
                    break
                # MySQL syntax
                # print(sql)  # check SQL syntax
                cur.execute(UPLOAD_SQL, [reagent_info_list[j], points_list[j] + ',' + gray_aver_list[j], points_list[j], i])  # execute SQL syntax
                # from datetime import datetime
                # # 获取当前时间
                # now = datetime.now()
                # # 格式化日期部分
                # date_part = now.strftime('%Y-%m-%d')
                # # 格式化时间部分
                # time_part = now.strftime('%H:%M:%S')
                # reagent_time = date_part
                # reagent_time_detail = time_part
                # cur.execute(
                #     UPLOAD_SQL_ADD_MODIFY_TIME,
                #     [
                #         reagent_info_list[j],
                #         points_list[j] + ',' + gray_aver_list[j],
                #         points_list[j],
                #         reagent_time,
                #         reagent_time_detail,
                #         i
                #     ]
                # )  # execute SQL syntax
                conn.commit()  # commit func using save change to database
            return j + 1
    except Exception as e:
        conn.rollback()
        print(e)
    cur.close()
    conn.close()


def selectMySql(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        if len(args) == 1:
            data = args[0]
            try:
                cur.execute(SELECT_ALL_REAGENT_SQL, [data])
                for i in cur.fetchall():
                    gray_aver_sql = i[15]
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
            cur.close()
            conn.close()
            return gray_aver_sql
        elif len(args) == 2:
            print("select2")
    except Exception as e:
        print(e)
        conn.rollback()
    cur.close()
    conn.close()


def changePhoto(id_reagent):
    # MySQL语句
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 执行SQL语句
        cur.execute(SELECT_ID_ALL_REAGENT_SQL, [id_reagent])
        for i in cur.fetchall():
            item_type = i[0][4:]
            patient_id = i[1]
            pic_name = i[2]
            pic_path = i[3]
            reagent_id = i[4]
            code_num = i[5]
            doctor = i[6]
            depart = i[7]
            reagent_matrix = i[8]
            row_exetable = reagent_matrix[0]
            column_exetable = reagent_matrix[2]
            cur_time = []
            cur_time.append(pic_path)
            cur_time.append(i[9])
            reagent_matrix_info = i[10]
            patient_name = i[11]
            patient_age = i[12]
            patient_gender = i[13]
            age = i[12]
            gender = i[13]
            name = i[11]
            name_pic = pic_name
            point_str = i[14]
            gray_aver_str = i[15]
            nature_aver_str = i[16]
            data_json = dict(patient_id=patient_id, patient_name=patient_name,
                             patient_age=patient_age, patient_gender=patient_gender,
                             item_type=item_type, pic_name=pic_name, reagent_id=reagent_id,
                             time=cur_time, doctor=doctor,
                             depart=depart, age=age,
                             gender=gender, name=name,
                             matrix=reagent_matrix, code_num=code_num,
                             pic_path=pic_path, name_pic=name_pic,
                             row_exetable=row_exetable, column_exetable=column_exetable,
                             reagent_matrix_info=reagent_matrix_info, point_str=point_str,
                             gray_aver_str=gray_aver_str, nature_aver_str=nature_aver_str)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    cur.close()
    conn.close()
    return data_json


def searchId(_name):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 提交事务
        cur.execute(SEARCH_REAGENT_ID, [_name])
        conn.commit()
    except Exception as e:
        print(str(e))
        # 有异常，回滚事务
        conn.rollback()
    _id, *rest = cur.fetchall()[0]
    cur.close()
    conn.close()
    return _id


def totalPage(*args):
    """
    获取查询总页数
    Args:
        *args: 查询的参数

    Returns:
        total: 查询总页数
    """
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 提交事务
        cur.execute(args[0], [*args[1:]])
        conn.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        conn.rollback()
    total = len(cur.fetchall())
    cur.close()
    conn.close()
    return total


def getSQLiteInfo(*args):
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 提交事务
        cur.execute(args[0], [*args[1:]])
        conn.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        conn.rollback()

    time_list = []
    patient_id_list = []
    reagent_id_list = []
    name_list = []
    """
    按照数据库数据排序，对数据进行处理
    获取第二行为病人号码改为获取第六行为样本条码
    获取第四行和第十行为采样时间
    获取第五行为试剂卡编号
    获取第十二行为病人姓名
    """
    for x in cur.fetchall():
        # patient_id_list.append(str(x[1]))
        patient_id_list.append(str(x[5]))
        time_list.append(x[3] + " " + x[9])
        reagent_id_list.append(str(x[4]))
        name_list.append(x[11])

    # 释放内存
    cur.close()
    conn.close()

    return patient_id_list, time_list, reagent_id_list, name_list


def setUserDict():
    """
    用户字典生成
    Returns:
        None
    """
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(SEARCH_ALL_USER)
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()
    user_name = []
    user_code = []

    for x in cursor.fetchall():
        user_name.append(x[0])
        user_code.append(x[1])

    user_dict = dict(zip(user_name, user_code))

    # 释放内存
    cursor.close()
    connection.close()
    return user_dict


def insertUser(username, usercode):
    """
    注册用户写入数据库
    Args:
        username: 用户名
        usercode: 密码

    Returns:
        None
    """
    user_name = username
    user_code = usercode
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(INSERT_USER_INFO, [user_name, user_code])
        # 提交事务
        connection.commit()
    except Exception as e:
        print(str(e))
        # 有异常，回滚事务
        connection.rollback()
        return FAILED_CODE
    # 释放内存
    cursor.close()
    connection.close()
    return SUCCEED_CODE

def insertCurveTable(curve_id, light_matrix, concentration_matrix):
    _id = curve_id
    _l = light_matrix
    _c = concentration_matrix
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(INSERT_SPLINE_INFO, [_id, _l, _c])
        # 提交事务
        connection.commit()
    except Exception as e:
        print(str(e))
        # 有异常，回滚事务
        connection.rollback()
        return FAILED_CODE
    # 释放内存
    cursor.close()
    connection.close()
    return SUCCEED_CODE

def insertSingleCurveTable(spline_id, curve_id):
    _s = spline_id
    _id = curve_id
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(UPDATE_SPLINE_INFO, [_s, _id])
        # 提交事务
        connection.commit()
    except Exception as e:
        print(str(e))
        # 有异常，回滚事务
        connection.rollback()
        return FAILED_CODE
    # 释放内存
    cursor.close()
    connection.close()
    return SUCCEED_CODE

def getCurvePoints(curve_id):
    _c = curve_id
    conn = sqlite3.connect(SQL_PATH)
    cur = conn.cursor()
    try:
        # 提交事务
        cur.execute(SEARCH_SPLINE_POINTS, [_c])
        conn.commit()
    except Exception as e:
        print(str(e))
        # 有异常，回滚事务
        conn.rollback()
    _, _, light_matrix, concentration_matrix, _ = cur.fetchall()[0]
    cur.close()
    conn.close()
    return light_matrix, concentration_matrix

def setCurveDict():
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(SEARCH_ALL_CURVE)
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()
    curve_id_list = []

    for x in cursor.fetchall():
        curve_id_list.append(x[0])

    # 释放内存
    cursor.close()
    connection.close()
    return curve_id_list

def getCurvePointsData(curve_id):
    _c = curve_id
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(SEARCH_CURVE_POINTS_VALUE, [_c])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()
    result = None

    for x in cursor.fetchall():
        result = x[2:]

    # 释放内存
    cursor.close()
    connection.close()
    return list(result)

def updateCurvePointsData(data, curve_id):
    points_len = 6
    _c = curve_id
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(UPDATE_CURVE_SQL, [*data[:points_len*2], _c])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    cursor.close()
    connection.close()

def updateSingleConFromUpload(spline_id, light_m, concentration_m):
    _s = spline_id
    _l = light_m
    _c = concentration_m
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(UPDATE_SPLINE_INFO_FROM_EXCEL, [_l, _c, _s])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    cursor.close()
    connection.close()

def updateNatureAverFromUpload(reagent_id, nature_aver):
    _id = reagent_id
    _a = nature_aver
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(UPDATE_NATURE_AVER_FROM_EXCEL, [_a, _id])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    cursor.close()
    connection.close()

def insertAllergenMatrix(reagent_type, reagent_matrix, reagent_matrix_info):
    _t = reagent_type
    _m = reagent_matrix
    _i = reagent_matrix_info
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(INSERT_ALLERGEN_MATRIX, [_t, _m, _i, 0])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    cursor.close()
    connection.close()

def selectAllergenInfo():
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(SELECT_ALLERGEN_INFO)
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()
    list1 = []
    list2 = []
    list3 = []
    for x in cursor.fetchall():
        # self.reagent_type.append(x[1])
        # self.reagent_matrix.append(x[2])
        # self.reagent_matrix_info.append(x[3])
        list1.append(x[1])
        list2.append(x[2])
        list3.append(x[3])
    # 释放内存
    cursor.close()
    connection.close()
    return list1, list2, list3

def deleteAllergenMatrix(reagent_type):
    _t = reagent_type
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(DELETE_ALLERGEN_INFO, [_t])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    cursor.close()
    connection.close()

def updateAllergenMatrix(reagent_type, reagent_matrix_info):
    _t = reagent_type
    _m = reagent_matrix_info
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(UPDATE_ALLERGEN_INFO, [_m, _t])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    cursor.close()
    connection.close()

def selectAllergenType():
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(SELECT_ALLERGEN_INFO)
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()
    list1 = []
    for x in cursor.fetchall():
        list1.append(x[1])

    # 释放内存
    cursor.close()
    connection.close()
    return list1

def selectAllergenMatrixInfo(item_type):
    _i = item_type
    connection = sqlite3.connect(SQL_PATH)
    cursor = connection.cursor()
    try:
        # 执行SQL语句
        cursor.execute(SELECT_ALLERGEN_MATRIX_INFO, [_i])
        # 提交事务
        connection.commit()
    except Exception as e:
        # print(str(e))
        # 有异常，回滚事务
        connection.rollback()

    # 释放内存
    data, *rest = cursor.fetchall()[0]
    cursor.close()
    connection.close()
    return data
