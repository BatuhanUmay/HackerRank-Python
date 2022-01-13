# .handle_comment(data)
# This method is called when a comment is encountered (e.g. <!--comment-->).
# The data argument is the content inside the comment tag:

# from HTMLParser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#           print "Comment  :", data


# .handle_data(data)
# This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
# The data argument is the text content of HTML.

# from HTMLParser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_data(self, data):
#         print "Data     :", data

#############################################################

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        satir_sayisi = len(data.split("\n"))

        if satir_sayisi > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
            
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = MyHTMLParser()

# html_string = ""

# for _ in range(int(input())):
#     html_string += input().rstrip() + "\n"

# parser.feed(html_string) 
    
sonuc = "\n".join(input() for _ in range(int(input())))
parser.feed(sonuc)

parser.close()