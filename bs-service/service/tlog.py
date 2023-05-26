from service_logger import MyLogger



def tlog():
    my_log.info('aaaaaaaaaaaaaaaaaaaaaa')

def su(a, b):
    try:
        a/b
    except:
        my_log.exception('wrong')


if __name__ == '__main__':
    my_log = MyLogger()

    # logger.add(sink='log.txt', rotation='10kb', )
    # logger.add(sink=sys.stdout, colorize=True)
    # logger.info("这是一条info")
    # logger.warning("这是一条warning")
    # logger.debug("这是一条debug")
    my_log.warning('warningggggggggggggg')
    tlog()
    su(1,0)