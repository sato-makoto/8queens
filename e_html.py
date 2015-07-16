#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eightqueen_func as eq
import html_rend as html

x, y, pairs, myset = eq.allclear()
mylist = eq.main(eq.width)

head = html.html_header()
for x in head:
  print x[:-1]

print html.h1_out(eq.width)
print html.p_out()
print html.first_line()
print html.table_first_line(eq.width)

table_line = html.lines_out(mylist, eq.width)

print table_line

foot = html.html_footer()
for x in foot:
  print x[:-1]

