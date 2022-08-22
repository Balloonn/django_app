from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">my webpage</h1>'
    line2 = '<a href="/play/">进入游戏</a>'
    return HttpResponse(line1 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<a href="/">返回主页面</a>'
    return HttpResponse(line1 + line2)
