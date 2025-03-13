import re
import base64
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

dddd= "5Y+w5rm+Lemmmea4ry3ml6XmnKwt5paw5Yqg5Z2hLemfqeWbvS3oj7Llvovlrr4t576O5Zu9LemprOadpeilv+S6mi3opb/nj63niZkt5rOw5Zu9LeWNsOW6pi3mvrPlpKfliKnkupot5Yqg5ou/5aSnLeW+t+WbvS3kv4TnvZfmlq8t5Zyf6ICz5YW2LeS5jOWFi+WFsC3otorljZct5be06KW/"
COUNTRIES= base64.b64decode(dddd).decode("utf-8").split("-")

