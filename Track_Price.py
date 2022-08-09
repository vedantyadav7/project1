import requests
from bs4 import BeautifulSoup
import time
import smtplib

URL = 'https://www.amazon.de/Mount-Format-Digital-Camera-ILCE-7M3/dp/B07B4L1PQ8/ref=sr_1_1_sspa?crid=UCVNIW99B72T&keywords=sony+a7&qid=1660058650&sprefix=sony+a7%2Caps%2C497&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOFMwM1FHN1hDV003JmVuY3J5cHRlZElkPUEwOTcxOTA2MzJYSThFQUQwRDQ4MiZlbmNyeXB0ZWRBZElkPUEwMDY2NjEwM0NMSktQOFo2NVVKUyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}


def price_check():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="desktop_unifiedPrice").get_text()
    converted_price = (price[0:5])
    print(converted_price)

    if (converted_price < '60.000'):
        send_mail()

    if (converted_price > '67.000'):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vedant.yadav7@gmail.com', 'gcdoyhfpjwhxeuhj')

    subject = "Alert! Price fell down"
    body = "Hey! The Price of the product you were looking for went down. Check the link below :https://www.amazon.de/Mount-Format-Digital-Camera-ILCE-7M3/dp/B07B4L1PQ8/ref=sr_1_1_sspa?crid=UCVNIW99B72T&keywords=sony+a7&qid=1660058650&sprefix=sony+a7%2Caps%2C497&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOFMwM1FHN1hDV003JmVuY3J5cHRlZElkPUEwOTcxOTA2MzJYSThFQUQwRDQ4MiZlbmNyeXB0ZWRBZElkPUEwMDY2NjEwM0NMSktQOFo2NVVKUyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

    msg = (f"Subject : {subject}\n\n{body}")
    server.sendmail('vedant.yadav7@gmail.com',
        'vedant.srim2020@gmail.com',
        msg
        )
    print("Email Has been sent")
    server.quit()


if __name__ == "__main__":
    while (True):
        price_check()
        time.sleep(60*60*60)

