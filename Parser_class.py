from bs4 import BeautifulSoup
import urllib.request

class Parser:
    raw_html = '' # сырой html
    html = '' # красивый обработанный html
    results = [] # результаты выборки

    def __init__(self, url, path):
        self.url = url # адрес, которй парсим
        self.path = path # путь, куда заисываем

    # парсинг
    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')

        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)  # find() ищет только один элемент
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            # добавляем данные в словарь
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href
            })

    # получение html
    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')  # парсим html-страницу

    # запишем данные в файл
    def save(self):
         with open(self.path, 'w', encoding='utf-8') as f:
             i = 1  # счетчик, номер новости
             for item in self.results:
                 f.write(
                     f"Новость № {i}\n\nНазвание: {item['title']}\nОписание: {item['desc']}\nСсылка: {item['href']}\n\n **********\n\n")
                 i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()