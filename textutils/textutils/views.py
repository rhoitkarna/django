# Self Created
from codecs import charmap_build
from os import remove
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    dj_text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ''

        for char in dj_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
            
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif(fullcaps == 'on'):
        analyzed_text = dj_text.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif(newlineremover == 'on'):
        analyzed_text = ''
        for char in dj_text:
            if char != "\n":
                analyzed_text = analyzed_text + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == 'on'):
        analyzed_text = ''
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == " " and dj_text[index+1] == " "):
                analyzed_text = analyzed_text + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    elif(charcount == 'on'):
        count = 0
        for char in dj_text:
            if char != " ":
                count = count + 1
        params = {'purpose': 'Count Characters Without Spaces', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
