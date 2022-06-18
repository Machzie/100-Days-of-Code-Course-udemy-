# Day 47 Project - Amazon Price Tracker
import config
import requests
import smtplib
from bs4 import BeautifulSoup

header = {
    "Accept-Language": "en",
    "User-Agent": "Defined"
}

response = requests.get(config.amazon_url, headers=header)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()
price_flt = float(price.split("£")[1])

product_name = soup.select(selector="#productTitle")[0].getText().strip(" ")

target_price = 40.00

if price_flt < target_price:

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=config.email_id, password=config.email_pw)
        connection.sendmail(from_addr=config.email_id, to_addrs=config.email_id,
                            msg=f"Subject: Amazon Price Alert!\n\n"
                                f"The price for {product_name} is now less than £{target_price:.2f}!\n"
                                f"\n"
                                f"Take a look: {config.amazon_url}".encode('utf-8')
                                )
