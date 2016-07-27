import datetime

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .kiwoom import k_module, k_thread, k_q


def index(request):
    if request.GET.get('login') and not k_module.get_connect_state():
        k_module.comm_connect()
        k_module.qs['OnEventConnect'].get()  # waiting for login
        if k_module.get_connect_state():
            messages.success(request, 'Login Succeeded')
        else:
            messages.error(request, 'Login Failed')
        return HttpResponseRedirect(reverse('kiwoom:index'))
    elif request.GET.get('logout') and k_module.get_connect_state():
        # Logout function does not exist.
        pass

    return render(request, 'kiwoom/home.html', {'login_state': k_module.get_connect_state()})


def basic_info(request, code):
    k_module.set_input_value('종목코드', code)
    k_module.comm_rq_data("주식기본정보", "opt10001", 0, "0001")
    tr_data = k_module.qs['OnReceiveTrData'].get()
    view_data = {
        'code': k_module.comm_get_data(tr_data['sTrCode'], "", tr_data['sRQName'], 0, "종목명"),
        'quantity': k_module.comm_get_data(tr_data['sTrCode'], "", tr_data['sRQName'], 0, "거래량")
    }
    return render(request, 'kiwoom/basic_info.html', view_data)


def chart(request, code):
    k_module.set_input_value("종목코드", code)
    k_module.set_input_value("기준일자", datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"))
    k_module.set_input_value("수정주가구분 ", 0)
    k_module.comm_rq_data("주식일봉차트조회요청", "opt10081", 0, "0002")
    data = k_module.qs['OnReceiveTrData'].get()
    comm_data_ex = k_module.get_comm_data_ex(data['sTrCode'], data['sRQName'])
    print(comm_data_ex)
    return render(request, 'kiwoom/chart.html')
