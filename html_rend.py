# -*- coding: utf-8 -*-
from time import localtime
import eightqueen_func as eq

classtaple = ('none', 'left', 'white', 'gray')
y, mo , d, h, m, s, n, n, n  =  localtime()    
datestr = '{}年{}月{}日 {}時{}分{}秒'.format(y, mo, d, h, m, s)

def html_header():
 header_file = 'html_header'
 h = open(header_file)
 return h

def html_footer():
 footer_file = 'html_footer'
 f = open(footer_file)
 return f

def h1_out(width):
 return '<h1>{} Queens</h1>'.format(eq.width)

def p_out():
 return '<p> -- {}に作成しました</p>'.format(datestr)

def first_line():
  return '<table summary="Queens">'

def table_first_line(width):
  ret_str = '<tr>\n  <td class="none"></td>'
  for x in range(width):
    ret_str = ret_str + '  <td class="none">{}</td>'.format(x)
  ret_str = ret_str + '</tr>'
  return ret_str

def lines_out(queens_list,width):
  wglist = classtaple[2:]
  q = ''
  ret_str = ''
  for x in range(width):
    begin_color = x%2
    ret_str = ret_str + '<tr>\n <td class="left">{}</td>'.format(x)
    for y in queens_list:
      if y[0] == x and begin_color%2 == 0:
         q = '♕'
      elif y[0] == x and begin_color%2 == 1:
         q = '♛'
      else:
         q = ''
      ret_str = ret_str + '  <td class="{}">{}</td>'.format(wglist[begin_color], q)
      begin_color = (begin_color + 1) % 2
    ret_str = ret_str + '</tr>'
   
  return ret_str
