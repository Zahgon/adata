# -*- coding: utf-8 -*-
"""
@desc: 热点榜单

同花顺热点榜单
https://eq.10jqka.com.cn/frontend/thsTopRank/index.html?fontzoom=no&client_userid=ceZLR&share_hxapp=gsc&share_action=webpage_share.hot_list_1714369375634&back_source=wxhy#/

@author: 1nchaos
@time: 2024/4/29
@log: change log
"""
import pandas as pd

from adata.common.headers import ths_headers
from adata.common.utils import requests
from adata.sentiment.alist import AList


class Hot(AList):  # 参考 pylint 改完之后实际上这个 Hot 和 AList 没有啥实例化的意义
    """热门榜单"""

    # 东方财富人气榜
    @staticmethod
    def pop_rank_100_east():
        """
        东方财富人气榜100
        http://guba.eastmoney.com/rank/
        """
        pass

    @staticmethod
    def hot_rank_100_ths():
        """
        同花顺热股100
        https://dq.10jqka.com.cn/fuyao/hot_list_data/out/hot_list/v1/stock?stock_type=a&type=hour&list_type=normal
        """
        api_url = (
            "https://dq.10jqka.com.cn/fuyao/hot_list_data/out/hot_list/v1/stock?stock_type=a&type=hour&list_type=normal"
        )
        headers = ths_headers.json_headers
        headers["Host"] = "dq.10jqka.com.cn"
        res = requests.request(method="get", url=api_url, params={}, headers=headers)
        data = res.json()["data"]["stock_list"]
        data_list = []
        for d in data:
            try:
                if "tag" in d and "concept_tag" in d["tag"]:
                    d["concept_tag"] = ";".join(d["tag"]["concept_tag"])
                if "popularity_tag" in d["tag"]:
                    d["pop_tag"] = d["tag"]["popularity_tag"].replace("\n", "")
                data_list.append(d)
            except:
                pass
        rename = {
            "order": "rank",
            "rise_and_fall": "change_pct",
            "code": "stock_code",
            "name": "short_name",
            "rate": "hot_value",
            "concept_tag": "concept_tag",
        }
        rank_df = pd.DataFrame(data).rename(columns=rename)
        rank_df = rank_df[["rank", "stock_code", "short_name", "change_pct", "hot_value", "pop_tag", "concept_tag"]]
        return rank_df

    @staticmethod
    def hot_concept_20_ths(plate_type=1):
        """
        同花热门概念板块
        :param plate_type: 1.概念板块，2.行业板块；默认：概念板块
        """
        pass


if __name__ == "__main__":
    print(Hot().hot_rank_100_ths())
    # print(Hot().pop_rank_100_east())
    # print(Hot().hot_concept_20_ths(plate_type=1))
    # print(Hot().hot_concept_20_ths(plate_type=2))
