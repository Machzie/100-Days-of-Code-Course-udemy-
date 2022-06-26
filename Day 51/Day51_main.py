# Day 51 Project - Internet Speed Checker Bot

from Bot import InternetSpeedTwitterBot

results = InternetSpeedTwitterBot().get_internet_speed()

down_speed = float(results[0])
up_speed = float(results[1])

InternetSpeedTwitterBot().tweet_at_provider(down_speed, up_speed)
