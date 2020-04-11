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


form = cgi.FieldStorage()

## data 폴더에 있는 값 읽어오기, 단 id가 form에 없을 경우 그냥 welcome출력
if 'id' in form :
    pageId = form["id"].value
    ## 파일 내용 불러오기
    description = open('data/'+pageId, 'r').read()
else :
    pageId = 'Welcome'
    description = 'Hello, web'

##글작성하는 탭 만들기
## input type = "타입명"
    ## text, submit 등
## 여러줄 입력
## testarea rows="정수"
## name="서버로 전송될 때 이름"
## place holder ="아무것도 입력 되지 않았을때 디폴트값"

## form 태그
## <form action="파일을 보낼 위치">

## 글을 쓸 때 쿼리 스트링을 리턴해버리면 웹사이트 정보를
## 서버에 사용자가 입력하거나 수정하는 경우가 있을수도 있음.

## 이때 form 태그에 method="post"를 삽입하면 url이 바뀌지 않음.
## 전달은 제대로 됨.


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
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name = "description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList()))