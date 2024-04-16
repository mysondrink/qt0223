"""
@Description：
@Author：mysondrink@163.com
@Time：2024/4/15 10:20
"""
try:
    import util.frozen as frozen
    from view.gui.curve import *
    from view.AbstractPage import AbstractPage
    import middleware.database as insertdb
    from third_party.keyboard.numkeyboard import NumKeyBoard
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.view.gui.curve import *
    from qt0223.view.AbstractPage import AbstractPage
    import qt0223.middleware.database as insertdb
    from qt0223.third_party.keyboard.numkeyboard import NumKeyBoard
from PySide2.QtCharts import QtCharts

QChartView = QtCharts.QChartView
QChart = QtCharts.QChart
QSplineSeries = QtCharts.QSplineSeries


class CurvePage(Ui_Form, AbstractPage):
    next_page = Signal(str)
    update_json = Signal(dict)
    update_log = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        curve_name_list = insertdb.setCurveDict()
        self.ui.modeBox_1.addItems(curve_name_list)
        self.ui.modeBox_1.setCurrentIndex(-1)
        self.ui.modeBox_1.currentIndexChanged.connect(self.setLineNum)
        self.paraline_list = []
        self.traverse_widgets(self)
        self.traverse_widgets2get_data()
        self.setMyChart()
        self.setFocusWidget()
        self.installEvent()

        return_icon_path = frozen.app_path() + r"/res/icon/return.png"
        self.ui.btnReturn.setIconSize(QSize(32, 32))
        self.ui.btnReturn.setIcon(QIcon(return_icon_path))

        confirm_icon_path = frozen.app_path() + r"/res/icon/confirm.png"
        self.ui.btnDump.setIconSize(QSize(32, 32))
        self.ui.btnDump.setIcon(QIcon(confirm_icon_path))

    def installEvent(self) -> None:
        """
        安装事件监听
        Returns:
            None
        """
        for item in self.paraline_list:
            item.installEventFilter(self)

    def setFocusWidget(self) -> None:
        """
        设置组件点击焦点
        Returns:
            None
        """
        # self.focuswidget = [self.ui.nameLine, self.ui.numLine]
        for item in self.paraline_list:
            item.setFocusPolicy(Qt.ClickFocus)

    def eventFilter(self, obj, event) -> bool:
        """
        槽函数
        事件过滤
        Args:
            obj: 发生事件的组件
            event: 发生的事件

        Returns:
            bool: 处理掉事件
        """
        if obj in self.paraline_list:
            if event.type() == QEvent.Type.FocusIn:
                # print(obj.setText("hello"))
                self.setKeyBoard(obj)
                return True
            else:
                return False
        else:
            return False

    def setKeyBoard(self, obj) -> None:
        """
        槽函数
        设置可以键盘弹出的组件
        Args:
            obj: 键盘弹出的组件

        Returns:
            None
        """
        self.keyboardtext = NumKeyBoard()
        self.keyboardtext.text_msg.connect(self.getKeyBoardText)
        obj_num = int(obj.objectName()[-2:])
        obj_text = obj.text()
        self.keyboardtext.textInput.setText(obj_text)
        if obj_num % 2:
            self.keyboardtext.nameLabel.setText(f"s{(obj_num - 1)%10} 发光值")
        else:
            self.keyboardtext.nameLabel.setText(f"s{(obj_num - 1)%10} 浓度")
        self.keyboardtext.showWindow()

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

    def traverse_widgets(self, widget, depth=0):
        # 对于每一个子组件
        for child in widget.children():
            # 如果子组件是QWidget类型
            if isinstance(child, QWidget):
                # 打印缩进的组件名称
                if isinstance(child, QLineEdit):
                    self.paraline_list.append(child)
                    # print("True?") if int(child.objectName()[-2:]) % 2 else print("False!")
                # print("  " * depth + type(child).__name__)
                # 递归遍历子组件的子组件
                self.traverse_widgets(child, depth + 1)

    def traverse_widgets2get_data(self):
        lst_sorted = sorted(self.paraline_list, key=lambda x: int(x.objectName()[-2:]))
        self.paraline_list = lst_sorted[:20]
        self.paraline_list_2 = lst_sorted[20:]

    def setLineNum(self):
        curve_id = self.ui.modeBox_1.currentText()
        value = insertdb.getCurvePointsData(curve_id)
        flag = [j.setText(str(i)) for i, j in zip(value[:20], self.paraline_list) if i is not None]
        flag = [j.setText(str(i)) for i, j in zip(value[20:], self.paraline_list_2) if i is not None]
        self.updateChart([i for i in value[:20] if i is not None])
        # print(value)

    def setMyChart(self):
        layout = QHBoxLayout()
        self.ui.page_4.setLayout(layout)
        mychart = QChart()
        # mychart.setTitle('Line Chart 1')
        self.myseries = QSplineSeries(mychart)
        # self.myseries.setName("主曲线")
        mychart.addSeries(self.myseries)
        mychart.createDefaultAxes()  # 创建默认轴
        mychart.legend().setVisible(False)    # 取消点位显示
        self.chartview = QChartView(mychart)
        self.chartview.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

        layout.addWidget(self.chartview)

    def updateChart(self, data):
        # self.myseries.clear()
        if self.myseries is not None:
            self.chartview.chart().removeSeries(self.myseries)
            self.myseries.deleteLater()
            self.myseries = None
        self.myseries = QSplineSeries()
        sorted_coordinates = list(zip(data[::2], data[1::2]))
        LIGHT_DATA = [(y, x) for x, y in sorted_coordinates]
        sorted_coordinates = sorted(LIGHT_DATA, key=lambda x: x[0])  # 按照横坐标进行从小到大排序
        for i in sorted_coordinates:
            self.myseries << QPointF(*i)
        # chart.legend().setVisible(False)    # 取消点位显示
        # self.chartview.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # self.chartview.chart().update()
        # layout.addWidget(self.chartview)
        self.chartview.chart().addSeries(self.myseries)
        self.chartview.chart().createDefaultAxes()
        self.chartview.repaint()

    @Slot()
    def on_pushButton_clicked(self):
        cur_index = (self.ui.stackedWidget.currentIndex() + 1) % self.ui.stackedWidget.count()
        self.ui.stackedWidget.setCurrentIndex(cur_index)

    @Slot()
    def on_btnReturn_clicked(self):
        page_msg = 'HomePage'
        self.next_page.emit(page_msg)

    @Slot()
    def on_btnDump_clicked(self):
        info = "保存中。。。"
        self.showInfoDialog(info)
        print("spline print")
        if self.ui.modeBox_1.currentIndex() == -1:
            print("Error!")
            info = "未选择曲线"
            self.showInfoDialog(info)
            return
        try:
            result = [i.text() for i in self.paraline_list if i.text() != '']
            insertdb.updateCurvePointsData([float(item) for item in result], self.ui.modeBox_1.currentText())
            info = "保存成功"
            self.showInfoDialog(info)
            print("spline success")
        except Exception as e:
            print(e)
            info = "保存失败"
            self.showInfoDialog(info)
            print("spline success")
            return


