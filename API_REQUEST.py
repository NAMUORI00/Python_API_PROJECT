import requests
from urllib.parse import urlencode, unquote
from xml.etree import ElementTree


# xml 리턴
def api_request():
    apikey = unquote("AU%2B3Jd9M%2F4EFoqDe43gUAyFC9QwBPwKS0grAx3kbZCqeAlO9yeNzqYh0OZT0gKYtAwVeJVkihmP8MyopkaQPfg%3D%3D")
    paramdata = {"authApiKey": apikey}
    resp = requests.get('http://openapi.jejuits.go.kr/rfcapi/rest/jejuits/getTrafficInfo', params=paramdata)
    tree = ElementTree.fromstring(resp.content)
    print(resp.content)
    return tree