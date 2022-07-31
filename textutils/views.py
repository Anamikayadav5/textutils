from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("hello world")
# def about(request):
#     return HttpResponse('''<h1>Code with harry website</h1> <a href="https://www.google.com/search?q=code+with+harry&rlz=1C1CHBF_enIN966IN966&oq=code+with+harry&aqs=chrome..69i57j35i39j69i59j0i19l7.4581j0j7&sourceid=chrome&ie=UTF-8">Click on harry</a>''')
def index(request):
    return render(request,"index2.html")
    # return HttpResponse("Home")
def analyze(request):
    #get the text
    txt = request.POST.get('text','default')
    #check checkbox values
    removepunct=request.POST.get('removepunc','default')
    fullcaps=request.POST.get('fullcap','default')
    newlineremoves=request.POST.get('newlineremover','default')
    extraspaceremoves=request.POST.get('extraspaceremover','default')
    charcounters=request.POST.get('charcounter','default')


    #analyze the text
    if(removepunct=='on'):
     punctuations = ''';:()[]{}!'".,?/@#$%^&*_~`><'''
     analyzed = ""
     for char in txt:
         if char not in punctuations:
             analyzed+=char

     params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
     return render(request,'analyze.html',params)
    elif(fullcaps=='on'):
        analyzed =""
        for char in txt:
            analyzed+=char.upper()
        params = {'purpose': 'Convert to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremoves=='on'):
        analyzed=""
        for char in txt:
            if (char!="\n" and char!="\r"):
             analyzed += char
        params = {'purpose': 'Convert to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extraspaceremoves=='on'):
        analyzed = ""
        for char in txt:
            if(char!='  '):
               analyzed+=char
        params = {'purpose': 'Remove Extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(charcounters=='on'):
        analyzed = 0
        for i in txt:
            analyzed += 1
        params = {'purpose': 'Count characters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("Capitalize first")
# def newlineremove(request):
#     return HttpResponse("New line removed")
# def spaceremove(request):
#     return HttpResponse("Space Remove   <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("Char count")
