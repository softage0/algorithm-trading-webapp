import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .kiwoom import k_module, k_q


def index(request):
    if request.GET.get('login') and not k_module.get_connect_state():
        k_module.comm_connect()
        k_q.get()  # waiting for login
        HttpResponseRedirect(reverse('trade:index'))
    elif request.GET.get('logout') and k_module.get_connect_state():
        k_module.comm_terminate()
        HttpResponseRedirect(reverse('trade:index'))

    return render(request, 'trade/index.html', {'login_state': k_module.get_connect_state()})


def basic_info(request, code):
    k_module.set_input_value('종목코드', code)
    k_module.comm_rq_data("주식기본정보", "opt10001", 0, "0001")
    return render(request, 'trade/basic_info.html', k_q.get())


def chart(request, code):
    k_module.set_input_value("종목코드", code)
    k_module.set_input_value("기준일자", datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"))
    k_module.set_input_value("수정주가구분 ", 0)
    k_module.comm_rq_data("주식일봉차트조회요청", "opt10081", 0, "0002")
    data = k_q.get()
    print(k_module.get_comm_data_ex(data['trCode'], data['sRQName']))
    return render(request, 'trade/chart.html')
