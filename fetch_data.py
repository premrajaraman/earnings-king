import requests, json
def get_data():
    url = "https://www.nseindia.com/api/event-calendar"
    headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en;q=0.9"}
    with requests.Session() as s:
        s.get("https://www.nseindia.com", headers=headers)
        res = s.get(url, headers=headers)
        if res.status_code == 200:
            data = [{"date": i['date'], "symbol": i['symbol'], "company": i['company']} 
                    for i in res.json() if "Financial Results" in i.get('purpose', '')]
            with open('results_data.json', 'w') as f: json.dump(data, f)
get_data()
