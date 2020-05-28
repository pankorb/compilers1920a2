import re



html_title = open('testpage.txt','r',encoding='utf-8').read()
# print(html_title)

rx = re.compile('<title>(.+?)</title>')

title = rx.search(html_title)

print(title.group(1))



rx = re.compile('<!--(.+?)-->', re.DOTALL)

result = rx.sub('<!-- -->', html_title) 





rx = re.compile('<script>(.+?)</script>', re.DOTALL)


result = rx.sub(' ', result) 
rx = re.compile('<style>(.+?)</style>',re.DOTALL)
result = rx.sub(' ', result)


print(result)



rx = re.compile('<a(.+?)</a>')


for temp in rx.finditer(result):
    print(temp.group(0)) 



rx = re.compile('<.+?>')
result = rx.sub(' ', result)




def funsub(result):
    if (result.group(0)=='&amp'):
        return '&'
    elif(result.group(0)=='&gt'):
        return '>'
    elif (result.group(0)=='&lt'):
       return '<'
    elif(result.group(0)=='&nbsp'):
        return ' '
rx = re.compile('&amp|&gt|&lt|&nbsp')
result = rx.sub(funsub, result)

def funsub2(result):
    return ' '
rx = re.compile('\s+')
result = rx.sub(funsub2, result)
print(result)












