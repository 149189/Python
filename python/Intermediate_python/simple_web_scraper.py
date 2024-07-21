#Write a program that scrapes data from a website and displays it.
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial")


if response==200:
    print("Successfully Fetched the webpage!")
    soup = BeautifulSoup(response.content,'html.parser')
    titles = soup.find_all('h2',class_='entry-title')

    for index,title in enumerate(titles,start=1):
        print(f"{index}.{title.get_text()}")
else:
    print("Failed to retrieve the Webpage. status code: ",response.status_code)