from bs4 import BeautifulSoup as bs
import codecs

# открываем документ
doc = bs(codecs.open('pand.html', encoding='utf-8', mode='r').read(), 'html.parser')
selectors = {
    'title': '.article_article-page h1',
    'date': '.date',
    'other': '.crosslinks__item a',
    'news': '.link_color'}

def get(doc, param):
    return doc.select(param)[0].decode_contents().strip()    
    
title = get(doc, selectors['title'])
date = get(doc, selectors['date'])
other = get(doc, selectors['other'])
news = get(doc, selectors['news'])

# вывод на экран
print('\nЗаголовок статьи:', title)
print('\nДата:', date)
print('\nРанее на эту тему:', other)
print('\nСамое новое в ленте новостей:', news)
