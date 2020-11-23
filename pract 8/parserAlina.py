from bs4 import BeautifulSoup as bs
import codecs

# открываем документ
doc = bs(codecs.open('pand.html', encoding='utf-8', mode='r').read(), 'html.parser')


i=0
title = doc.select('.article_article-page h1')[0].decode_contents().strip()
date = doc.select('.date')[0].decode_contents().strip()
other = doc.select('.crosslinks__item a')[0].decode_contents().strip()
news = doc.select('.link_color')[0].decode_contents().strip()


# вывод на экран
print('\nЗаголовок статьи:', title)
print('\nДата:', date)
print('\nРанее на эту тему:', other)
print('\nСамое новое в ленте новостей:', news)
