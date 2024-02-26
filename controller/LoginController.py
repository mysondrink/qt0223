"""
@Description：登录注册控制
@Author：mysondrink@163.com
@Time：2024/1/10 11:18
"""
import pymysql
try:
    from controller.AbstractController import AbstractController
except ModuleNotFoundError:
    from qt0223.controller.AbstractController import AbstractController

FAILED_CODE = 404
SUCCEED_CODE = 202


class LoginController(AbstractController):
    def __init__(self):
        """
        构造函数
        """
        super().__init__()
        self.setUserDict()

    def __del__(self):
        """
        析构函数
        """
        super().__del__()

    def setUserDict(self) -> None:
        """
        用户字典生成
        Returns:
            None
        """
        connection = pymysql.connect(host="127.0.0.1", user="root", password="password", port=3306, database="test",
                                     charset='utf8')
        # MySQL语句
        sql = 'SELECT * FROM user_table'
        # 获取标记
        cursor = connection.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
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

        self.user_dict = dict(zip(user_name, user_code))

        # 释放内存
        cursor.close()
        connection.close()

    def authUser(self, msg) -> None:
        """
        槽函数
        用户信息校验
        Args:
            msg: view发送来的信息，包括用户名和密码

        Returns:
            None
        """
        name = msg['name']
        password = msg['password']
        if self.user_dict.get(name) is None or self.user_dict.get(name) != password:
            self.update_json.emit(dict(code=FAILED_CODE))
        else:
            self.update_json.emit(dict(code=SUCCEED_CODE))
        return
