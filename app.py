from idr_rate_scraper import getRates

url = 'http://www.floatrates.com/daily/idr.json'
idrRates = getRates(url)
for value in idrRates.json().values():
  print(value['code'])
  print(value['name'])
  print(value['date'])
  print(value['inverseRate'])
