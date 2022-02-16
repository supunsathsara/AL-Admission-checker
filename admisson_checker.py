##from pathlib import Path
import requests

startI = int(input("Enter starting Index Number: "))
endI = int(input("Enter ending Index Number: "))

i = startI
while i < endI:
    header = {
        "authority": "admission.doenets.lk",
        "method": "POST",
        "path": "/api/admission",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "54",
        "content-type": "application/json",
        "origin": "https://admission.doenets.lk",
        "referer": "https://admission.doenets.lk/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }

    data = {"admission": 75, "type": "index", "identifier": i}

    url = "https://admission.doenets.lk/api/admission"
    response = requests.post(url, headers=header, json=data)
    res_json = response.json()

    ##print(res_json)

    if res_json != {
        "name": "Not Found",
        "message": "No candidate record found",
        "code": 0,
        "status": 404,
        "type": "yii\\web\\NotFoundHttpException",
    }:
        print("Index no:", i, "refference:", res_json["reference"])
         ##IF WANT TO DOWNLOAD THE PDF FILES UNCOMMENT BELOW LINES[NOT RECOMENNED THOUGH]
            
        ##pdf_url = "https://admission.doenets.lk/api/admission/" + res_json["reference"]
        ##filename = Path(str(i) + ".pdf")
        ##response = requests.get(pdf_url)
        ##filename.write_bytes(response.content)
    i += 1
