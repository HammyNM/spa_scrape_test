
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import quote

#enviromental housekeeping
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

API_Token = os.getenv("scrapeDo_key")
Target_url = "https://scotland.shinyapps.io/ScotPHO_profiles_tool/"
JsonInstructions = ""

def tempInstructionFunction():
    #tempCode to test concept
    DSselector = '[value="Main Dataset"]'
    Regionselector = '[value="Scotland"]'

    JsonInstructions = json.dumps([{"Action": "Click","Selector": DSselector},
                                   {"Action": "Wait", "Timeout": 2000},
                                   {"Action": "Click","Selector": Regionselector},
                                   {"Action": "Wait", "Timeout": 2000}])

    #likely needless
    #{"Action": "Click","Selector": ".btn.btn-sm.dropdown-menu.show"}
    
    return JsonInstructions

def scrape_site():
    JsonInstructions = tempInstructionFunction()
    api_url= f"https://api.scrape.do?token={API_Token}&url={quote(Target_url)}&render=true&playWithBrowser={quote(JsonInstructions)}"

    response = requests.get(api_url, timeout=45, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Connected")

        #find dynamic titles - TEST
        #testType = soup.find_all('div', class_='item')
        #for item in testType:
        #    print("Found:", item.text)

        #TO:DO Code to get CSV or parquet link for dataset

    else:
        print("Failed:", response.status_code)

scrape_site()
