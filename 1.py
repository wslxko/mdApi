import os
import argparse
import logging
import sys

FORMAT = '[%(asctime)s, %(levelname)-7s]: %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('spider')
logger.setLevel(logging.INFO)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-wp", "--work-path", default="", help="work path")
    parser.add_argument("-fn", "--file-name", default="name", help="file name")
    parser.add_argument("-ty", "--task-type", required=True, help="file_type:zh_en or en_zh")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    logger.info("Start split it ...")
    work_path = args.work_path
    file_name = args.file_name
    type = args.task_type
    print(work_path)
    print(file_name)
    print(type)
