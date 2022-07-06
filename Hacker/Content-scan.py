import requests
url = "http://111.200.241.244:52109/"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

def file(file1):
    f = open(file1,encoding='utf-8').readlines()
    return f

def run():

    run = file("dictionary.txt")
    for i in run:
        cf = i.strip("\n")
        URL = url + str(cf)

        response = requests.get(URL,headers=headers)
 
        if response.status_code == 200:
            print("[+]" + str(cf) + "存在", len(response.text))
    return ""

run()