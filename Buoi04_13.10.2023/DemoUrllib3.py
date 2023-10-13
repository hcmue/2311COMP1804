# import urllib3
# resp = urllib3.request("GET", "https://sjc.com.vn/giavang/textContent.php")
# print(resp.status)
# print(resp.data)

import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4

# Gọi api
resp = requests.get("https://sjc.com.vn/giavang/textContent.php")
print(resp)

print('STATUS:', resp.status_code)
# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")

# Find Elements by ID
# results = soup.find(id="ResultsContainer")
# Find Elements by HTML Class Name
# job_elements = results.find_all("div", class_="card-content")
tr_elements = soup.find_all("tr")
for tr_item in tr_elements:
    # print(tr_elements)
    # Ứng mỗi tr tìm td
    td_elements = tr_item.find_all("td")
    if len(td_elements) == 3: # Đủ 3 cột
        print(tr_item.find('td', class_="ylo2_text"))
