from py2html.main import *

page = web()
page.create()

# Header Parameters
#   text = header text
#   n = title level
page.header(text='My Site', n=1)

# Label Parameters
#   text = label text
#   color = label color
page.label(text='', color='')

page.compile()