# configman
读取ini文件，生成子类配置文件，可以使用语法conf.a.b.c来配置项目

## 使用
直接运行build_config.py文件会读取当前文件夹的base.config.ini配置信息，然后生成config.py文件。
运行test.py文件，可以看到调用的实例。

## 关于
要是使用dict，修改dict的行为也可以做到，点语法的功能。但是，没有办法完全对照ini的语法信息。
所以，使用了类继承的方法实现了这个功能。（其实，当时压根没有想起python的魔法方法可以实现这个功能）
