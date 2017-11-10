from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import MyFirstModel

def my_page_first(request):
    my_records_arr = MyFirstModel.objects.order_by('published_date')
    return render(request, 'prilogenie111/my_page_first.html', {'my_records_arr': my_records_arr})

def my_page_second(request, pk):
    my_record = get_object_or_404(MyFirstModel, pk=pk)
    return render(request, 'prilogenie111/my_page_second.html', {"my_record": my_record})