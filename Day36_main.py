# Day 36 Project - Stocks and Shares Terminal
import requests
import datetime as dt
import smtplib
import config

STOCK_TICKER = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_TICKER,
    "apikey": config.stock_api_key
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "from": dt.datetime.now().strftime("%Y-%m-%d"),
    "apiKey": config.news_api_key
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

stock_data_m1 = stock_data_list[0]
stock_data_m1_close = float(stock_data_m1["4. close"])
stock_data_m2 = stock_data_list[1]
stock_data_m2_close = float(stock_data_m2["4. close"])

print(stock_data_m1_close, stock_data_m2_close)

stock_diff = stock_data_m1_close - stock_data_m2_close
stock_diff_abs = abs(stock_diff)

stock_diff_pc = (stock_diff / stock_data_m1_close) * 100
print(stock_diff_pc)

if stock_diff_pc >= 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()

    articles = news_data["articles"][:3]

    #article_formatted = [f'{article["title"]}\n{article["description"]}' for article in articles]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=config.email_id, password=config.email_pw)
        for article in articles:
            connection.sendmail(from_addr=config.email_id, to_addrs=config.email_id,
                                msg=f"Subject:{STOCK_TICKER}: {stock_diff_pc:+.2f} %\n\n"
                                f"Headline: {article['title']}\n"
                                f"Description: {article['description']}".encode('utf-8'))
