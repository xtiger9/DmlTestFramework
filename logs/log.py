import logging
import os.path
import time
from colorama import Fore, Style

# 定义日志级别字典
log_level_dict = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}

log_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
# 保存的日志的完整名称
if os.getcwd().__contains__('logs'):
    log_file = "../logs/" + log_name + ".log"
else:
    log_file = os.getcwd() + "/logs/" + log_name + ".log"


class Logger(object):
    """彩色日志类"""

    def __init__(self, logger, log_file=log_file, log_level=log_level_dict['debug']):
        """指定保存日志的文件路径，日志级别；将日志输出到：控制台 和 指定日志文件"""
        self.log_file = log_file
        self.log_level = log_level
        # 设置logger名称
        self.logger = logging.getLogger(name=logger)
        # 设置参数级别
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        # 判断handlers是否存在
        if not self.logger.handlers:
            # 写入控制台
            console_stream = logging.StreamHandler()
            console_stream.setLevel(self.log_level)
            console_stream.setFormatter(self.formatter)
            self.logger.addHandler(console_stream)
            # 写入文件
            file_stream = logging.FileHandler(self.log_file, mode='a', encoding='utf-8')
            file_stream.setLevel(self.log_level)
            file_stream.setFormatter(self.formatter)
            self.logger.addHandler(file_stream)

    def debug(self, msg):
        """定义debug输出的日志颜色 debug -> white"""
        # self.logger.debug(Fore.WHITE + "DEBUG - " + str(msg) + Style.RESET_ALL)
        self.logger.debug("DEBUG - " + str(msg))

    def info(self, msg):
        """定义info输出的日志颜色 info -> green"""
        # self.logger.info(Fore.GREEN + "INFO - " + str(msg) + Style.RESET_ALL)
        self.logger.info("INFO - " + str(msg))

    def warning(self, msg):
        """定义warning输出的日志颜色 warning -> red"""
        # self.logger.warning(Fore.RED + "WARNING - " + str(msg) + Style.RESET_ALL)
        self.logger.warning("WARNING - " + str(msg))

    def error(self, msg):
        """定义error输出的日志颜色 error -> red"""
        # self.logger.error(Fore.RED + "ERROR - " + str(msg) + Style.RESET_ALL)
        self.logger.error("ERROR - " + str(msg))

    def critical(self, msg):
        """定义critical输出的日志颜色 critical -> red"""
        # self.logger.critical(Fore.RED + "CRITICAL - " + str(msg) + Style.RESET_ALL)
        self.logger.critical("CRITICAL - " + str(msg))


if __name__ == '__main__':
    log = Logger(logger="test")
    log.debug("debug")
    log.info("info")
    log.error("error")
    log.warning("warning")
    log.critical("critical")
