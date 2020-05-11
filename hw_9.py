from Parser_class import Parser

parser = Parser('https://www.ua-football.com/sport', 'news.txt')
parser.run()
# print(parser.raw_html) # сырой html
# print(parser.html) # красивый html
# print(parser.results)