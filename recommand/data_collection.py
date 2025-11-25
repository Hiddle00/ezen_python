import requests
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json&key=??"
response = requests.get(url)

data = response.json()
print(data)

total_count = data["TotalCount"]
print(total_count)
print(data["Data"][0]["Result"][0]["DOCID"])