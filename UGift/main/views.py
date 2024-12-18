from django.shortcuts import render

def index(request):
    return render(request,'main/index.html', {'title':''})

def page1(request):
    return render(request,'main/page1.html')

def page2(request):
    return render(request,'main/page2.html')

def page3(request):
    return render(request,'main/page3.html')
