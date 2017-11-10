from django.shortcuts import render

def my_page_first(request):
    return render(request, 'prilogenie111/my_page_first.html', {})

def my_page_second(request):
    return render(request, 'prilogenie111/my_page_second.html', {})