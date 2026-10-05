
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

#enviromental housekeeping
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

API_Token = os.getenv("scrapeDo_key")
Target_url = "https://scotland.shinyapps.io/ScotPHO_profiles_tool/"

def scrape_site():
    api_url= f"https://api.scrape.do?token={API_Token}&url={quote(Target_url)}&render=true"

    response = requests.get(api_url, timeout=45, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Connected")

        #find dynamic titles
        testType = soup.find_all('div', class_='item')
        for item in testType:
            print("Found:", item.text)
    else:
        print("Failed:", response.status_code)

scrape_site()
