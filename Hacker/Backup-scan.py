import requests
url1 = "url"
dir1 = ['web','website','backup','back','www','wwwroot','temp']
final2 = ['tar','tar.gz','zip','rar','bak']

for i in dir1 :
    for j in final2 :
        filename = str(i) + '.' + str(j)
        url = str(url1) + '/' + filename

        print(filename + '  ',end='')

        print(len(requests.get(url).text))