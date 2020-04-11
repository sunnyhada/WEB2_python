#!python
print("content-type: text/html; charset=utf-8\n")
print()

##반복문을 이용해 글 목록 구현
##os.listdir(path) : list를 return 함.

import cgi, os

files = os.listdir('data')
print(files)
listStr = ''
for item in files :
    listStr = listStr + item
print(listStr)

form = cgi.FieldStorage()
if 'id' in form :
    pageId = for["id"].value
    description = open('data/'+pageId, 'r').read()
else :
    pageId = 'Welcome'
    description = 'Hello, web'

print('''<!doctype htmll>
<html>
<head>
    <title>WEB1 - Welcom</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="python_docx.py">WEB</a></h1>
    <ol>
        <li><a href="python_docx.py?id=HTML">HTML</a></li>
        <li><a href="python_docx.py?id=CSS">CSS</a></li>
        <li><a href="python_docx.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
</body>'''.format(title=pageId))