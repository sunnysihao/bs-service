from loguru import logger
import sys



def tlog():
    pass



if __name__ == '__main__':
    logger.add(sink='log.txt', rotation='10kb', )
    logger.add(sink=sys.stdout, colorize=True)
    logger.info("这是一条info")
    logger.warning("这是一条warning")
    logger.debug("这是一条debug")
    tlog()