import eightqueen_func as eq

classtaple = ('none', 'left', 'white', 'gray')

def cross_x(qlist, width):
  clist = [None for y in range(width)]
  for x in qlist:
    clist[x[0]] =  x
  return clist  

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


def first_line():
  return '<table>'

def table_first_line(width):
  print '<tr>\n  <td class="none"></td>'
  for x in range(width):
    print '  <td class="none">{}</td>'.format(x)
  print '</tr>'

def lines_out(queens_list,width):
  wglist = classtaple[2:]
  new_queen_list = cross_x(queens_list, width)
  for x in range(width):
    begin_color = x%2
    print '<tr>\n <td class="left">{}</td>'.format(x)
    for y in queens_list:
      if y[1] = 


      print '  <td class="{}"></td>'.format(wglist[begin_color])
      begin_color = (begin_color + 1) % 2
    print '</tr>'
