# -*- coding: utf-8 -*-
"""
@desc: 雪花算法 生成唯一 全局id
       使用方式 单例模式使用
       import worker
@author: 1nchaos
@time: 2022/4/8
@log: change log
"""

import logging
import random
import time

# 64位ID的划分
WORKER_ID_BITS = 5
DATACENTER_ID_BITS = 5
SEQUENCE_BITS = 12

# 最大取值计算 # 2**5-1 0b11111
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)
MAX_DATACENTER_ID = -1 ^ (-1 << DATACENTER_ID_BITS)

# 移位偏移计算
WORKER_ID_SHIFT = SEQUENCE_BITS
DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)

# Twitter元年时间戳
TWEPOCH = 1580885600337

logger = logging.getLogger('flask.app')


class _IdWorker(object):
    """
    用于生成雪花算法 id的对象
    """

    def __init__(self, datacenter_id=1, worker_id=1, sequence=0):
        """
        初始化
        :param datacenter_id: 数据中心（机器区域）ID
        :param worker_id: 机器ID
        :param sequence: 其实序号
        """
        # sanity check
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id值越界')
        if datacenter_id > MAX_DATACENTER_ID or datacenter_id < 0:
            raise ValueError('datacenter_id值越界')

        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.sequence = sequence
        # 上次计算的时间戳
        self.last_timestamp = -1


    def _gen_timestamp(self):
        """
        生成整数时间戳
        :return:int timestamp
        """
        pass

    def _til_next_millis(self, last_timestamp):
        """
        等到下一毫秒
        """
        pass

    def id(self):
        """
        获取新ID
        :return:
        """
        pass


# 随机分配机器id 和 数据中心
worker = _IdWorker(random.randint(0, 31), random.randint(0, 31))

if __name__ == '__main__':
    print(worker.id())
