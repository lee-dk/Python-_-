from selenium import webdriver
import pandas as pd

'''
127.014   37.596326
126.979   37.568157
126.993   37.572195
126.949   37.587077
127.077   37.458150
126.994   37.569238
127.003   37.573050
'''
x = ['127.014', '126.979', '126.993', '126.949', '127.077', '126.994', '127.003']
y = ['37.596326', '37.568157', '37.572195', '37.587077', '37.458150', '37.569238', '37.573050']

driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
driver.implicitly_wait(3)
url_startX = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoByBusNSub?ServiceKey=MT9k5VcAGch1xQwYHcvv1ej9TCzetVpOFC3ikeBe44U2S11WVLlIgwMvCEbKvoX1zqCgJ58UcWwtiLENWlnzdA%3D%3D&startX='
url_startY = '&startY='
url_endX = '&endX='
url_endY = '&endY='
df = pd.DataFrame(columns=['start_place', 'end_place', 'travelTime'])
for n in range(0,6) :
    url = url_startX + x[n] + url_startY + y[n] + url_endX + x[n+1] + url_endY + y[n+1]
    driver.get(url)
    driver.implicitly_wait(5)
    start_place = driver.find_element_by_css_selector('#folder4 > div.opened > div:nth-child(2) > span:nth-child(2)').text

    end_place = driver.find_element_by_css_selector("#folder4 > div.opened > div:nth-child(8) > span:nth-child(2)").text

    travelTime = driver.find_element_by_css_selector('#folder3 > div.opened > div:nth-child(3) > span').text
    # folder3 > div.opened > div:nth-child(4) > span:nth-child(2)
    driver.implicitly_wait(8)

    print("출발 : ", start_place)
    print("도착 : ", end_place)
    print("이동시간 : ", travelTime)

    driver.implicitly_wait(5)
#driver.quit()
'''
with open('C:/Temp/TravelTime.csv', "wt", encoding="utf-8") as f:
    f.write('start_place,end_place,travelTime\n')
    for i in range(len(start_place)):
        f.write('"' + start_place[i] + '",' + end_place[i] + '",' + travelTime[i] + '\n')
'''