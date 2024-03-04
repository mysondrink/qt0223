"""
@Description：软件更新类
@Author：mysondrink@163.com
@Time：2024/3/4 13:46
"""
import time
import os
import zipfile
try:
    import util.frozen as frozen
    from controller.AbstractThread import AbstractThread
except ModuleNotFoundError:
    import qt0223.util.frozen as frozen
    from qt0223.controller.AbstractThread import AbstractThread

TIME_TO_SLEEP = 2
TRYLOCK_TIME = -1
FAILED_CODE = 404
SUCCEED_CODE = 202

MY_ZIP = frozen.app_path() + r'/update.zip'
MY_DIR = frozen.app_path()


class MyUpdateThread(AbstractThread):
    def __init__(self) -> object:
        """
        构造函数
        初始化线程，调用父类方法进行日志记录
        Returns:
            object
        """
        super().__init__()

    def run(self) -> None:
        """
        线程运行函数
        进行数据库的检测
        Returns:
            None
        """
        try:
            with zipfile.ZipFile(MY_ZIP, 'r') as zip_ref:
                zip_ref.extractall(MY_DIR)
                time.sleep(TIME_TO_SLEEP)
                info_msg = "更新成功！"
                code_msg = SUCCEED_CODE
                status_msg = self.currentThread()
                self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            if os.path.exists(MY_ZIP):
                os.remove(MY_ZIP)
        except Exception as e:
            self.sendException()
            info_msg = "更新失败！"
            code_msg = FAILED_CODE
            status_msg = 1
            self.update_json.emit(dict(info=info_msg, code=code_msg, status=status_msg))
            if os.path.exists(MY_ZIP):
                os.remove(MY_ZIP)
        finally:
            self.log_thread.deleteLater()
            if os.path.exists(MY_ZIP):
                os.remove(MY_ZIP)
