class web():
    def __init__(self):
        self.content = []
    
    def create(self, title='py2html site'):
        self.title = title
    
    #Layout Creator
    def html(self, code):
        self.content.append(code)
    def label(self, text):
        self.content.append('<p>'+text+'</p>')
    def href(self, text, link):
        self.content.append('<a href='+link+'>'+text+'</a>')

    def compile(self):
        html = open('page.html', 'w')
        html.write('<DOCTYPE html>\n')
        html.write('<html>\n')

        html.write('    <head>\n')
        html.write('        <title>'+self.title+'</title>\n')
        html.write('    </head>\n')

        html.write('    <body>\n')

        for c in self.content:
            html.write('        '+c+'\n')
        
        html.write('    </body>\n')

        html.write('</html>\n')
        html.close()