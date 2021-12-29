from django.shortcuts import render
from django.http import response
def post_list(request):
    return render(request, 'blog/post_list.html', {})
