import datetime

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .kiwoom import k_module


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
        return HttpResponseRedirect(reverse('kiwoom:index'))

    return render(request, 'kiwoom/home.html', {
        'login_state': k_module.get_connect_state()
    })


def api_docs(request):
    return HttpResponse(k_module.ocx.generateDocumentation())


def account_info(request):
    return render(request, 'kiwoom/account_info.html', {
        'login_state': k_module.get_connect_state(),
        'account_count': k_module.get_login_info("ACCOUNT_CNT"),
        'account_no': k_module.get_login_info("ACCNO"),
        'user_id': k_module.get_login_info("USER_ID"),
        'user_name': k_module.get_login_info("USER_NAME"),
        'key_input_security': k_module.get_login_info("KEY_BSECGB"),
        'firewall': k_module.get_login_info("FIREW_SECGB")
    })


def stock_list(request):
    return render(request, 'kiwoom/stock_list.html', {
        'login_state': k_module.get_connect_state(),
        'market_list': k_module.MARKET_LIST
    })


def stock_detail_list(request, market_type):
    return render(request, 'kiwoom/stock_detail_list.html', {
        'login_state': k_module.get_connect_state(),
        'stock_code_list': k_module.get_code_list_by_market(market_type).strip(';').split(';'),
        'k_module': k_module
    })


def basic_info(request, code):
    k_module.set_input_value('종목코드', code)
    k_module.comm_rq_data("주식기본정보", "opt10001", 0, k_module.S_SCREEN_NO)
    tr_data = k_module.qs['OnReceiveTrData'].get()
    return render(request, 'kiwoom/basic_info.html', {
        'login_state': k_module.get_connect_state(),
        'name': k_module.comm_get_data(tr_data['sTrCode'], "", tr_data['sRQName'], 0, "종목명"),
        'quantity': k_module.comm_get_data(tr_data['sTrCode'], "", tr_data['sRQName'], 0, "거래량"),
        'current_price': k_module.comm_get_data(tr_data['sTrCode'], "", tr_data['sRQName'], 0, "현재가"),
        'total_price': k_module.comm_get_data(tr_data['sTrCode'], "", tr_data['sRQName'], 0, "시가총액")
    })


def chart(request, code):
    k_module.set_input_value("종목코드", code)
    k_module.set_input_value("기준일자", datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"))
    k_module.set_input_value("수정주가구분 ", 0)
    k_module.comm_rq_data("주식일봉차트조회요청", "opt10081", 0, k_module.S_SCREEN_NO)
    data = k_module.qs['OnReceiveTrData'].get()
    comm_data_ex = k_module.get_comm_data_ex(data['sTrCode'], data['sRQName'])
    print(comm_data_ex)
    return render(request, 'kiwoom/chart.html', {
        'login_state': k_module.get_connect_state()
    })
