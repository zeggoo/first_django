from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),    # 장고걸스 테스트용
    path('', views.index, name="index"),
]
