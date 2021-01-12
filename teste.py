from py2html.main import *

page = web()
page.create(title='Static Site', bg='black')

page.header(text='LOREM IPSUM')
page.header(text='CONTENT:', n='2')
page.label(text='Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus iusto quibusdam labore quasi sint ut, nam eum, impedit temporibus rerum ratione necessitatibus magni qui aliquid. Laborum cum quas est numquam.')

page.compile()