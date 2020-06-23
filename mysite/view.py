# I have created this file
#from django.http import HttpResponse
# Code 1
#def index(request):
#   return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com/watch?v=XgkHROatjHI"> mo salah</a> <a
#    href="https://www.facebook.com/">Facebook</a>''')
#def about(request):
#    return HttpResponse("about akshay")

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'city':'berlin','country':'germany'}
    return render(request,'index.html',params)
def about(request):
    return HttpResponse('''<h1>about</h1> <a href='/'>back</a>> goback </a>''')
def analyze(request):
    a = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    newline = request.GET.get('newline','off')
    spaceremover = request.GET.get('spaceremover','off')
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if newline == "on":
        for char in a:
            if char != "/n":
                analyzed = analyzed + char
        a=analyzed
        analyzed=""
    if removepunc == "on":
        for char in a:
            if char not in punctuation:
                analyzed = analyzed+char
    # analyze the text
    # return text and if not there then provide default value
        a=analyzed
        analyzed=""
    if uppercase == "on":
        analyzed = a
        analyzed = analyzed.upper()
        a=analyzed
        analyzed=""
    if spaceremover == "on":
        for i in range(0,len(a)):
            if a[i] == " " and a[i+1]==" ":
                continue
            else:
                analyzed=analyzed+a[i]

    analyzed=a
    params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
