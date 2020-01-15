# import config
# print(config.username)
# import requests
# r = requests.get(config.url)
# print(r.text)
from configboy import config;config(path="../config.ini",argument='-p')
# config.path('./config.ini','base') # 一个项目调用一次
# print(config.asd)
# print(config.username)
config.printall()
# print(config.__dict__)
# import test
