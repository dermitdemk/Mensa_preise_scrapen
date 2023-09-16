from bs4 import BeautifulSoup
import requests
from datetime import date
import time
import pandas as pd
from gettext import find
import mysql.connector
import re


webseite_der_mensa = 'https://www.stw-thueringen.de/mensen/erfurt/mensa-nordhaeuser-strasse.html'

html_as_text = requests.get(webseite_der_mensa).text
soup = BeautifulSoup(html_as_text,'lxml')
today = date.today()
today_as_string= string_formatting = '{:%d.%m.%Y}'.format(today)

def preis_from_str_to_float(string):
    if len(string.split(" "))>2:
        for number in re.findall(r'\d.\d+', string):
            if "," in number:
                string = number
            else:
                string = 0
    
    return float(str(string.replace(",",".")))

def find_meals_of_today():
    path_on_local = 'data/daten.csv'
    path_on_server = '/home/erik/mensa_scrapen/data/daten.csv'
    mydb = mysql.connector.connect(host="//////////////",user="////////////",password="///////////",database="//////")

    menu_of_meals = soup.find_all('div', class_= 'row rowMealInner p-3 rounded')

    for meal in menu_of_meals :
        is_vegan = False
        name_of_meal = meal.find('div', class_='mealText' ).text
        all_prices_as_str = meal.find('div', class_='mealPreise' ).text
        all_prices_as_str = all_prices_as_str[:-1]
        all_prices_as_list = all_prices_as_str.split('/')
        all_icons_of_the_meal = meal.find_all('img', class_='splIconMeal')
        for icon in all_icons_of_the_meal:
            lable_of_icon = icon.get('alt')
            if 'Vegan' in lable_of_icon :
                is_vegan = True
        d = {'essen' : [name_of_meal],
        'preis_st' : [all_prices_as_list[0]],
        'preis_ma' : [all_prices_as_list[1]],
        'preis_ga' : [all_prices_as_list[2]],
        'datum':[today_as_string],
        'vegan': [is_vegan]}

        student_preis = preis_from_str_to_float(all_prices_as_list[0])
        mitarbeiter_preis = preis_from_str_to_float(all_prices_as_list[1])
        gast_preis = preis_from_str_to_float(all_prices_as_list[2])
        sql ="INSERT INTO Mensa_data_of_scraper (gericht_name, student_preis, mitarbeiter_preis, gast_preis, is_vegan, datum) VALUES (%s, %s, %s,%s, %s, %s)"
        val = (name_of_meal, student_preis, mitarbeiter_preis, gast_preis,is_vegan,today)
        mycursor = mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()        
        
        df = pd.DataFrame(d, columns=['essen', 'preis_st','preis_ma','preis_ga', 'datum','is_vegan'])
        df.to_csv(path_on_server, mode='a', header=False, index=False)
    saved = pd.read_csv(path_on_server)


if __name__ =='__main__':
    find_meals_of_today()

