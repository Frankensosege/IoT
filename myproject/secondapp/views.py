from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def exam1(request):
    template = loader.get_template('exam1.html')
    # print(template)
    return HttpResponse(template.render(None, request))

def exam2(request):
    template = loader.get_template('exam2.html')
    context = {'name': 'test', 'address':'서울시'}
    return HttpResponse(template.render(context, request))
    # == return render(request, 'exam2.html', context)

def exam3(request):
    context = {'name': 'test', 'address':'서울시'}
    return render(request, 'exam2.html', context)

def exam4(request):
    context = {'name': None, 'address':None}
    return render(request, 'exam4.html', context=context)

def exam5(request):
    template = loader.get_template('exam5.html')
    if request.method == 'GET':
        msg='GET 방식으로 호출'
    else:
        msg='POST 방식으로 호출'
    context = {'result': msg}
    return HttpResponse(template.render(context, request))
