import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

non_decimal = re.compile(r'[^\d.]+')

def scrape_data(url):
    # Call website and retrieve html
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # sepperate and store data
    try:
        pie = soup.find_all('div', class_="_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q")
        temp = non_decimal.sub('', soup.find('span', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY').text)
#         print(temp)
        hl = soup.find('div', class_="_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q").find_all('span')
        high = hl[0].text
#         print(high)
        low =hl[1].text
#         print(low)
        feel = non_decimal.sub('', soup.find('span', class_="_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt").text)
#         print(feel)
        humid = non_decimal.sub('', pie[2].text)
#         print(humid)
        pressure = non_decimal.sub('', pie[4].text)
#         print(pressure)
    except:
        print(f'unable to scrape from {url}')
        return('empty')
        
    data = [temp, high, low, feel, humid, pressure]
    return(data)  

def collect_data(cities):
    x = len(cities)
    loopNum = 1
    while x >0:
        x = len(cities)
        print(f'Try # {loopNum}')
        for city in cities:
            name = city['name']
            url = city['url']
            print(f'Trying to scrape info for {name}. url is : {url}')
            if ((city['data'][0] == None) or (city['data'][0] == 'empty')):
                city['data'] = []
                city['data'].append(scrape_data(url))
            else:
                x -= 1
        loopNum +=1

    print('Done')
    return

def makeNsave(cities):
    high = []
    low = []
    temp = []
    feel = []
    humid = []
    pressure = []
    name = []
    
    for city in cities:
        name.append(city['name'])
        high.append(city['data'][0][1])
        low.append(city['data'][0][2])
        temp.append(city['data'][0][0])
        feel.append(city['data'][0][3])
        humid.append(city['data'][0][4])
        pressure.append(city['data'][0][5])
    
    df_base = {
        'City' : name,
        'Temp' : temp,
        'Feel' : feel,
        'High' : high,
        'Low' : low,
        'Humidity' : humid,
        'Pressure' : pressure
    }
    
    df = pd.DataFrame(df_base)
    df.to_csv('scraped.csv', index=False)
    return
    
def go():
    print('Starting')
    non_decimal = re.compile(r'[^\d.]+')
    cities = [
        {'name' : 'Chicago', 'url' : 'https://weather.com/weather/today/l/e0abde3003a88dedecad92fedc96375000c16843287a51dbf2cd92f062217180', 'data' : [None]},
        {'name' : 'Nashville', 'url' :'https://weather.com/weather/today/l/c497a8fe783a21075e4be0fe8e3851415b88cb2e30a6fa184550e22a7ae728c6' , 'data' : [None]},
        {'name' : 'Denver', 'url' : 'https://weather.com/weather/today/l/675c2b6342b3512ea4f15bc9070663be6e36cc4bf61056076c500098c8eb3bbe', 'data' : [None]},
        {'name' : 'Seattle', 'url' : 'https://weather.com/weather/today/l/ced0de18c1d771856e6012f3abf0a952cfe22952e72e516e6e098d54ca737114', 'data' : [None]},
        {'name' : 'Honolulu', 'url' : 'https://weather.com/weather/today/l/263f49e812cfbd2c5812f4c3f3dec5eb89d625bb80fab3d024ed4d3a10220f32', 'data' : [None]},
        {'name' : 'Miami', 'url' : 'https://weather.com/weather/today/l/3881cd527264bc7c99b6b541473c0085e75aa026b6bd99658c56ad9bb55bd96e', 'data' : [None]},
        {'name' : 'Omaha', 'url' : 'https://weather.com/weather/today/l/249cf41186d4f776ce51abe6b22bbf8aa2c285e24387cbab91e6aaa518bfbc3c', 'data' : [None]},
        {'name' : 'Houston', 'url' : 'https://weather.com/weather/today/l/110a124808308e4fc03ee2b75754a7e06e9334b6d23d6fa317f1bb84b5f8a65e', 'data' : [None]},
        {'name' : 'Pheonix', 'url' : 'https://weather.com/weather/today/l/729d869b5da7e1b89835d0de7940cda8b0b2e0dafda4ef6f742b558409755f66', 'data' : [None]},
        {'name' : 'Albuquerque', 'url' : 'https://weather.com/weather/today/l/cdad20b8f7657de1012528aeda289407445c7be167e14dd56a66b0cd3716ff03', 'data' : [None]}
    ]
    print('Collecting data')
    print('--------------------------------')
    collect_data(cities)
    print('Saving data')
    print('--------------------------------')
    makeNsave(cities)
    print('Done')
    print('A csv has been made in whatever folder you ran this from')
    return
