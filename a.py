import base64
import re
import requests
import v2config
from urllib.parse import quote as url_encode

NODES = {}
updated_at = {}
COUNTRIES_u = {}
Session = requests.session()

def init():
    global NODES,COUNTRIES_u
    for i in v2config.REPOS: NODES[i] = ["",{}]     #time,nodes

    COUNTRIES_u = {}
    for i in v2config.COUNTRIES:COUNTRIES_u[i] = url_encode(i) 
def base64_remove_symbols(data):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', data)
    
    return cleaned
def save():
    for cnt in v2config.COUNTRIES:
        with open(f"\\node\\{base64_remove_symbols(base64.b64encode(cnt.encode("utf-8")).decode("utf-8"))}.txt","w",encoding="utf-8") as f:
            for i in v2config.REPOS:
                f.write("\r\n".join(NODES[i][1][cnt]) + "\r\n")  # 将列表转换为字符串，分隔符为
def updateNodes(repo_name,updated_at):
    global NODES
    resp = Session.get(f"https://api.github.com/repos/{repo_name}/readme",headers=v2config.HEADERS)
    d = resp.json()["content"]
    d = base64.b64decode(d).decode('utf-8')  # 添加base64解码
    d = re.findall(v2config.REX_LINK, d)[0]
    d = Session.get(d,proxies={
        "http":"http://127.0.0.1:10809",
        "https":"http://127.0.0.1:10809"
    })
    if d.status_code != 200:return
    d = base64.b64decode(d.text).decode('utf-8')  # 添加base64解码
    l = d.replace("\r\n","\n").splitlines()
    def _pop(j):
        l.remove(j)
        return j
    for cnt in v2config.COUNTRIES:
        NODES[repo_name][1][cnt] = [_pop(j) for j in l if COUNTRIES_u[cnt] in j]
    NODES[repo_name][0] = updated_at
def getRepoTime():
    global updated_at
    response = Session.get(v2config.SEARCH_URL, headers=v2config.HEADERS)
    results = response.json()["items"]
    for item in results:
        repo_name = item["full_name"]
        if repo_name in v2config.REPOS:
            updated_at[item["updated_at"]] = repo_name
    sorted_times = sorted(updated_at.keys(), reverse=True)
    for time_key in sorted_times:
        print(f"最新仓库：{updated_at[time_key]} 更新时间：{time_key}")
        updateNodes(updated_at[time_key], time_key)
    
init()
getRepoTime()
save()
