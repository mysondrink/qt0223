import os
import re
import cv2 as cv
import datetime
import numpy as np
try:
    from view.gui.info import *
    import util.frozen as frozen
    from util import dirs
    from util.report import MyReport
    from view.AbstractPage import AbstractPage, ProcessDialog
    from controller.USBController import CheckUSBThread
    # import middleware.database as insertdb
    from pic_code.img_main import img_main
except ModuleNotFoundError:
    from qt0223.view.gui.info import *
    import qt0223.util.frozen as frozen
    from qt0223.util import dirs
    from qt0223.util.report import MyReport
    from qt0223.view.AbstractPage import AbstractPage, ProcessDialog
    from qt0223.controller.USBController import CheckUSBThread
    # import qt0223.middleware.database as insertdb
    from qt0223.pic_code.img_main import img_main



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
        self.pix_table_model = QStandardItemModel(
            self.row_exetable + int(self.row_exetable / 2), self.column_exetable
        )
        self.pix_table_model_copy = QStandardItemModel(
            self.row_exetable + int(self.row_exetable / 2) + 2,
            self.column_exetable
        )
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
        # creating a report display
        self.setTableWidget(self.data['item_type'], self.allergy_info, self.data['nature_aver_str'])

    def setTableWidget(self, item_type, reagent_info, nature_aver_str):
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
        text = MyReport().gethtml(item_type, reagent_info, nature_aver_str)
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
        if msg == 202:
            self.usbthread.deleteLater()
            info = "下载完成！"
            self.showInfoDialog(info)
        elif msg == 404:
            self.usbthread.deleteLater()
            info = "U盘未插入或无法访问！"
            self.showInfoDialog(info)
        elif msg == 405:
            self.usbthread.deleteLater()
            info = "图片读取失败或未找到图片！"
            self.showInfoDialog(info)

    def showDataView(self, data):
        """
        定位点数据展示
        Args:
            data: 过敏原信息

        Returns:
            None
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
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_time = self.test_time
        Data_Base = [self.data['patient_name'], self.data['patient_gender'], self.data['patient_id'],
                    self.data['code_num'], '检测组合' + self.data['item_type'], test_time, time_now]
        gray_aver_str = self.data['gray_aver_str'].split(",")
        nature_aver_str = self.data['nature_aver_str'].split(",")
        array_gray_aver = np.array(gray_aver_str)
        array_nature_aver = np.array(nature_aver_str)
        matrix_gray_aver = array_gray_aver.reshape(9, 5)
        matrix_nature_aver = array_nature_aver.reshape(9, 5)
        Data_Nature = matrix_nature_aver
        Data_Light = matrix_gray_aver
        Main = img_main()
        if Main.natPrint(Data_Base, Data_Nature, Data_Light):
            dialog.closeDialog()
            info = "输出表格成功!"
            self.update_info.emit(info)
        else:
            dialog.closeDialog()
            info = "输出表格失败!"
            self.update_info.emit(info)

    @Slot()
    def on_btnDownload_clicked(self):
        """
        槽函数
        下载按钮操作
        Returns:
            None
        """
        print("Download")
        name = self.data['name_pic']
        path = self.data['pic_path']
        data = self.data
        self.usbthread = CheckUSBThread(name, path, data, self.data['point_str'] + ',' + self.allergy_info)
        self.usbthread.update_json.connect(self.getUSBInfo)
        # 创建定时器
        self.download_timer = QTimer()
        self.download_timer.timeout.connect(self.usbthread.start)
        self.download_timer.timeout.connect(self.download_timer.stop)
        # 设置定时器延迟时间，单位为毫秒
        # 延迟2秒跳转
        delay_time = 2000
        self.download_timer.start(delay_time)
        m_title = ""
        m_info = "下载中..."
        # infoMessage(m_info, m_title, 300)
        info = "下载中..."
        self.showInfoDialog(info)

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
        self.ui.stackedWidget.setCurrentIndex(0)

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