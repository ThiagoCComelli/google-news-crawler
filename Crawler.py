from bs4 import BeautifulSoup
import requests
from Database import Database

class Crawler:
    headers = {
        'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    def __init__(self):
        pass

    def start():
        database = Database("localhost","root","root","gerenciador_de_caixa")
        database.createConnection()
        databaseConnection = database.getConnection()

        request = requests.get("https://www.google.com/search?q=economia&tbm=nws&sxsrf=AOaemvLjm-eGdpmuCaqCIrmCMMuZh6MkrQ:1635102165354&source=lnms&sa=X&ved=2ahUKEwi7nvKd3uPzAhXNqZUCHcT5BZQQ_AUoAnoECAEQBA&biw=1280&bih=653&dpr=1", headers=Crawler.headers)
        soup = BeautifulSoup(request.text, 'lxml')

        for result in soup.select('a[class=WlydOe]'):
            content = result.find('div', attrs={'class': 'iRPxbe'})
            obj = {}

            try:
                obj["website"] = content.find_all('div')[0].text
                obj["title"] = content.find_all('div')[1].text
                obj["description"] = content.find_all('div')[2].text
                obj["href"] = result["href"]

                add_news = f'INSERT INTO news VALUES ("{obj["title"]}", "{obj["href"]}", "{obj["description"]}", DEFAULT, DEFAULT);'
                databaseConnection["cursor"].execute(add_news)
            except:
                continue
        
        databaseConnection["connection"].commit()
        database.closeConnection()



