# 默认读取当前目录的config.ini，section默认读取ini文件下的conf.conf
from configboy import config
print(config.username)

# 读取指定的config.ini，section默认读取ini文件下的conf.conf
from configboy import config;config(path='../config.ini')
print(config.username)

# 默认读取当前目录的config.ini，通过-p参数指定section
from configboy import config;config(argument='-p')
print(config.username)