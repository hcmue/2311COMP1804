import requests
from bs4 import BeautifulSoup

resp = requests.get("https://giavang.pnj.com.vn")

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, "html.parser")
    tbody = soup.find("tbody")

    result = []
    # print(tbody)
    trs = tbody.find_all("tr")
    # HCM
    td_hcm1 = trs[0].find_all("td")
    td_hcm2 = trs[1].find_all("td")
    print(td_hcm1)
    for item in td_hcm1:
        print(item.text)
    print(td_hcm2)
    for item in td_hcm2:
        print(item.text)
    
    result.append({
        "area": td_hcm1[0].text.strip(),
        "pnj": {
            "sell":  td_hcm1[2].text.strip(),
            "buy":  td_hcm1[3].text.strip(),
        },
        "sjc": {
            "sell":  td_hcm2[1].text.strip(),
            "buy":  td_hcm2[2].text.strip(),
        }
    })

    print(result)
