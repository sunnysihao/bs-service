from sanic import Sanic
from sanic.log import logger, error_logger, access_logger, server_logger
from sanic.response import *
from loguru import logger as rulog
import logging
from logging.handlers import RotatingFileHandler


app = Sanic('tlog')
# logger.addHandler(logging.FileHandler(r"D:\Desktop\bs-service\bs-service\bs-service\service\server_logs\log.txt"))
# rulog.add(r"D:\Desktop\bs-service\bs-service\bs-service\service\server_logs\log.txt")
file_handler = RotatingFileHandler(r"D:\Desktop\bs-service\bs-service\bs-service\service\server_logs\log.txt")
file_handler.suffix = "%Y%m%d"
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s: %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

server_logger.addHandler(file_handler)
server_logger.setLevel("WARNING")
logger.setLevel("INFO")
# rulog.add(file_log)
@app.route('/')
async def ttt(request):
    logger.info('infoooooooooooooooooo')
    server_logger.warning('warningggggggggggg')
    return text('done')


if __name__ == '__main__':
    app.run(access_log=True)
