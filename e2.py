#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eightqueen_func as eq
import html_rend as html
from selenium import webdriver
from time import sleep
import large_list as l
import os

browser = webdriver.Firefox()
working_dir = os.getcwd() + '/'

x, y, pairs, myset = eq.allclear()
# mylist = eq.main(eq.width)
# mylist = [[2, 0], [4, 1], [1, 2], [7, 3], [5, 4], [3, 5], [6, 6], [0, 7]]
mylist = [[2, 0], [4, 1], [1, 2], [7, 3], 
[5, 4], [3, 5], [6, 6], [None, None]]

large_list = l.l_list()

output_html = 'hoge.html'

def html_output(mylist):
  f = open(output_html, 'w')
  head = html.html_header()
  for x in head:
    f.write(x[:-1])
  f.write(html.h1_out(eq.width))
  f.write(html.p_out())
  f.write(html.first_line())
  f.write(html.table_first_line(eq.width))
  table_line = html.lines_out(mylist, eq.width)
  f.write(table_line)
  foot = html.html_footer()
  for x in foot:
    f.write(x[:-1])
  f.close()

sleep(3)
for x in large_list:
  if x == [[]]:
    sleep(10)
  else:
    html_output(x)
    browser.get('file://' +  working_dir + output_html)
    sleep(2)

sleep(10)
browser.close()
