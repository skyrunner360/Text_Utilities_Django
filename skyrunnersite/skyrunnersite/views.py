#I have Created this File - Rishi
from django.http import HttpResponse
from django.shortcuts import render
#Navigation Page
def index(request):
    return render(request,'index2.html')
def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')


    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremover','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charcount = request.POST.get('charcount','off')
    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext=analyzed
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    if (newlineremove=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed= analyzed+char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        djtext=analyzed
    if (extraspaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext=analyzed
    if (charcount=="on"):
        analyzed = ""
        for char in djtext:
                analyzed = len(djtext)
        params = {'purpose': 'Number of characters are :', 'analyzed_text': analyzed}
    if (removepunc!="on" and fullcaps!="on" and newlineremove!="on" and extraspaceremove!="on" and charcount!= "on"):
        return HttpResponse("Please select an operation and try again")
    return render(request, 'analyze.html', params)