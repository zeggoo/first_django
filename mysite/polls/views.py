from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


from .models import Post  # 장고걸스 테스트용


def index(request):
    return HttpResponse("Hello, world. Yor're at the polls index.")


def post_list(request):
    # 장고걸스 테스트용
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'polls/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # 장고걸스 테스트용
    post = get_object_or_404(Post, pk=pk)    
    return render(request, 'polls/post_detail.html', {'post': post})
