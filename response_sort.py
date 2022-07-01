import requests
from requests.sessions import Session
import csv

website_url_list = ["https://www.google.com/","https://www.netflix.com/","https://www.linkedin.com/","https://www.amazon.in/"]*25

result = {}
sorted_result = {}

# Iteration of all URL and send HTTPS GET Request
def send_https_request(urls:list):
    with requests.Session() as session:
        for url in urls:
            https_get_request(url,session=session)

# Store all result into dictionarie in formate  Key = Response Time, Value = WebsiteURL, Status code
def https_get_request(url:str,session:Session):
    with session.get(url) as response:
        key = response.elapsed.total_seconds()
        status_code = response.status_code
        result[key] = url,status_code

# Creating csv file with columna 'Website URL','Status Code','Response Time'
def create_csv_file(result):
    with open('/Users/sanketjaiswal/Desktop/Test/latency_evaluate_py/https_response.csv','w',newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Website URL','Status Code','Response Time'])

        for k in result:
           thewriter.writerow([list(k[1])[0],list(k[1])[1],k[0]])

send_https_request(website_url_list)

# Sort the dictionary based on the lowest response time among all the URLs
sorted_result = sorted(result.items())
create_csv_file(sorted_result)