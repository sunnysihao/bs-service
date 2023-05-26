from os.path import *
import logging
from logging.handlers import RotatingFileHandler
from sanic.log import server_logger, access_logger, error_logger
import sys


def my_logger(level="INFO", backup_count=10, output_dir=None):
    level = level.upper()
    log_file = join(output_dir, 'server_log.txt')
    file_handler = RotatingFileHandler(log_file, maxBytes=1*1024, backupCount=backup_count, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.suffix = "%Y%m%d"
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s: %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    server_logger.addHandler(file_handler)
    server_logger.setLevel(level)
    error_logger.addHandler(file_handler)
    error_logger.setLevel('ERROR')

    # # print to stdout
    # stream_handler = logging.StreamHandler(sys.stdout)
    # stream_handler.setLevel(level)
    # stream_handler.setFormatter(formatter)
    # access_logger.addHandler(stream_handler)
    #
    # # info
    # length = 20
    # logging.log(level, "-" * length + " logging start " + "-" * length)
    # logging.log(level, "LEVEL: {}".format(logging.getLevelName(level)))
    # logging.log(level, "PATH:  {}".format(log_file))
    # logging.log(level, "-" * (length * 2 + 15))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=str, default="INFO", nargs='?', help="logging level")
    args = parser.parse_args()

    my_logger(args.level)

