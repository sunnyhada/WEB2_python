#!python
print("content-type: text/html; charset=utf-8\n")
print()
##URL query string 사용하기

##python에 html과 똑같이 표현할 수 있음.
##index.py?id= : Query String.
##뒤에 올 것을 입력받으려면? cgi를 이용하면 됨.

#refactoring : 함수를 이용해서 간단하게 만들어 보기.


import cgi, os, view

#'data'폴더에 있는 디렉토리 리스트를 불러오기
# 파일을 추가함으로써 컨텐츠를 보여줄 수 있음.

form = cgi.FieldStorage()

## data 폴더에 있는 값 읽어오기, 단 id가 form에 없을 경우 그냥 welcome출력
if 'id' in form :
    pageId = form["id"].value
    ## 파일 내용 불러오기
    description = open('data/'+pageId, 'r').read()
    ## 보안을 위해 jsp같은 스크립트 코드가 작동되지 않도록 함.
    ## 관련 api, 패키지 ↓
        ## 검색어 : python html sanitizer
        ## PyPI 접속 (파이썬 홈페이지)
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')
    ## update_link
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else :
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action=''


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
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(title=pageId,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))