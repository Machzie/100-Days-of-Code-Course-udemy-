# Day 35 Project - Rain Alert App
import requests
import datetime as dt
import smtplib
import config


weather_params = {
    "lat": 51.507,
    "lon": -0.128,
    "exclude": "minutely",
    "appid": config.api_key,
    "units": "metric"
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
weather_data = request.json()

for i in range(12):
    time_unix = weather_data["hourly"][i]["dt"] + weather_data["timezone_offset"]
    time = dt.datetime.utcfromtimestamp(time_unix).strftime('%I %p')
    weather_code = weather_data["hourly"][i]["weather"][0]["id"]

    if weather_code < 700:

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=config.email_id, password=config.email_pw)
            connection.sendmail(from_addr=config.email_id, to_addrs="mattzieba@gmail.com",
                                msg=f"Subject:Rain Alert!\n\n"
                                    f"Rain expected to start at {time}\n"
                                    f"Bring an umbrella!")
        break
