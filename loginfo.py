import logging
import platform

fname = 'script'
uname = platform.node()
logger = logging.getLogger(uname)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(f"{fname}.log", mode='w')
formatter_1 = logging.Formatter("%(name)s %(filename)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter_1)
logger.addHandler(handler)
logger.info("This is a info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")
