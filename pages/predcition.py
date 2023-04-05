import requests as rq
import xml.etree.ElementTree


data = rq.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')

print(data)