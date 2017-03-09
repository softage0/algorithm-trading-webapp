# Algorithm Trading

Algorithm Trading web application project with Python, Django, PyQt5 and Javascript


## Requirements

* Windows 7/10
* [Python 3.5.x 32bit](https://www.python.org/)
* [Kiwoom Flash(번개) and Kiwoom Open API+ module](https://www2.kiwoom.com/nkw.templateFrameSet.do?m=m1408000000)

## Setup Instructions

Clone the repo: `https://github.com/softage0/algorithm-trading-webapp.git`

Run the following code on the cloned repo:
```
$ pip install -r requirements.txt
```


## Quick Start

Run dev server:
```
$ python manage.py runserver
```

Then you can access by the following URL:
http://127.0.0.1:8000/


## Setup Zipline (optional)

*The following is the installation steps for Windows platform. The installations on the other platforms may be different.*

[Zipline](http://www.zipline.io/) is a Pythonic algorithmic trading library. It is an event-driven system that supports both backtesting and live-trading.


Install the following build tools first:

* [Visual C++ Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools)

Download the following packages from [Gohlke's repository](http://www.lfd.uci.edu/~gohlke/pythonlibs/):

* numpy-1.11.1+mkl-cp35-cp35m-win32.whl
* scipy-0.17.1-cp35-cp35m-win32.whl
* numexpr-2.6.0-cp35-cp35m-win32.whl

And install them:
```
$ pip install {filename} 
```

Install Zipline:
```
$ pip install zipline 
```


## References
* 파이썬을 이용한 시스템 트레이딩 (기초편)(https://wikidocs.net/book/110)
* https://github.com/sculove/QWebview-plus
