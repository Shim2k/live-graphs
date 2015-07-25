import urllib
import json
import time

i = 0

while(1):
    params = urllib.urlencode({'txtUserName': 'webmaster', 'txtPassword': '2020'})
    response = urllib.urlopen("http://2.55.72.142/htm_login.htm", params)
    html = response.read()

    res = urllib.urlopen("http://2.55.72.142/app_dd_SysSum.txt")
    hey = res.read()
    data = hey.split(';')
    arr = []

    i += 1

    for meas in data:
        if meas.split('=')[0] and meas.split('=')[1]:
            x = { 'key' : meas.split('=')[0], 'value' : meas.split('=')[1] }
            arr.append(x)

    with open('data' + str(i) +'.json', 'wb') as data:
        data.write(json.dumps(arr))
    time.sleep(5)
