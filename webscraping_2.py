from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.yelp.com/search?find_desc=Ramen&find_loc=Dusseldorf,++North+Rhine-Westphalia').text

soup = BeautifulSoup(source, 'lxml')


csv_file = open('ramen_plc.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Address', 'Numbers'])


sum_data = soup.find_all("div", {"class" : "biz-listing-large"})

for item in sum_data:
        name = item.find("a", {"class" : "biz-name"}, "span").text
        print(name)


        street_adr = item.find("address").get_text(separator='\n')
        try:
            print(street_adr)
        except:
            "not working"


        phone_num = item.find("span", {"class" : "biz-phone"}).text
        print(phone_num)


        csv_writer.writerow([name, street_adr, phone_num])

csv_file.close()
