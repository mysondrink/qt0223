"""
@Description：注册界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:21
"""
import pymysql
try:
    import util.frozen as frozen
    from view.gui.register import *
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage
    from controller.RegisterController import RegisterController
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.register import *
    from qt0223.third_party.keyboard.keyboard import KeyBoard
    from qt0223.view.AbstractPage import AbstractPage
    from qt0223.controller.RegisterController import RegisterController

class RegisterPage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    def __init__(self):
        """
        构造函数
        初始化注册界面信息，同时创建记录异常的信息
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()
        self.controller = RegisterController()
        self.controller.update_json.connect(self.getControllerInfo)

    def InitUI(self) -> None:
        """
        设置界面相关信息
        Returns:
            None
        """
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        self.setFocusWidget()
        self.installEvent()

    def installEvent(self) -> None:
        """
        安装事件监听
        Returns:
            None
        """
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self) -> None:
        """
        设置组件点击焦点
        Returns:
            None
        """
        self.focuswidget = [self.ui.nameLine, self.ui.pwdLine, self.ui.pwdLine_2]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event) -> None:
        """
        槽函数
        事件过滤
        Args:
            obj: 发生事件的组件
            event: 发生的事件

        Returns:
            None
        """
        if obj in self.focuswidget:
            if event.type() == QEvent.Type.FocusIn:
                # print(obj.setText("hello"))
                self.setKeyBoard(obj)

    def getKeyBoardText(self, msg) -> None:
        """
        槽函数
        获取键盘的文本信息
        Args:
            msg: 信号，键盘文本信息

        Returns:
            None
        """
        self.focusWidget().setText(msg)
        self.focusWidget().clearFocus()

    def setKeyBoard(self, obj) -> None:
        """
        槽函数
        设置可以键盘弹出的组件
        Args:
            obj: 键盘弹出的组件

        Returns:
            None
        """
        self.keyboardtext = KeyBoard()
        self.keyboardtext.text_msg.connect(self.getKeyBoardText)
        obj_name = obj.objectName()
        obj_text = obj.text()
        self.keyboardtext.textInput.setText(obj_text)
        if obj_name == "nameLine":
            self.keyboardtext.nameLabel.setText("用户名")
        elif obj_name == "pwdLine":
            self.keyboardtext.nameLabel.setText("新密码")
        else:
            self.keyboardtext.nameLabel.setText("再次输入")
        self.keyboardtext.showWindow()

    def getControllerInfo(self, msg) -> None:
        """
        获取controller的信息
        Args:
            msg: 返回的信息

        Returns:
            None
        """
        code = msg['code']
        if code == 202:
            page_msg = 'LoginPage'
            self.next_page.emit(page_msg)
            info = "注册成功!"
            self.showInfo(info)
        elif code == 404:
            info = "注册失败!"
            self.showInfo(info)
        return

    def checkName(self) -> None:
        """
        输入检测
        检测输入的用户名和密码
        Returns:
            None
        """
        if self.ui.pwdLine.text() == "" or self.ui.nameLine.text() == "" or self.ui.pwdLine_2.text() == "" :
            info = "请输入用户名或密码！"
            self.showInfo(info)
        elif self.ui.pwdLine.text() != self.ui.pwdLine_2.text():
            info = "两次输入不正确！"
            self.showInfo(info)
        else:
            name = self.ui.nameLine.text()
            password = self.ui.pwdLine.text()
            self.controller.insertUser(name, password)
        return

    def insertUser(self) -> None:
        """
        abandoned
        注册用户写入数据库
        Returns:
            None
        """
        user_name = self.ui.nameLine.text()
        user_code = self.ui.pwdLine.text()
        connection = pymysql.connect(host="127.0.0.1", user="root", password="password", port=3306, database="test",
                                     charset='utf8')
        # MySQL语句
        sql = 'INSERT INTO user_table(user_name, user_code) VALUES (%s,%s)'

        # 获取标记
        cursor = connection.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, [user_name, user_code])
            # 提交事务
            connection.commit()
        except Exception as e:
            # print(str(e))
            # 有异常，回滚事务
            connection.rollback()
        # 释放内存
        cursor.close()
        connection.close()

    @Slot()
    def on_btnReturn_clicked(self) -> None:
        """
        槽函数
        返回按钮操作
        Returns:
            None
        """
        page_msg = 'LoginPage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnConfirm_clicked(self) -> None:
        """
        槽函数
        确认按钮操作
        Returns:
            None
        """
        self.checkName()
