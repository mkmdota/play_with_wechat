import json
import requests

key = ''
while True:
    info = input('\n我：')
    url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    res = requests.get(url)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    print('\nTuling: '+jd['text'])
    print(jd)
