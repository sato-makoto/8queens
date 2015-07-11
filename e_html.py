#!/usr/bin/env python
import eightqueen_func as eq
import html_rend as html

x, y, pairs, myset = eq.allclear()
mylist = eq.get_queens_pattern()

head = html.html_header()
for x in head:
  print x[:-1]

print html.h1_out(eq.width)
print html.first_line()
html.table_first_line(eq.width)

html.lines_out(mylist, eq.width)

foot = html.html_footer()
for x in foot:
  print x[:-1]

