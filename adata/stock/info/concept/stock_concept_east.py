# -*- coding: utf-8 -*-
"""
@summary: 股票概念
东方财富股票概念

https://data.eastmoney.com/bkzj/gn.html

单个股票的所有概念板块
https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_F10_CORETHEME_BOARDTYPE&columns=SECUCODE%2CSECURITY_CODE%2CSECURITY_NAME_ABBR%2CNEW_BOARD_CODE%2CBOARD_NAME%2CSELECTED_BOARD_REASON%2CIS_PRECISE%2CBOARD_RANK%2CBOARD_YIELD%2CDERIVE_BOARD_CODE&quoteColumns=f3~05~NEW_BOARD_CODE~BOARD_YIELD&filter=(SECUCODE%3D%22600138.SH%22)(IS_PRECISE%3D%221%22)&pageNumber=1&pageSize=&sortTypes=1&sortColumns=BOARD_RANK&source=HSF10&client=PC&v=0029565688091059528
@author: 1nchaos
@date: 2023/3/30 16:17
"""

import pandas as pd

from adata.common import requests
from adata.common.utils.code_utils import compile_exchange_by_stock_code
from adata.stock.info.cache import get_all_concept_code_east_csv_path
from adata.stock.info.concept.stock_concept_template import StockConceptTemplate


class StockConceptEast(StockConceptTemplate):
    """
    东方财富股票概念
    """

    def __init__(self) -> None:
        super().__init__()

    def all_concept_code_east(self, wait_time=None):
        """
        https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=1000&po=1&np=1&fields=f12%2Cf13%2Cf14%2Cf62&fid=f62&fs=m%3A90%2Bt%3A3
        :return: 概念[[name,index_code，concept_code]]
        """
        # 1. 请求获取所有概念
        try:
            curr_page = 1
            page_size = 100
            data = []
            while curr_page < 50:
                url = f"https://push2.eastmoney.com/api/qt/clist/get" \
                      f"?pn={curr_page}&pz={page_size}&po=1&np=1&fields=f12%2Cf13%2Cf14%2Cf62&fid=f62&fs=m%3A90%2Bt%3A3"
                res_json = requests.request('get', url, headers={}, proxies={}, wait_time=wait_time).json()
                res_data = res_json['data']['diff']
                if not res_data:
                    break
                for _ in res_data:
                    data.append({'index_code': _['f12'], 'concept_code': _['f12'], 'name': _['f14'], 'source': '东方财富'})
                if len(res_data) < page_size:
                    break
                curr_page += 1
            result_df = pd.DataFrame(data=data, columns=self._CONCEPT_CODE_COLUMNS)
        except Exception as e:
            result_df = pd.DataFrame(data=[], columns=self._CONCEPT_CODE_COLUMNS)
        # 2. 读取缓存文件 结果拼接去重
        csv_df = pd.read_csv(get_all_concept_code_east_csv_path())
        result_df = pd.concat([result_df, csv_df], ignore_index=True).drop_duplicates(subset=['concept_code'])
        return result_df

    def concept_constituent_east(self, concept_code=None, wait_time=None):
        """
        https://data.eastmoney.com/bkzj/BK1085.html
        https://push2.eastmoney.com/api/qt/clist/get?fid=f62&po=1&pz=1000&pn=1&np=1&fltt=2&invt=2&fs=b:BK0966&fields=f12,f14
        :param wait_time: 等待时间：毫秒；表示每个请求的间隔时间，主要用于防止请求太频繁的限制。
        :param concept_code: 概念代码，BK开头
        :return: 概念的成分股
        """
        pass

    def get_concept_east(self, stock_code: str = '000001'):
        """
        根据股票代码获取，股票所属的所有的概念信息
        https://datacenter.eastmoney.com/securities/api/data/v1/get?
        reportName=RPT_F10_CORETHEME_BOARDTYPE
        &columns=SECUCODE%2CSECURITY_CODE%2CSECURITY_NAME_ABBR%2CNEW_BOARD_CODE%2CBOARD_NAME%2CSELECTED_BOARD_REASON%2CIS_PRECISE%2CBOARD_RANK%2CBOARD_YIELD%2CDERIVE_BOARD_CODE
        &quoteColumns=f3~05~NEW_BOARD_CODE~BOARD_YIELD
        &filter=(SECUCODE%3D%22600138.SH%22)(IS_PRECISE%3D%221%22)
        &pageNumber=1&pageSize=&sortTypes=1&sortColumns=BOARD_RANK&source=HSF10&client=PC&v=0029565688091059528
        :param stock_code: 股票代码
        :return: 概念信息
        """
        pass

    def get_plate_east(self, stock_code: str = '000001', plate_type=None):
        """
        根据股票代码获取，股票所属的所有的板块相关的信息
        :param stock_code: 股票代码
        :param plate_type: 1. 行业 2. 地域板块 3.概念 默认：0全部
        :return: 板块信息
        """
        pass


if __name__ == '__main__':
    print(StockConceptEast().all_concept_code_east())
    # print(StockConceptEast().concept_constituent_east(concept_code="BK0637"))
    # print(StockConceptEast().get_concept_east(stock_code="600020").to_string())
    # print(StockConceptEast().get_plate_east(stock_code="600020", plate_type=1).to_string())
