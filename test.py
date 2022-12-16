import requests,sys,json,string,random

global ip_port1
global cishu
global sc
global scstr
##检查代理

cishu=1
while True:
    s = string.ascii_letters
    r1 = random.randint(0,9)
    r2 = random.randint(0,9)
    r3 = random.randint(0,9)
    r4 = random.randint(0,9)
    r5 = random.choice(s)
    r6 = random.choice(s)
    r7 = random.choice(s)
    r8 = random.choice(s)
    r1 = str(r1)
    r2 = str(r2)
    r3 = str(r3)
    r4 = str(r4)
    r = r1 + r2 +r3 +r4 + r5 + r6 +r7 +r8
    ip_port1 = "代理用户名:代理密码_country-国家_session-" + r + "@代理IP:代理端口"
    proxies = {
    'http': 'http://' + ip_port1,
    'https':'http://' +  ip_port1
    }
    #ip检测网址
    url="http://ip234.in/f.json"
    header={'User-Agent':'Mozilla/5.0'}
    if not ip_port1:
        print('ip_port不能为空')
        sys.exit(0)
    try:
        response=requests.get(url,headers=header,proxies=proxies,timeout=5)
        html = response.text
        data = json.loads(html) #拿到json
        data ['data']
        data2= data['data']
        sc = data2['score']
        url="http://ip234.in/ip.json"
        response=requests.get(url,headers=header,proxies=proxies,timeout=5)
        IPJSON = response.text
        data = json.loads(IPJSON) #拿到json
        ip = data ['ip']

        if(sc<20):
            print("代理威胁分数小于20，保留")
            print('代理IP:代理端口:代理用户名:代理密码_country-国家_session-' + r + " | ip为" + ip )
            file_path = 'good.txt'
            with open(file_path, mode='a', encoding='utf-8') as file_obj:
                file_obj.write('代理IP:代理端口:代理用户名:代理密码_country-国家_session-' + r +  "| ip = " + ip + "\n")
        if(sc>20):
            scstr = str(sc)
            print("代理威胁分数为"+ scstr + "丢弃")
        


        
    except :
        print("代理连接超时！")import requests,sys,json,string,random

global ip_port1
global cishu
global sc
global scstr
##检查代理

cishu=1
while True:
    s = string.ascii_letters
    r1 = random.randint(0,9)
    r2 = random.randint(0,9)
    r3 = random.randint(0,9)
    r4 = random.randint(0,9)
    r5 = random.choice(s)
    r6 = random.choice(s)
    r7 = random.choice(s)
    r8 = random.choice(s)
    r1 = str(r1)
    r2 = str(r2)
    r3 = str(r3)
    r4 = str(r4)
    r = r1 + r2 +r3 +r4 + r5 + r6 +r7 +r8
    ip_port1 = "代理用户名:代理密码_country-国家_session-" + r + "@代理IP:代理端口"
    proxies = {
    'http': 'http://' + ip_port1,
    'https':'http://' +  ip_port1
    }
    #ip检测网址
    url="http://ip234.in/f.json"
    header={'User-Agent':'Mozilla/5.0'}
    if not ip_port1:
        print('ip_port不能为空')
        sys.exit(0)
    try:
        response=requests.get(url,headers=header,proxies=proxies,timeout=5)
        html = response.text
        data = json.loads(html) #拿到json
        data ['data']
        data2= data['data']
        sc = data2['score']
        url="http://ip234.in/ip.json"
        response=requests.get(url,headers=header,proxies=proxies,timeout=5)
        IPJSON = response.text
        data = json.loads(IPJSON) #拿到json
        ip = data ['ip']

        if(sc<20):
            print("代理威胁分数小于20，保留")
            print('代理IP:代理端口:代理用户名:代理密码_country-国家_session-' + r + " | ip为" + ip )
            file_path = 'good.txt'
            with open(file_path, mode='a', encoding='utf-8') as file_obj:
                file_obj.write('代理IP:代理端口:代理用户名:代理密码_country-国家_session-' + r +  "| ip = " + ip + "\n")
        if(sc>20):
            scstr = str(sc)
            print("代理威胁分数为"+ scstr + "丢弃")
        


        
    except :
        print("代理连接超时！")