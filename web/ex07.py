# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 12:18:28 2025

@author: MYCOM
"""
#네이버 스마트 스토어 제품 크롤링(아이폰)
import requests
from bs4 import BeautifulSoup
url = "https://search.shopping.naver.com/ns/search?query=%EC%95%84%EC%9D%B4%ED%8F%B0"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "NAC=0GBPB0gHolNj; NNB=XLAWNIWQYLWWQ; SRT30=1762820373; bnb_tooltip_shown_finance_v1=true; NACT=1; SRT5=1762830955; sus_val=oDqwMUrXZ2H5n3x81DRa+U0t; nstore_session=TlXLqwGZMw4C8t6LJT+WJSx5; RELATED_PRODUCT=ON; OEP_CONFIG=[{%22serId%22:%22shopping%22%2C%22type%22:%22oep%22%2C%22expId%22:%22NNS-PRA-UI%22%2C%22varId%22:%224%22%2C%22value%22:{%22bt%22:%224%22%2C%22is_control%22:false}%2C%22userType%22:%22nnb%22%2C%22provId%22:%22%22%2C%22sesnId%22:%22%22}%2C{%22serId%22:%22shopping%22%2C%22type%22:%22oep%22%2C%22expId%22:%22PWL-EXT-LGC-P2%22%2C%22varId%22:%226%22%2C%22value%22:{%22bt%22:%223%22%2C%22is_control%22:false}%2C%22userType%22:%22nnb%22%2C%22provId%22:%22%22%2C%22sesnId%22:%22%22}%2C{%22serId%22:%22shopping%22%2C%22type%22:%22oep%22%2C%22expId%22:%22QAC-RANK-ADAPT%22%2C%22varId%22:%222%22%2C%22value%22:{%22bt%22:%222%22%2C%22is_control%22:true}%2C%22userType%22:%22nnb%22%2C%22provId%22:%22%22%2C%22sesnId%22:%22%22}%2C{%22serId%22:%22shopping%22%2C%22type%22:%22oep%22%2C%22expId%22:%22NNS-RANKING%22%2C%22varId%22:%2283%22%2C%22value%22:{%22bt%22:%227%22%2C%22is_control%22:false}%2C%22userType%22:%22nnb%22%2C%22provId%22:%22%22%2C%22sesnId%22:%22%22}]; nstore_pagesession=je6q1wqWVrFYDssLWxw-340361; X-Wtm-Cpt-Tk=Ar9vOU3NH5Aosq5kHKZImMd0NEsFp_ep7NxEKUVkHWH5Nry_k2f_fgmS9CGQcLQsCjfA93LmGHOi8g8vA12iFDXVJdNhDJbYO7C051yJ0i0fIwDqsf76QnwLC4m4KzSujxbHAkAiihafiXelkQT7noFoW-EWgVSIfC6FwPw1UI9PdQFwXoQ4C3lbWFTC7G5Ygy0PYFGq34As9rAWCh49MwE8RfU171NG_BWhmrboOY2YfjXruePaYyCYpovGPfh7MWZ3scnUk7roEvNpLGJ-ioyGky_reMrNDb-vb_MIxj29QG_UnF5-b5A6yo1nTfsuYXzl-1EwVtf-2aAAl394sXlZbtgSRrsJAkcdvbI2RCdma8eXnAD4; SHP_BUCKET_ID=5; BUC=YDWu8BQtakmT81sEuaWSIyHtZ6GMd5QlXkYMTOwYa7U=",
    "priority": "u=0, i",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-form-factors": '"Desktop"',
    "sec-ch-ua-full-version-list": 'Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"10.0.0"',
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
response = requests.get(url)
#418 : 요청을 수행할 수 없을때 의 에러 코드

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"

