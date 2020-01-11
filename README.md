# configboy
> 读取ini文件，添加到config.py的全局变量

## 安装
> pip install configboy

## 使用
> 只在需要配置文件的地方，运行命令configboy。在当前目录下会生成config.ini文件和config.py文件。运行项目的时候，需要添加选择配置的参数。试着运行 python config.py configboy.dev.api 看看。项目引用配置的时候，直接import config，config.username 进行使用。

## 工作过程
> 配置的名称会以点分割，然后会覆盖前者的配置。例如：configboy.dev.api 会覆盖 configboy.dev的配置，configboy.dev会覆盖configboy的配置。