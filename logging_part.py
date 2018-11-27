import logging, traceback

# 设置日志级别
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()


def logging_test():
    try:
        logger.debug(u"1除以0")
        1 / 0
    except Exception:
        # traceback.format_exc()返回字符串，traceback.print_exc()直接打印
        logger.error(traceback.format_exc()), traceback.print_exc()
        logging.error(u"出错了")
        logger.info(u"1除以0info")
        logger.warning(u"1除以0warning")
        logging.error(u"出错了")

if __name__ == '__main__':
    logging_test()