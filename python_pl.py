from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1').text
soup = BeautifulSoup(source, 'lxml')

data = soup.find('div')

phones = data.find_all('div', class_='a-section a-spacing-medium')
names_class = 'a-size-base-plus a-color-base a-text-normal'
reais_class = 'a-price-whole'
cents_class = 'a-price-fraction'

csv_file = open('iphones_amazon.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['phone_name', 'price'])

for i in range(len(phones)):
    try:
        print(f'{phones[i].find("span", class_=names_class).text} || Price: {phones[i].find("span", class_=reais_class).text}{phones[i].find("span", class_=cents_class).text}')
        print()
        csv_writer.writerow([phones[i].find("span", class_=names_class).text, f'{phones[i].find("span", class_=reais_class).text}{phones[i].find("span", class_=cents_class).text}'])

    except:
        print(f'{phones[i].find("span", class_=names_class).text} || SEM ESTOQUE')
        print()
        csv_writer.writerow([phones[i].find("span", class_=names_class).text, '-'])
csv_file.close()