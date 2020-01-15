import os
import sys
from pathlib import Path
from configparser import RawConfigParser as _ConfigParser

class _PowerConfigParser(_ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

    def geteval(self, section, option):
        result = self.get(section, option)
        try:
            return eval(result)
        except:
            return result

class Config:
    def __init__(self):
        self._path='./config.ini'
        self._dict = {}
        self._section = None
        self.read_ini()

    def read_ini(self):
        self._conf = _PowerConfigParser()
        p = Path(sys.argv[0])
        # print("=" * 100)
        _ini_path = p.joinpath(p.parent, self._path)
        if os.path.exists(_ini_path):
            # 文件存在读取ini文件
            self._conf.read(_ini_path, encoding="utf-8")

            # 如果self._section没有初始化，则尝试从conf.conf 读取section。
            if self._section is None:
                try:
                    self._section = self._conf.geteval("conf", 'conf')
                except:
                    # print("ini file not have >\n[conf]\nconf=configuration_name\n---------------------------")
                    # 读取conf.conf 失败，直接返回
                    return
            # 如果self._section已经初始化，则继续读取内容。
            else:
                pass
        else:
            return
        print('文件位置：', _ini_path)
        _list_session = self._section.split(".")
        _names = []
        if '.' in self._section:
            for _index in range(len(_list_session)):
                _n, *_ = self._section.rsplit('.', _index)
                _names.insert(0, _n)
        else:
            _names.append(self._section)
        # print("加载配置顺序：", _names)
        # _conf = _PowerConfigParser()
        # _conf.read(_cfgpath, encoding="utf-8")
        _sections = self._conf.sections()
        # sections
        # print("所有项目配置：", _sections)
        for __name in _names:
            self._run(self._conf,__name)
        # for k, v in self._dict.items():
        #     if not k.startswith('_'):
        #         print("%-20s | %-14s | %s" % (k, type(v), v))
        print("=" * 100)

    def _run(self,_conf,name):
        # 调用读取配置模块中的类
        _options = _conf.options(name)
        for _option in _options:
            _values = _conf.geteval(name, _option)
            self._dict[_option]=_values

    def printall(self):
        print(self._dict)
        return self._dict

    def __getattr__(self, item):
        result = self._dict.get(item)
        if result is None:
            if self._section is None:
                raise Exception("config._section is null,please call config")
            raise KeyError("arg <%s> not in section <%s>"%(item,self._section))
        return result

    def __call__(self, path='./config.ini',argument=False):
        self._dict = {}
        self._path = path
        if argument:
            self.set_argv(argument)
        self.read_ini()

    def set_argv(self,argument):
        argvs = sys.argv
        try:
            index = argvs.index(argument)
        except ValueError:
            raise ValueError(f"require {argument} argument")
        self._section = argvs[index+1]

config = Config()