# latency_evaluate_py
This Python script is responsible for sending HTTPS requests to 100 URLs and getting the response time It will also sort URLs based on lowest response time. In the end, It will also store URLs, Status Codes, and Response Time on CSV file.

Python Script Workflow

1. First I have created an array of website URLs and I’m taking 4 website URL examples with a multiplication of 25 to convert this list into 100 URL lists.
2. I have initialized two empty dictionaries to store the results of Website URL, Response Time, and Status code and I have chosen the python dictionary      because it stores the value in key formate. Key = Response Time, Value = WebsiteURL, Status code.
3. Then I have created one method to send http request to all array website url then I have created request session using with statement. with statement in Python is used in exception handling to make the code cleaner and much more readable. Using for loop it will iterate every url in array and send https get request.
4. Second method https_get_request this method is responsible to get the session response and it will adding value in dictionaries in this format Key = Response Time, Value = WebsiteURL, Status code.
5. It will sort the dictionary based on the lowest response time among all the URLs.
6. Third method is to create the CSV file and we’re creating every dictionarie value into different csv column. First I have created top row writerow(  ['Website URL','Status Code','Response Time']) then using for loop it will copy website url, status code, response time.

And this script will also work for nonstatus response codes but currently I don't have any URL that returns 404 or 500 status codes.

To run this same script in your environment you need to change the csv file path only -> open('<path>/resultponse.csv','w',newline='')

