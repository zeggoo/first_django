from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Yor're at the polls index.")


def post_list(request):
    # 장고걸스 테스트용
    return render(request, 'polls/post_list.html', {})
