import re
REPOS = [
    "mksshare/mksshare.github.io",
    "abshare3/abshare3.github.io",
    "toshare5/toshare5.github.io",
    "mkshare3/mkshare3.github.io",
    "abshare/abshare.github.io",
]

SEARCH_URL = "https://api.github.com/search/repositories?q=每日分享免费节点 免费机场 in:description github.io in:name&type=repositories&s=updated&o=desc"
SEARCH_URL_2 = "https://api.github.com/search/repositories?q=collect free site from abshare mksshare tolinkshare2 mkshare3 toshare5 abshare3 in:description Free_Site in:name&type=repositories&s=updated&o=desc"
REX_LINK = re.compile("订阅链接\r\n\r\n```\r\n(https://.*?)\r")
HEADERS = {
  'authority': 'github.com',
  'accept': 'application/json',
  'accept-language': 'zh-CN,zh;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
}


COUNTRIES= [
    "台湾",
    "香港",
    "日本",
    "新加坡",
    "韩国",
    "菲律宾",
    "美国",
    "马来西亚",
    "西班牙",
    "泰国",
    "印度",
    "澳大利亚",
    "加拿大",
    "德国",
    "俄罗斯",
    "土耳其",
    "乌克兰",
    "越南",
    "巴西"
]
