#!python

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value

#삭제
os.remove('data/'+pageId)

#redirection 리다이렉션
#입력이 끝나면 첫 페이지로 돌려버림.
print("Location: index.py")
print()