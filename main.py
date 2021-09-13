import requests
from urllib.parse import urlencode, unquote

def Request_API_1():
    API_KEY = unquote("AU%2B3Jd9M%2F4EFoqDe43gUAyFC9QwBPwKS0grAx3kbZCqeAlO9yeNzqYh0OZT0gKYtAwVeJVkihmP8MyopkaQPfg%3D%3D")
    paramdata = {"authApiKey": API_KEY}
    resp = requests.get('http://openapi.jejuits.go.kr/rfcapi/rest/jejuits/getTrafficInfo', params=paramdata)
    print(resp.text)



if __name__ == '__main__':
    Request_API_1()


