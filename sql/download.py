import datetime
import urllib
from urllib import request

BASE = "https://archive.sensor.community/"

def download(url):
    data = urllib.request.urlopen(url).read()
    return data

def save(data, filename):
    'Save data into the given filename.'
    with open(filename, 'wt') as f:
        f.write(data)

def days_between_today_and_past_date(year, month, day):
    past_date = datetime.date(year, month, day)
    today = datetime.date.today()
    days = (today - past_date).days
    return days

def download_days(number_of_days):
    'Download and save data for a given number of days.'
    one_day = datetime.timedelta(days=1)

    for i in range(1, number_of_days + 1): # no data for today
        current_date = datetime.date.today() - i * one_day
        base_url = f'{BASE}{current_date}/{current_date}'

        if str(current_date)[0:4] == "2021": break
        # if not str(current_date)[0:4] == str(datetime.date.today().year):
        #     base_url = f'{BASE}{datetime.date.today().year - 1}/{current_date}/{current_date}'

        for sensor in ['sds011_sensor_3659', 'sds011_sensor_36593']:
            url = f'{base_url}_{sensor}.csv'
            print('download', url)
            try:
                data = str(download(url), encoding='UTF-8')
            except Exception as e:
                print(f'Unable to download ({base_url}): {e}')
                continue
            
            save(data, f'data/{current_date}_{sensor}.csv')

if __name__ == '__main__':
    download_days(days_between_today_and_past_date(2022, 1, 1))