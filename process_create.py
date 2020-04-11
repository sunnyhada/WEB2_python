#!python

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

#open을 이용하면 'w'의 태그를 이용해서 write 해줌.
opened_file = open('data/'+title, 'w')
opened_file.write(description)

#redirection 리다이렉션
#입력이 끝나면 첫 페이지로 돌려버림.
print("Location: index.py?id="+title)
print()