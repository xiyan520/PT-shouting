import requests
import datetime

# 各站点开关启用：True 禁用：False
enable_daqingchong = True
enable_tosky = True
enable_qingwa = True

#是否启用青蛙求下载
enable_qingwa_download = False 

# IYUU 令牌
iyuu_key = ""  # 填入你的 IYUU 令牌

# Cookies 定义
cookies_daqingchong = {
    'c_secure_uid': '',
    'c_secure_pass': '',
    'c_secure_ssl': '',
    'c_secure_tracker_ssl': '',
    'c_secure_login': ''
}

cookies_tosky = {
    'c_secure_uid': '',
    'c_secure_pass': '',
    'c_secure_ssl': '',
    'c_secure_tracker_ssl': '',
    'c_secure_login': ''
}

cookies_qingwa = {
    'c_secure_uid': '',
    'c_secure_pass': '',
    'c_secure_ssl': '',
    'c_secure_tracker_ssl': '',
    'c_secure_login': ''
}

# 请求参数
params_1 = {
    'shbox_text': '青虫娘，求上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_2 = {
    'shbox_text': '青虫娘，求魔力',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_5 = {
    'shbox_text': '青虫娘，求彩虹id',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_6 = {
    'shbox_text': '青虫娘，求vip',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_3 = {
    'shbox_text': '来点上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_4 = {
    'shbox_text': '来点魔力',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_7 = {
    'shbox_text': '蛙总，求上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_8 = {
    'shbox_text': '蛙总，求下载',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

# 请求头
headers_daqingchong = {
    'Host': 'cyanbug.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://cyanbug.net/index.php'
}

headers_tosky = {
    'Host': 't.tosky.club',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://t.tosky.club/index.php'
}

headers_qingwa = {
    'Host': 'www.qingwapt.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.qingwapt.com/index.php'
}

# 存储响应消息
messages = []

# 获取今天的日期
today = datetime.date.today()

# 发送请求（大青虫）
if enable_daqingchong:
    url_daqingchong = "https://cyanbug.net/shoutbox.php"
    try:
        response_1 = requests.get(url_daqingchong, headers=headers_daqingchong, cookies=cookies_daqingchong, params=params_1)
        messages.append("大青虫上传求成功" if response_1 and response_1.text.strip() else "大青虫上传求失败")
    except requests.exceptions.RequestException:
        messages.append("大青虫上传请求异常")

    try:
        response_2 = requests.get(url_daqingchong, headers=headers_daqingchong, cookies=cookies_daqingchong, params=params_2)
        messages.append("大青虫魔力求成功" if response_2 and response_2.text.strip() else "大青虫魔力求失败")
    except requests.exceptions.RequestException:
        messages.append("大青虫魔力请求异常")

    # 每月1号发送这两个请求
    if today.day == 1:
        try:
            response_5 = requests.get(url_daqingchong, headers=headers_daqingchong, cookies=cookies_daqingchong, params=params_5)
            messages.append("大青虫求彩虹ID成功" if response_5 and response_5.text.strip() else "大青虫求彩虹ID失败")
        except requests.exceptions.RequestException:
            messages.append("大青虫彩虹ID请求异常")

        try:
            response_6 = requests.get(url_daqingchong, headers=headers_daqingchong, cookies=cookies_daqingchong, params=params_6)
            messages.append("大青虫求VIP成功" if response_6 and response_6.text.strip() else "大青虫求VIP失败")
        except requests.exceptions.RequestException:
            messages.append("大青虫VIP请求异常")

# 发送请求（tosky）
if enable_tosky:
    url_tosky = "https://t.tosky.club/shoutbox.php"
    try:
        response_3 = requests.get(url_tosky, headers=headers_tosky, cookies=cookies_tosky, params=params_3)
        messages.append("tosky求上传成功" if response_3 and response_3.text.strip() else "tosky求上传失败")
    except requests.exceptions.RequestException:
        messages.append("tosky上传请求异常")

    try:
        response_4 = requests.get(url_tosky, headers=headers_tosky, cookies=cookies_tosky, params=params_4)
        messages.append("tosky求魔力成功" if response_4 and response_4.text.strip() else "tosky求魔力失败")
    except requests.exceptions.RequestException:
        messages.append("tosky魔力请求异常")

# 发送请求（青蛙）
if enable_qingwa:
    url_qingwa = "https://www.qingwapt.com/shoutbox.php"
    try:
        response_7 = requests.get(url_qingwa, headers=headers_qingwa, cookies=cookies_qingwa, params=params_7)
        messages.append("青蛙求上传成功" if response_7 and response_7.text.strip() else "青蛙求上传失败")
    except requests.exceptions.RequestException:
        messages.append("青蛙上传请求异常")

    # 判断是否启用下载请求
    if enable_qingwa_download:
        try:
            response_8 = requests.get(url_qingwa, headers=headers_qingwa, cookies=cookies_qingwa, params=params_8)
            messages.append("青蛙求下载成功" if response_8 and response_8.text.strip() else "青蛙求下载失败")
        except requests.exceptions.RequestException:
            messages.append("青蛙下载请求异常")

# 最终统一打印结果
for message in messages:
    print(message)
# 发送结果到 IYUU
url = f"https://iyuu.cn/{iyuu_key}.send"

# 定义文本和描述
text = "自动发送GET请求结果"
desp = "\n".join(messages)

# 定义请求参数
params = {
    'text': text,
    'desp': desp
}

# 发送GET请求到 IYUU
try:
    response_iyuu = requests.get(url, params=params)
    if response_iyuu.status_code == 200:
        response_data = response_iyuu.json()
        print("IYUU消息发送成功" if response_data["errcode"] == 0 else "IYUU消息发送失败")
    else:
        print("IYUU消息发送失败")
except requests.exceptions.RequestException:
    print("发送请求异常")
