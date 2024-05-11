"""
@Description：检测组合设置界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:45
"""
import sys
import traceback
page_dict = {'page': 0, 'page2': 1, 'page3': 2, 'page4': 3, 'page5': 4}
try:
    import util.frozen as frozen
    # from func.infoPage import infoMessage
    from view.TestPage import allergen
    from view.gui.edit import *
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    # from func.infoPage import infoMessage
    from qt0223.view.TestPage import allergen
    from qt0223.view.gui.edit import *
    from qt0223.third_party.keyboard.keyboard import KeyBoard
    from qt0223.view.AbstractPage import AbstractPage


class EditPage(Ui_Form, AbstractPage):
    def __init__(self):
        """
        初始化加载界面信息，同时创建记录异常的信息
        """
        super().__init__()
        self.reagent_num = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        """
        设置界面相关信息
        Returns:
            None
        """
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.rowCb.addItems(["8x5"])
        self.resetBtn()

        self.setBtnIcon()
        self.ui.reagentTable.verticalHeader().setVisible(False)
        self.ui.reagentTable.horizontalHeader().setVisible(False)
        self.ui.reagentTable.setShowGrid(True)

        self.setFocusWidget()
        self.installEvent()

    def setReagentTable(self, row, column, num):
        """
        设置过敏原表格
        Args:
            row: 表格的行
            column: 表格的列
            num: 表格类型，1为添加表格，2为修改表格

        Returns:
            None
        """
        if num == 1:
            self.row_reagent_table = row
            self.column_reagent_table = column
            self.pix_reagent_table_model = QStandardItemModel(self.row_reagent_table + int(self.row_reagent_table / 2), self.column_reagent_table)
            self.ui.reagentTable.setModel(self.pix_reagent_table_model)

            self.ui.reagentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.reagentTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            for i in range(0, self.row_reagent_table + int(self.row_reagent_table / 2)):
                if i % 3 == 0:
                    for j in range(0, self.column_reagent_table):
                        content_cb = QComboBox(self)
                        content_cb.addItems(allergen)
                        content_cb.setCurrentIndex(0)
                        content_cb.setEditable(True)
                        _lineEdit = content_cb.lineEdit()
                        _lineEdit.setAlignment(Qt.AlignCenter)
                        # content_cb.setStyleSheet(self.cb_style_sheet)
                        self.ui.reagentTable.setIndexWidget(self.pix_reagent_table_model.index(i, j), content_cb)
        else:
            self.row_reagent_table = row
            self.column_reagent_table = column
            self.pix_reagent_table_model = QStandardItemModel(self.row_reagent_table + int(self.row_reagent_table / 2),
                                                              self.column_reagent_table)
            self.ui.reagentTable.setModel(self.pix_reagent_table_model)

            self.ui.reagentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.reagentTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

            str_num = self.reagent_matrix_info[self.reagent_type.index(self.ui.editCb.currentText())]

            for i in range(0, self.row_reagent_table + int(self.row_reagent_table / 2)):
                if i % 3 == 0:
                    for j in range(0, self.column_reagent_table):
                        content_cb = QComboBox(self)
                        content_cb.addItems(allergen)
                        num = int(str_num[j + (i % 3) * self.row_reagent_table])
                        content_cb.setCurrentIndex(num)
                        content_cb.setEditable(True)
                        _lineEdit = content_cb.lineEdit()
                        _lineEdit.setAlignment(Qt.AlignCenter)
                        # content_cb.setStyleSheet(self.cb_style_sheet)
                        self.ui.reagentTable.setIndexWidget(self.pix_reagent_table_model.index(i, j), content_cb)

    def setBtnIcon(self):
        """
        设置按钮图标
        Returns:
            None
        """
        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnConfirm.setIconSize(QSize(32, 32))
        self.ui.btnConfirm.setIcon(QIcon(confirm_icon_path))

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        add_icon_path = frozen.app_path() + r"/res/icon/add.png"
        pixImg = self.mySetIconSize(add_icon_path)
        self.ui.add_icon_label.setPixmap(pixImg)
        self.ui.add_icon_label.setAlignment(Qt.AlignCenter)

        delete_icon_path = frozen.app_path() + r"/res/icon/delete.png"
        pixImg = self.mySetIconSize(delete_icon_path)
        self.ui.delete_icon_label.setPixmap(pixImg)
        self.ui.delete_icon_label.setAlignment(Qt.AlignCenter)

        edit_icon_path = frozen.app_path() + r"/res/icon/edit.png"
        pixImg = self.mySetIconSize(edit_icon_path)
        self.ui.edit_icon_label.setPixmap(pixImg)
        self.ui.edit_icon_label.setAlignment(Qt.AlignCenter)

    def mySetIconSize(self, path):
        """
        设置按钮图标比例
        Args:
            path: 图标路径

        Returns:
            None
        """
        img = QImage(path)  # 创建图片实例
        mgnWidth = 50
        mgnHeight = 50  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        pixImg = QPixmap.fromImage(
            img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中
        return pixImg

    def installEvent(self):
        """
        安装时间监听
        Returns:
            None
        """
        for item in self.focuswidget:
            item.installEventFilter(self)

    def setFocusWidget(self):
        """
        设置组件点击焦点
        Returns:
            None
        """
        self.focuswidget = [self.ui.nameLine]
        for item in self.focuswidget:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event):
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
                return True
            else:
                return False
        else:
            return False

    def setKeyBoard(self, obj):
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
            self.keyboardtext.nameLabel.setText("试剂卡型号")
        self.keyboardtext.showWindow()

    def getKeyBoardText(self, msg):
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

    def resetBtn(self):
        """
        重置按钮信息，返回编辑首页
        Returns:
            None
        """
        self.ui.btnConfirm.hide()
        self.ui.btnReturn.setGeometry(10, 10, 780, 80)

    def resetBtn_2(self):
        """
        重置按钮信息，当发生页面跳转时触发
        Returns:
            None
        """
        self.ui.btnConfirm.show()
        self.ui.btnReturn.setGeometry(410, 10, 380, 80)

    def setReagentCb(self):
        """
        读取数据库，获取试剂卡信息
        Returns:
            None
        """
        connection = pymysql.connect(host="127.0.0.1", user="root", password="password", port=3306, database="test",
                                     charset='utf8')
        # MySQL语句
        sql = 'SELECT * FROM matrix_table'
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
        self.reagent_type = []
        self.reagent_matrix = []
        self.reagent_matrix_info = []

        for x in cursor.fetchall():
            self.reagent_type.append(x[1])
            self.reagent_matrix.append(x[2])
            self.reagent_matrix_info.append(x[3])

        # self.ui.modeBox_1.clear()
        # self.ui.modeBox_3.clear()
        # self.ui.modeBox_1.addItems(self.reagent_type)
        # self.ui.modeBox_1.setCurrentIndex(-1)
        # self.ui.typeLabel.setText("")
        # self.ui.modeBox_3.addItems(self.reagent_type)
        # self.ui.modeBox_3.setCurrentIndex(-1)

        self.ui.deleteCb.clear()
        self.ui.deleteCb.addItems(self.reagent_type)
        self.ui.editCb.clear()
        self.ui.editCb.addItems(self.reagent_type)

        # 释放内存
        cursor.close()
        connection.close()

    def readPixtableNum(self, num):
        """
        读取表格内容，同时以list形式保存到数据库
        Args:
            num: 读取添加和修改页面的表格

        Returns:
            None
        """
        str_num = ""
        if num == 1:
            return
        else:
            for i in range(self.row_reagent_table + int(self.row_reagent_table / 2)):
                # row_list = []
                if i % 3 == 0:
                    for j in range(self.column_reagent_table):
                        index = self.ui.reagentTable.model().index(i, j)  # 获取单元格的 QModelIndex 对象
                        combo_box = self.ui.reagentTable.indexWidget(index)  # 获取该单元格中的 QComboBox 对象
                        data_index = combo_box.currentIndex()
                        # current_text = combo_box.currentText()  # 获取 QComboBox 当前选中的文本
                        str_num = str_num + str(data_index)
        return str_num

    def insertMatrix(self, name, item_type):
        """
        插入数据到数据库
        Args:
            name: 试剂卡名称
            item_type: 试剂卡规格

        Returns:
            None
        """
        matrix = self.readPixtableNum(2)
        connection = pymysql.connect(host="127.0.0.1", user="root", password="password", port=3306, database="test",
                                     charset='utf8')
        # MySQL语句
        sql = 'INSERT INTO matrix_table(reagent_type, reagent_matrix, reagent_matrix_info) VALUES (%s,%s,%s)'

        # 获取标记
        cursor = connection.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, [name, item_type, matrix])
            # 提交事务
            connection.commit()
        except Exception as e:
            # print(str(e))
            # 有异常，回滚事务
            connection.rollback()
        # 释放内存
        cursor.close()
        connection.close()

    def edit(self):
        """
        修改页面跳转判断
        Returns:
            槽函数
        """
        if self.reagent_num == 1:
            self.insertMatrix(self.add_name, self.add_matrix_type)
            self.setReagentCb()
            # m_title = ""
            # m_info = "成功！"
            # infoMessage(m_info, m_title)
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.reagent_num == 2:
            item_type = self.reagent_matrix[self.reagent_type.index(self.ui.editCb.currentText())]
            str_name = self.ui.editCb.currentText()
            self.updateReagentDB(str_name, item_type)
            self.setReagentCb()
            # m_title = ""
            # m_info = "成功！"
            # infoMessage(m_info, m_title)
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)

    def deleteItem(self):
        """
        删除页面跳转判断
        Returns:
            槽函数
        """
        item = self.ui.deleteCb.currentText()
        self.deleteReagentDB(item)
        self.resetBtn()
        self.ui.stackedWidget.setCurrentIndex(0)

    def deleteReagentDB(self, item_type):
        """
        删除数据库试剂卡信息
        需要修改
        Args:
            item_type: 试剂卡名称

        Returns:
            None
        """
        # matrix = self.readPixtableNum(2)
        connection = pymysql.connect(host="127.0.0.1", user="root", password="password", port=3306, database="test",
                                     charset='utf8')
        # MySQL语句
        sql = 'DELETE FROM matrix_table WHERE reagent_type = %s'

        # 获取标记
        cursor = connection.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, item_type)
            # 提交事务
            connection.commit()
        except Exception as e:
            # print(str(e))
            # 有异常，回滚事务
            connection.rollback()
        # 释放内存
        cursor.close()
        connection.close()

    def updateReagentDB(self, name, item_type):
        """
        修改数据库试剂卡信息
        Args:
            name:
            item_type:

        Returns:

        """
        matrix = self.readPixtableNum(2)
        connection = pymysql.connect(host="127.0.0.1", user="root", password="password", port=3306, database="test",
                                     charset='utf8')
        # MySQL语句
        sql = 'UPDATE matrix_table SET reagent_matrix_info = %s WHERE reagent_type= %s AND reagent_matrix = %s'

        # 获取标记
        cursor = connection.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql, [matrix, name, item_type])
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
    def on_btnAdd_clicked(self):
        """
        添加按钮操作
        槽函数
        Returns:

        """
        self.resetBtn_2()
        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def on_btnDelete_clicked(self):
        """
        删除按钮操作
        槽函数
        Returns:

        """
        self.resetBtn_2()
        self.ui.stackedWidget.setCurrentIndex(2)
        self.setReagentCb()

    @Slot()
    def on_btnModify_clicked(self):
        """
        修改按钮操作
        槽函数
        Returns:

        """
        self.resetBtn_2()
        self.ui.stackedWidget.setCurrentIndex(3)
        self.setReagentCb()

    @Slot()
    def on_btnConfirm_clicked(self):
        """
        确认按钮操作
        槽函数
        Returns:

        """
        return
        if self.ui.stackedWidget.currentIndex() == 1:
            # 添加
            dict_mode = {
                "2x3": 1,
                "2x5": 2,
                "4x5": 3,
                "8x5": 4,
            }
            if dict_mode.get(self.ui.rowCb.currentText()) == 1:
                row_t = 2
                column_t = 3
            elif dict_mode.get(self.ui.rowCb.currentText()) == 2:
                row_t = 2
                column_t = 5
            elif dict_mode.get(self.ui.rowCb.currentText()) == 3:
                row_t = 4
                column_t = 5
            else:
                row_t = 8
                column_t = 5

            self.add_matrix_type = self.ui.rowCb.currentText()
            self.add_name = self.ui.nameLine.text()
            self.reagent_num = 1
            self.setReagentTable(row_t, column_t, 1)
            self.ui.stackedWidget.setCurrentIndex(4)
        elif self.ui.stackedWidget.currentIndex() == 2:
            # 删除
            m_title = ""
            m_info = "确认中..."
            infoMessage(m_info, m_title, 380)
            # 创建定时器
            self.change_timer = QTimer()
            self.change_timer.timeout.connect(self.deleteItem())
            # 设置定时器延迟时间，单位为毫秒
            # 延迟2秒跳转
            delay_time = 2000
            self.change_timer.start(delay_time)
        elif self.ui.stackedWidget.currentIndex() == 3:
            # 修改
            self.reagent_num = 2
            str_cb = self.reagent_matrix[self.reagent_type.index(self.ui.editCb.currentText())]
            row = int(str_cb[0])
            col = int(str_cb[2])
            self.setReagentTable(row, col, 2)
            self.ui.stackedWidget.setCurrentIndex(4)
        elif self.ui.stackedWidget.currentIndex() == 4:
            m_title = ""
            m_info = "成功！"
            infoMessage(m_info, m_title, 400)
            self.edit()
            # # 创建定时器
            # self.change_timer = QTimer()
            # self.change_timer.timeout.connect(self.edit)
            # # 设置定时器延迟时间，单位为毫秒
            # # 延迟2秒跳转
            # delay_time = 2000
            # self.change_timer.start(delay_time)

    @Slot()
    def on_btnReturn_clicked(self):
        """
        返回按钮操作
        槽函数
        Returns:

        """
        if self.ui.stackedWidget.currentIndex() == 0:
            page_msg = 'HomePage'
            self.next_page.emit(page_msg)
        else:
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)

