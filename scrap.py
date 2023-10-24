import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient

#to scrape and get it in string
def getdata(url):
    r = requests.get(url)
    return r.text


#html code 
def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    return(soup)

#filter jobs
def jobs(soup):
    data_str = ''
    for i in soup.find_all("div", class_ = "mosaic mosaic-provider-jobcards mosaic-provider-hydrated"):
        data_str = data_str + i.get_text()
    res_1 = data_str.split("\n")
    return(res_1)

#filter company data
def company_data(soup):
    data_str = ''
    res = ''
    for i in soup.find_all('div', class_ = 'heading6 company_location tapItem-gutter companyInfo'):
        data_str = data_str + i.get_text()
    res_1 = data_str.split("\n")

    res = []
    for item in range(1, len(res_1)):
        if len(res_1[item]) > 1:
            res.append(res_1[item])
    return(res)

if __name__ == "__main":
    #get the Python developer jobs in Aurangabad, Maha
    job = "python+developer"
    location = "Pune%2C+Maharashtra"
    url = "https://www.indeed.co.in/jobs?q=" + job + "&l=" + location

    #get it in html 
    soup = html_code(url)

    #get the data and store it
    job_res = jobs(soup)
    comp_res = company_data(soup)


#STOEING THE DATA IN MONGODB
mongo_uri = "mongodb://localhost:27017/"
db_name = "emp_data"
client = MongoClient(mongo_uri)
db = client[db_name]

collection = db['emp']

with open('indeed_jobs.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        collection.insert_one(row)

    
