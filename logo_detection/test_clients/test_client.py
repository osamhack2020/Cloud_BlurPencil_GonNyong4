import requests

resp = requests.post('https://osam2020-4gb-uokiv.run.goorm.io/predict',
                     files={"file": open('twice.jpg', 'rb')})
print(resp.text)
