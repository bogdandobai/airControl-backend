import time
from datetime import datetime
from lxml import html
import requests


class Crawler:

    def scraping(self):
        response = requests.get('http://127.0.0.1:8000/cities')
        cities = response.json()

        while True:
            for city in cities:
                calculated_index = 0
                page = requests.get(city["url"])
                tree = html.fromstring(page.content)
                rows = tree.xpath(".//div[@id='citydivmain']//table[3]//tr")
                measurements = []
                measure = {"city": city["id"], "date": str(datetime.now())}
                for row in rows:
                    index = row.xpath(".//td[1]/div/div/span/text()")
                    if index:
                        index = str(index[0]).replace(" ", "")
                        index = index.replace(".", "")
                        if index.find("PM10") != -1 or index.find("PM25") != -1 or index.find(
                                "NO2") != -1 or index.find("O3") != -1 or index.find("SO2") != -1:
                            current = row.xpath(".//td[2]/text()")[0]
                            if current != "-":
                                current = int(current)
                                if calculated_index < current:
                                    calculated_index = current
                            else:
                                current = 0
                            measure[index] = current
                measurements.append(measure)
                print(measure)
                    #response = requests.post('http://127.0.0.1:8000/measurements', data=None, json={measure})
                url = 'http://127.0.0.1:8000/measurements?city='+city["name"]
                response = requests.post(url, data=measure)
                index = int(calculated_index)
                requests.patch("http://127.0.0.1:8000/cities/"+str(city["id"]), json={"index":index})
            time.sleep(7200)
crawler = Crawler()
crawler.scraping()
