"""
@Description：摄像头管理类
@Author：mysondrink@163.com
@Time：2024/1/9 10:32
"""
from PySide2.QtCore import Signal
import time
try:
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    from qt0223.controller.AbstractThread import AbstractThread


TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202


class CheckCameraThread(AbstractThread):
    def __init__(self):
        """
        构造函数
        初始化线程，调用父类方法进行日志记录
        """
        super().__init__()

    def run(self):
        """
        线程运行函数
        进行相机的检测
        Returns:
            None
        """
        try:
            # qmutex.tryLock(trylock_time)
            info_msg = "摄像头检测中。。。"
            code_msg = SUCCEED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            time.sleep(TIME_TO_SLEEP)
            info_msg = "连接摄像头成功！"
            code_msg = SUCCEED_CODE
            status_msg = self.currentThread()
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            # qmutex.unlock()
        except Exception as e:
            self.sendException()
            info_msg = "camera error！"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
        finally:
            self.log_thread.deleteLater()