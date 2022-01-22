from html.parser import HTMLParser
class HTMLParserClass(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
htmlCode = '\n'.join([input() for _ in range(int(input()))])
parser = HTMLParserClass()
parser.feed(htmlCode)
parser.close()