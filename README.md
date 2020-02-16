《魔兽世界怀旧服》自动排队及防掉线工具
===================================


该工具仅限Win64下使用。开发环境为Windows 10，Python 3.6.2。

开发
========

执行下述命令构建开发环境。


```
D:\dev\autoqueue> python -m venv .env
D:\dev\autoqueue> bin\Scripts\activate
D:\dev\autoqueue> (.env) pip install -r requirements.txt
```

使用
========

执行下述命令启动。

```
D:\dev\autoqueue> (.env) python autoqueue.py
```

或者可以编译成.exe文件分发。

```
D:\dev\autoqueue> (.env) auto-py-to-exe
```

