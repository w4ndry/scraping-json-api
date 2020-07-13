from flask import Flask, render_template
from idr_rate_scraper import getRates

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/idr-rates')
def idr_rates():
  url = 'http://www.floatrates.com/daily/idr.json'
  data_json = getRates(url)

  return render_template('index.html', data=data_json)

if __name__ == "__main__":
  app.run(debug=True)
