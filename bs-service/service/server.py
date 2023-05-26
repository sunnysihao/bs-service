from sanic import Sanic
from sanic.response import *
from sanic.exceptions import NotFound
from sanic.log import logger, error_logger, access_logger, server_logger
import logging
from logging.handlers import RotatingFileHandler
from service_logger import my_logger


app = Sanic(name='BSservice')

my_logger(output_dir=r"D:\Desktop\bs-service\bs-service\bs-service\service\server_logs")
@app.route("/index")
async def hello(request):
    # access_logger.info("access info")
    server_logger.warning("server_warning")
    return json({
        "data": 'hello',
        "message": 'world',
        "params": request.args.get('a')
    })

@app.route('/')
async def ttt(request):
    # access_logger.info('access info')
    server_logger.warning('warningggggggggggg')
    return text('done')

# 未定义路由响应
@app.exception(NotFound)
def ignore_404s(request, exception):
    error_logger.exception("not found warn log*****************")
    return text("404 - Not found")

@app.route('/sum')
async def sum(request):
    a = request.args.get('a')
    b = request.args.get('b')
    sum = str(int(a) / int(b))
    return text(sum)
    # try:
    #     sum = str(int(a)/int(b))
    #     return text(sum)
    # except Exception as e:
    #     server_logger.error(e)
    #     return text('')



if __name__ == '__main__':
    app.run(host='localhost', port=8000, access_log=True)



