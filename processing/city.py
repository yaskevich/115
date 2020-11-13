import json
import pandas
import requests
from scrapy.selector import Selector

# http://piratepad.net/4b5nVMPFZv

# {"items":{"67571":{"id":"67571","href":"\/problem\/67571","address":"проспект Независимости 117аМинск","lng":"27.63898277","lat":"53.93099594","category":{"id":"295","parent_id":"20","icon":"20"},"user":{"id":"38339","name":"Наталья ","last_name":"Блыщик ","middle_name":"Юрьевна "},"date_create":"30 марта 10:47","date_planned":"27.04.2017","crm_date_planned":"2017-04-27","crm_create_at":"2017-03-30","status":"4","rating":"0","photo":{"before":["\/upload\/image\/207626.jpg"],"after":[]}}}}
# http://115.xn--90ais/api/problem/getMapData/67571

ds = pandas.read_csv('opendata-115-2017-03-01.csv', skiprows=range(0, 2), sep=',',)
[n, m] =  [3, 15]
root = "http://115.xn--90ais/"

headers0 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3024.0 Safari/537.36',
}

def get_problem(sess, token, id):
    mapstr = root + 'api/problem/getMapData/' + str(id)
    # ref = root + 'problem/' + str(id)
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3024.0 Safari/537.36',
    #     'Referer': ref,
    #     'X-Requested-With': 'XMLHttpRequest',
    # }
    payload = {'_token': token}
    # cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(sess.cookies))
    # r = sess.post(mapstr, headers=headers, data=payload, cookies=cookies)
    # print(sess.headers)
    r = sess.post(mapstr, data=payload)

    if r.status_code == 200:
        body = r.content
        return body
    else:
        print(r.status_code)
    return

req_sess = requests.Session()
req_sess.headers.update(headers0)
r = req_sess.get(root)
if r.status_code == 200:
    body = r.content
    tkn = Selector(text=body).css('.b-modal > input[name=_token]::attr(value)').extract()[0]
    res = get_problem(req_sess, tkn, 67571)
    jsd = json.loads(res)
    print(jsd)
exit()

for index, row in ds.iterrows():
    # print(row['category'])
    # exit()
    if index >= n:
        print(row['id'])
    if index == m:
        break
        exit()