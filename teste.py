from py2html.main import *

site = web()
site.create(title='My Site')

site.label(text='Hello World')
site.href(link='https://www.google.com', text='google')
site.label(text='created with py2html')

site.compile()