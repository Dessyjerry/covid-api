import requests

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-25-2020.csv"

resp = requests.get(url)

print(resp.text)