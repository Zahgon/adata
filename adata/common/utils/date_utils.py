# -*- coding: utf-8 -*-
"""
@desc: readme
@author: 1nchaos
@time: 2024/7/23
@log: change log
"""
from datetime import datetime, timedelta


def get_n_days_date(days=0, fmt="%Y-%m-%d"):
    """
    获取 N 天后的日期，
    :param days: 天数；N可以是负数，表示N天前的日期
    :param fmt: 日期格式；默认：%Y-%m-%d
    :return: 对应的日期
    """
    pass


def get_cur_time(fmt="%Y-%m-%d %H:%M:%S"):
    """
    获取当前时间，
    """
    return datetime.now().strftime(fmt)
