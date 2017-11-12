from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import MyFirstModel

from .models import MyModelForSum

from forms import MyForm_1
from django.http import HttpResponse

def my_page_first(request):
    my_records_arr = MyFirstModel.objects.order_by('published_date')
    return render(request, 'prilogenie111/my_page_first.html', {'my_records_arr': my_records_arr})

def my_page_second(request, pk):
    my_record = get_object_or_404(MyFirstModel, pk=pk)
    return render(request, 'prilogenie111/my_page_second.html', {"my_record": my_record})

def my_page_third(request):
    form = MyForm_1()
    return render(request, 'prilogenie111/my_page_third.html', {"form": form})

def my_summa(request):
    a = int( request.GET['a'] )
    b = int( request.GET['b'] )
    c = a + b

    a = str(a)
    b = str(b)
    c = str(c)

    MyModelForSum.objects.create(aaa = a, bbb = b, ccc = c)

    my_arr = MyModelForSum.objects.order_by('pk')

    bigString = ""
    for kkk in my_arr:
        bigString = bigString + kkk.aaa + "___" + kkk.bbb + "___" + kkk.ccc + "\n"

    return HttpResponse(str(bigString))