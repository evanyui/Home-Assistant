import urllib.request, json, pprint

clear = '是晴天'
clouds = '多雲'
haze = '要小心煙霾'
mist = '會起霧'
rain = '記得帶雨傘，可能會下雨'
snow = '有機會下雪'
default = '多數為晴天'

URL = "http://api.openweathermap.org/data/2.5/weather?zip=30318,us&units=metric&appid=d54cd01e8005bc84825fce37ff2d073a"
req = urllib.request.Request(URL)

def ask_weather():
    try:
        res = urllib.request.urlopen(req).read()
        data = json.loads(res)

        temp = str(int(data['main']['temp']))
        w = '目前的溫度是 %s 度. ' % temp  
        
        temp_max = str(int(data['main']['temp_max']))
        temp_min = str(int(data['main']['temp_min']))
        w += "今天最高溫為 %s 度, 最低溫為 %s 度. " % (temp_max, temp_min)

        weather = str(data['weather'][0]['main'])
        if weather == 'Clear':
            status = clear
        elif weather == 'Clouds':
            status = clouds
        elif weather == 'Haze':
            status = haze
        elif weather == 'Rain':
            status = rain
        elif weather == 'Snow':
            status = snow
        elif weather == 'Mist':
            status = mist 
        else:
            status = default
        w += "今天 %s." % status
    except:
        w = "對不起，氣象預報功能有點問題." 

    return w

