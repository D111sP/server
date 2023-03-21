from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from cheat.models import *


@csrf_exempt
def check(request):
    if request.method == 'POST':
        status = {'status': False}

        key_base = Key_base.objects.all()
        reg_date_user = Date_user.objects.all()

        key_user = request.POST.get("key")
        print(key_user)
        wfi_user = request.POST.get("wfi")
        name_PC_user = request.POST.get("name_PC")

        for key_b in key_base:
            if key_b.key == key_user:
                if len(reg_date_user) == 0:
                    form = fill_Date_user(request.POST, key_b)
                    form.save()
                    status['status'] = True
                    fill_History_date_user(request.POST, status['status'])
                    return JsonResponse(status)
                else:
                    for el_user in reg_date_user:
                        if el_user.key.key == key_user and el_user.wfi == wfi_user and el_user.name_PC == name_PC_user:
                            status['status'] = True
                            fill_History_date_user(request.POST, status['status'])
                            return JsonResponse(status)
                    try:
                        form = fill_Date_user(request.POST, key_b)
                        form.save()
                        status['status'] = True
                        fill_History_date_user(request.POST, status['status'])
                        return JsonResponse(status)
                    except Exception:
                        fill_History_date_user(request.POST, status['status'])
                        return JsonResponse(status)
                break

        fill_History_date_user(request.POST, status['status'])
        return JsonResponse(status)

def fill_Date_user(re_Post, key):
    form = Date_user()
    print(key)
    form.key = key
    form.name_PC = re_Post.get("name_PC")
    form.ip = re_Post.get("ip")
    form.stone = re_Post.get("stone")
    form.wfi = re_Post.get("wfi")
    form.uname = re_Post.get("uname")


    return form

def fill_History_date_user(re_Post, status):
    form = History_date_user()

    form.key = re_Post.get("key")
    form.name_PC = re_Post.get("name_PC")
    form.ip = re_Post.get("ip")
    form.stone = re_Post.get("stone")
    form.wfi = re_Post.get("wfi")
    form.uname = re_Post.get("uname")
    form.status = status

    form.save()
