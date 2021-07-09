from html import unescape
input_str=input('输入要转换的数字或字符引用(格式:&#x)并以;分割 ')
arr=input_str.split(';')
for c in arr:
    print(c + ' --> ' + unescape(c))