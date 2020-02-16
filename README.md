《魔兽世界怀旧服》自动排队及防掉线工具
===================================


该工具仅限Win64下使用。开发环境为Windows 10，Python 3.6.2。

## 开发

执行下述命令构建开发环境。


```
D:\dev\autoqueue> python -m venv .env
D:\dev\autoqueue> bin\Scripts\activate
D:\dev\autoqueue> (.env) pip install -r requirements.txt
```

### 结构

本工具采用PyQt5构建UI，采用pyautogui和pywin32作为窗体控制工具。

### 编辑界面

请安装[QtDesigner](https://build-system.fman.io/qt-designer-download)编辑文件 `ui/autoqueue.ui`。
编辑完成后，运行如下命令生成 Python 代码：

```
pyuic5 ui\autoqueue.ui > ui\autoqueue.py
```


## 使用

执行下述命令启动。

```
D:\dev\autoqueue> (.env) python autoqueue.py
```

或者可以编译成.exe文件分发。

```
D:\dev\autoqueue> (.env) auto-py-to-exe
```

