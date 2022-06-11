import re
c1 = 'hello world'
strinfo = re.compile('world')
d1 = strinfo.sub('python', c1)
print('1原始字符串:{}'.format(c1))
print('1替换字符串:{}'.format(d1))