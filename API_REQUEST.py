import requests
from urllib.parse import urlencode, unquote
from xml.etree import ElementTree


# xml 리턴
def api_request():
    tree = ElementTree.parse('getTrafficInfo.xml')
    return tree


# 이하의 코드는 API에 접근 가능하던 때 온라인으로 xml을 다운받고 해석하는 코드였습니다
#def api_request():
#    apikey = unquote("AU%2B3Jd9M%2F4EFoqDe43gUAyFC9QwBPwKS0grAx3kbZCqeAlO9yeNzqYh0OZT0gKYtAwVeJVkihmP8MyopkaQPfg%3D%3D")
#    paramdata = {"authApiKey": apikey}
#    resp = requests.get('http://openapi.jejuits.go.kr/rfcapi/rest/jejuits/getTrafficInfo', params=paramdata)
#    tree = ElementTree.fromstring(resp.content)
#    return tree