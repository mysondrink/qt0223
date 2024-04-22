"""
@Description：
@Author：mysondrink@163.com
@Time：2024/4/15 15:54
"""
import re

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
try:
    import util.frozen as frozen
    from third_party.keyboard.abstractkeyboard import abstractkeyboard
    from third_party.keyboard.keybutton import keybutton
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.third_party.keyboard.abstractkeyboard import abstractkeyboard
    from qt0223.third_party.keyboard.keybutton import keybutton

NORMAL_BUTTON_WIDTH = 55
NORMAL_BUTTON_HEIGHT = 45

BACKSPACE_ICON = frozen.app_path() + r"/third_party/keyboard/Image/backspace.png"
CLOSE_ICON = frozen.app_path() + r"/third_party/keyboard/Image/close.png"

BUTTON_SPACING_RATIO = 0.030
BUTTON_WIDTH_RATIO = 0.09
BUTTON_HEIGHT_RATIO = 0.2

list_4 = ['0', '1', '2']
list_1 = ['4', '5', '6']
list_2 = ['7', '8', '9']
list_3 = ['.', 'back', 'close']
list_key = {
    "0": Qt.Key_0,
    "1": Qt.Key_1,
    "2": Qt.Key_2,
    "3": Qt.Key_3,
    "4": Qt.Key_4,
    "5": Qt.Key_5,
    "6": Qt.Key_6,
    "7": Qt.Key_7,
    "8": Qt.Key_8,
    "9": Qt.Key_9,
    ".": Qt.Key_unknown,
    "back": Qt.Key_Backspace,
    "close": Qt.Key_Close
}

qss = "QLineEdit {                    \
            border-style: none;        \
            padding: 3px;              \
            border-radius: 5px;        \
            border: 1px solid #dce5ec; \
            font-size: 30px;           \
        }                              \
        "


class MyNumKeyBoard(abstractkeyboard):
    info_msg = Signal(str)
    pressedChanged = Signal(int, str)

    def __init__(self) -> object:
        """
        构造函数
        初始化键盘布局界面
        Returns:
            object: 实现键盘类
        """
        super().__init__()
        self.m_isChinese = False
        self.InitUI()
        self.resetButton()

    def InitUI(self) -> None:
        """
        初始化键盘布局界面
        Returns:
            None
        """
        self.pressedChanged.connect(super().onKeyPressed)
        self.layout = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h1.setSizeConstraint(QLayout.SetNoConstraint)
        self.h2.setSizeConstraint(QLayout.SetNoConstraint)
        self.h3.setSizeConstraint(QLayout.SetNoConstraint)
        self.h4.setSizeConstraint(QLayout.SetNoConstraint)

        self.pinyin = ''
        # 1为中文,0为英文
        self.flag_CtoE = 1
        # 1为大写,0为小写
        self.flag_UtoL = 0

        for i in range(len(list_1)):
            button = keybutton(list_1[i])
            button.setText(list_1[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h1.addWidget(button)
        for i in range(len(list_2)):
            button = keybutton(list_2[i])
            button.setText(list_2[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h2.addWidget(button)
        for i in range(len(list_3)):
            button = keybutton(list_3[i])
            button.setText(list_3[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h3.addWidget(button)
        for i in range(len(list_4)):
            button = keybutton(list_4[i])
            button.setText(list_4[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h4.addWidget(button)

        self.layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.layout.addLayout(self.h4, 15)
        self.layout.addLayout(self.h1, 15)
        self.layout.addLayout(self.h2, 15)
        self.layout.addLayout(self.h3, 15)
        self.setLayout(self.layout)

    def resetButton(self) -> None:
        """
        重置键盘按钮
        Returns:
            None
        """
        button = self.findChildren(QPushButton)
        for i in button:
            if i.value == 'back':
                i.setText('')
                i.setIcon(QIcon(BACKSPACE_ICON))
                i.setIconSize(QSize(40, 40))
            elif i.value == 'close':
                i.setText('')
                i.setIcon(QIcon(CLOSE_ICON))
                i.setIconSize(QSize(40, 40))

    def getButtonInfo(self, info) -> None:
        """
        槽函数
        获取当前当前键盘按钮的值
        Args:
            info: 键盘按钮的值

        Returns:
            None
        """
        if info == 'close':
            self.info_msg.emit('close')
            return
        super().onKeyPressed(list_key[info], info)
