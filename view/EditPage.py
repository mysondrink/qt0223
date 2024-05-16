"""
@Description：检测组合设置界面显示
@Author：mysondrink@163.com
@Time：2024/1/11 10:45
"""
import sys
import traceback
page_dict = {'page': '检疫设置主页', 'page2': '添加试剂页', 'page3': '删除试剂页', 'page4': '修改试剂页', 'page5': '过敏原页'}
LINEEDIT_STYLE = "font: 20pt;background-color: rgb(255, 255, 127);"
try:
    import util.frozen as frozen
    # from func.infoPage import infoMessage
    from view.TestPage import allergen
    from view.gui.edit import *
    from third_party.keyboard.keyboard import KeyBoard
    from view.AbstractPage import AbstractPage
    import middleware.database as insertdb
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    # from func.infoPage import infoMessage
    from qt0223.view.TestPage import allergen
    from qt0223.view.gui.edit import *
    from qt0223.third_party.keyboard.keyboard import KeyBoard
    from qt0223.view.AbstractPage import AbstractPage
    import qt0223.middleware.database as insertdb


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
        # self.ui.rowCb.addItems(["8x5"])
        self.resetBtn()

        self.setBtnIcon()
        self.ui.reagentTable.verticalHeader().setVisible(False)
        self.ui.reagentTable.horizontalHeader().setVisible(False)
        self.ui.reagentTable.setShowGrid(True)

        self.setFocusWidget()
        self.installEvent()

    def setReagentTable(self, num):
        """
        设置过敏原表格
        Args:
            num: 表格类型，1为添加表格，2为修改表格

        Returns:
            None
        """
        try:
            row = self.ui.reagentTable.model().rowCount()
            column = self.ui.reagentTable.model().columnCount()
        except AttributeError:
            row = 4
            column = 5
        if num == 1:
            # 插入数据库
            self.pix_reagent_table_model = QStandardItemModel(row, column)
            self.ui.reagentTable.setModel(self.pix_reagent_table_model)

            self.ui.reagentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.reagentTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            # 测试数据
            a = 100
            test_data = [str(i) for i in range(a, a + row * column)]
            #
            for i in range(row):
                for j in range(column):
                    _lineEdit = QLineEdit(self)
                    # 测试数据
                    _lineEdit.setText(test_data[i * row + j])
                    #
                    _lineEdit.setStyleSheet(LINEEDIT_STYLE)
                    _lineEdit.setObjectName("lineedit")
                    _lineEdit.setFocusPolicy(Qt.ClickFocus)
                    _lineEdit.installEventFilter(self)
                    self.ui.reagentTable.setIndexWidget(self.pix_reagent_table_model.index(i, j), _lineEdit)
        else:
            # 查询数据库
            self.pix_reagent_table_model = QStandardItemModel(row, column)
            self.ui.reagentTable.setModel(self.pix_reagent_table_model)

            self.ui.reagentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.reagentTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

            allergen_str = self.reagent_matrix_info[self.reagent_type.index(self.ui.editCb.currentText())]
            list1 = allergen_str.split(",")
            list2 = [list1[i:i + column] for i in range(0, len(list1), column)]
            result = []
            for i in range(0, row * 2, 2):
                result.append([a + b for a, b in zip(list2[i], list2[i + 1])])
            for i in range(row):
                for j in range(column):
                    _lineEdit = QLineEdit(self)
                    _lineEdit.setText(result[i][j])
                    _lineEdit.setStyleSheet(LINEEDIT_STYLE)
                    _lineEdit.setObjectName("lineedit")
                    _lineEdit.setFocusPolicy(Qt.ClickFocus)
                    _lineEdit.installEventFilter(self)
                    self.ui.reagentTable.setIndexWidget(self.pix_reagent_table_model.index(i, j), _lineEdit)

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
        安装事件监听
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
        elif obj.objectName() == "lineedit":
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
        self.ui.nameLine.setText("")
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
        self.allergen_type = []
        self.allergen_matrix = []
        self.allergen_matrix_info = []
        self.reagent_type, self.reagent_matrix, self.reagent_matrix_info = insertdb.selectAllergenInfo()
        self.ui.deleteCb.clear()
        self.ui.deleteCb.addItems(self.reagent_type)
        self.ui.editCb.clear()
        self.ui.editCb.addItems(self.reagent_type)

    def readPixtableNum(self, num):
        """
        读取表格内容，同时以str形式保存到数据库
        Args:
            num: 读取添加和修改页面的表格

        Returns:
            None
        """
        allergen_matrix_info = []
        row = self.ui.reagentTable.model().rowCount()
        column = self.ui.reagentTable.model().columnCount()
        if num == 1:
            return
        else:
            for i in range(row):
                list1 = []
                list2 = []
                for j in range(column):
                    index = self.ui.reagentTable.model().index(i, j)
                    lineEdit = self.ui.reagentTable.indexWidget(index)
                    data = lineEdit.text()
                    if (i * row + j) % 2 == 0:
                        list1.append(data)
                        list1.append("")
                    else:
                        list2.append("")
                        list2.append(data)
                list2.append("")
                allergen_matrix_info.extend(list1 + list2[1:])
            result = ",".join(allergen_matrix_info)
            return result

    def insertMatrix(self, name, item_type):
        """
        插入数据到数据库
        Args:
            name: 试剂卡名称
            item_type: 试剂卡规格

        Returns:
            None
        """
        allergen_matrix = self.readPixtableNum(2)
        insertdb.insertAllergenMatrix(name, item_type, allergen_matrix)

    def operation_edit(self):
        """
        修改页面跳转判断
        Returns:
            槽函数
        """
        if self.reagent_num == 1:
            # 添加数据
            print("insertMatrix")
            self.insertMatrix(self.add_name, self.add_matrix_type)
            # self.setReagentCb()
            # m_title = ""
            # m_info = "成功！"
            # infoMessage(m_info, m_title)
            self.resetBtn()
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.reagent_num == 2:
            # 修改数据
            print("updateMatrix")
            str_name = self.ui.editCb.currentText()
            self.updateReagentDB(str_name)
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
        flag = insertdb.deleteAllergenMatrix(item_type)

    def updateReagentDB(self, name):
        """
        修改数据库试剂卡信息
        Args:
            name: 检测组合名称

        Returns:
            None
        """
        matrix = self.readPixtableNum(2)
        flag = insertdb.updateAllergenMatrix(name, matrix)

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
        if self.ui.stackedWidget.currentIndex() == 1:
            name_text = self.ui.nameLine.text()
            print(name_text)
            if name_text == '':
                info = "请输入内容！"
                self.showInfoDialog(info)
                return
            # 添加
            # row_t = 4
            # column_t = 5

            self.add_matrix_type = "8x5"
            self.add_name = self.ui.nameLine.text()
            self.reagent_num = 1
            self.setReagentTable(1)
            self.ui.stackedWidget.setCurrentIndex(4)
        elif self.ui.stackedWidget.currentIndex() == 2:
            # 删除
            self.deleteItem()
            info = "操作成功！"
            self.showInfoDialog(info)
        elif self.ui.stackedWidget.currentIndex() == 3:
            # 修改
            self.reagent_num = 2
            str_cb = self.reagent_matrix[self.reagent_type.index(self.ui.editCb.currentText())]
            self.setReagentTable(2)
            self.ui.stackedWidget.setCurrentIndex(4)
        elif self.ui.stackedWidget.currentIndex() == 4:
            info = "操作成功！"
            self.showInfoDialog(info)
            self.operation_edit()

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

