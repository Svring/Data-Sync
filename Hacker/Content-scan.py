import requests
#什么都扫描不出来的扫描器
url = "http://97f48ca0-90ac-452f-830b-71c5bd25d500.node4.buuoj.cn:81/example"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

def file(file1):
    f = open(file1,encoding='utf-8').readlines()
    return f

def run():

    run = file("extra\\dictionary.txt")

    for i in run:
        cf = i.strip("\n")
        URL = url + str(cf)

        response = requests.get(URL,headers=headers)
 
        if response.status_code == 200:
            print("[+]" + str(cf) + "存在")

            print("[+]" + str(cf) + "存在",file=f)
    return ""

with open("extra\\result.txt",'w') as f:
    f.write(run())
    f.close()