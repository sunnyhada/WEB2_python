#!python

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value

#open을 이용하면 'w'의 태그를 이용해서 write 해줌.
#close해주기
opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#redirection 리다이렉션
#입력이 끝나면 첫 페이지로 돌려버림.
print("Location: index.py?id="+title)
print()