#!python
print("content-type: text/html; charset=utf-8\n")
print()
##URL query string 사용하기

##python에 html과 똑같이 표현할 수 있음.
##index.py?id= : Query String.
##뒤에 올 것을 입력받으려면? cgi를 이용하면 됨.

import cgi, os, view

#'data'폴더에 있는 디렉토리 리스트를 불러오기
# 파일을 추가함으로써 컨텐츠를 보여줄 수 있음.
files = os.listdir('data')
listStr=''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()

## data 폴더에 있는 값 읽어오기, 단 id가 form에 없을 경우 그냥 welcome출력
if 'id' in form :
    pageId = form["id"].value
    ## 파일 내용 불러오기
    description = open('data/'+pageId, 'r').read()
else :
    pageId = 'Welcome'
    description = 'Hello, web'

## 칸에 값이 채워져 있길 바라는 경우 value를 이용해주면 된다.

## 주소값 변경을 방지하기 위해 pageId를 별도로 받음
## input type = 'hidden'
## <input type="hidden" name="pageId" value="{form_default_title}">


print('''<!doctype htmll>
<html>
<head>
    <title>WEB1 - Welcom</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
    {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId"  placeholder="title" value="{form_default_title}"></p>
        <p><input type="text" name="title"  placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name = "description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList, form_default_title=pageId, form_default_description=description))