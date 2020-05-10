import requests
from bs4 import BeautifulSoup
import sendgrid
from sendgrid.helpers.mail import *
import pytz
from datetime import datetime


def getattendance(usernameStr, passwordStr):
    payload = {
        '__VIEWSTATE': '/wEPDwULLTEyNjQ1NjQ1NzQPZBYCAgEPZBYCAgUPDxYCHgdWaXNpYmxlaGRkZIqPif+b0uAXNRcpudOPuSZIhFZF+ZyEYJSsRc5adfuf',
        '__VIEWSTATEGENERATOR': 'C2EE9ABB',
        '__EVENTVALIDATION': '/wEdAAa6Rfbp834zD41GZae+BZolBjpuGLkudYNkCAonVyADt+5PVNfdHmla7NuBu7/wrMOVJ8S+i3yz3zEAJ6fmP76XY3plgk0YBAefRz3MyBlTcIFjpILoFgeQqvXWA+7aEDSCFTPwlWoys6XvWcua8jBxOuyAd8tWuNIe5msclFCGcw==',
        'txtUserName':usernameStr,
        'btnNext': 'Next'
    }
    payload1 = {
        '__VIEWSTATE': '/wEPDwULLTEyNjQ1NjQ1NzQPZBYCAgEPZBYUAgUPDxYCHgdWaXNpYmxlaGRkAgsPDxYCHwBnZGQCDQ8PFgQeCEltYWdlVXJsBUR+XEVSUFxBZG1pblxTdHVkZW50UGhvdG9zLmFzcHg/U3R1ZElkPTc1ODAmQ29sQ29kZT0wMDAxJkdycENvZGU9Q0JJVB8AZ2RkAhEPDxYGHgRUZXh0BQwxNjAxMTc3MzUxMDEeB0VuYWJsZWRoHwBoZGQCEw8PFgIfAGdkZAIVDw8WAh8CZWRkAhcPDxYCHwBoZGQCGQ8PFgIfAGdkZAIdDw8WAh8AZ2RkAh8PDxYCHwBnZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFB0ltZ0JhY2sFDEltZ1VzZXJQaG90b+3TjDS6wPcYpl0eo1T9sdc7OYOuW7x+zNdEArjy8kFO',
        '__VIEWSTATEGENERATOR': 'C2EE9ABB',
        '__EVENTVALIDATION': '/wEdAArZEQT62kYeIwT3xYElIUTOBjpuGLkudYNkCAonVyADt+5PVNfdHmla7NuBu7/wrMOVJ8S+i3yz3zEAJ6fmP76XMqzV50RwENIvbYFT84oCw9L5WsiImyZWZthxHYT/WpZ2NvjHOkq5wKoqN6Aim8WGPOaW1pQztoQA36D1w/+bXSh34ya5objibTUZ9mTnN+RqfELTZPFfe1CxOjiRYdfTeuKweSZO7NTrXZptLn4NUrwnT1HzgkYKQw3KvA6DgL0=',
        'txtPassword': passwordStr,
        'btnSubmit': 'Next'}

    with requests.Session() as s:
        url = 'https://erp.cbit.org.in/Login.aspx?ReturnUrl=%2f'

        r = s.get(url)

        r = s.post(url, data=payload)

        r = s.post(url, data=payload1)
        soup = BeautifulSoup(r.content, 'html5lib')
        return(soup.find(id="ctl00_cpStud_lblTotalPercentage").getText())


def sendmail(mailid,name,attendance,time):
    sg = sendgrid.SendGridAPIClient(api_key="ENTER API KEY")
    from_email = Email("mprajay999@gmail.com")
    to_email = To(mailid)
    subject = "Attendance"
    content = Content("text/plain","Hi {} your Attendance is {} on {}".format(name,attendance,time))
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)


def gettime():
    tz = pytz.timezone('Asia/Kolkata')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    return (datetime.now(tz).strftime(fmt))

