# I have creeted this file -AS

from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    #with open("file_one.txt") as f:
        #return HttpResponse(f.read())
    #return HttpResponse('''<a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'>Code with harry</a>''')    
    #return HttpResponse("Home Page !!!!")
    #params={'name':'Anjani','Planet':'Earth'}
    #return render(request,'index.html',params)
    return render(request,'index_1.html')


def analyze(request):
    #get the text 
    djtext=(request.GET.get('text','default'))
    
    #Check check box values
    Removepunc=(request.GET.get('removepunc','off'))
    Capatilized=(request.GET.get('capatilize','off'))
    allcaps = (request.GET.get('allcaps','off'))
    newlineremovechar= (request.GET.get('newlineremovechar','off'))  
    spaceremover= (request.GET.get('spaceremover','off'))  
    charcount=(request.GET.get('charcount','off')) 

    #Initilizing string variable
    analyzed=''
   
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    #analyze the text   

    #Removing Puncuation

    if Removepunc =="on":
        for _char in djtext:
            if _char not in punctuations:
                analyzed+=_char
        
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}     
        return render(request,'analyze.html',params)    
    
    #Converting text to upper case
    elif allcaps == 'on' :
        analyzed=''
        for _charcap in djtext:
            analyzed+=_charcap.upper()
        
        params={'purpose':'Changed to Upper Case','analyzed_text':analyzed}     
        return render(request,'analyze_1.html',params)       


    
    #Capatilizing the input string
    elif Capatilized=='on':
        djtext=djtext.capitalize()
        params={'purpose':'Capatilize','analyzed_text':djtext}     
        return render(request,'analyze_1.html',params)   

    #New Line character remover    
    elif newlineremovechar=='on':
        analyzed=''
        for _char in djtext:
            if _char !='\n':
                analyzed+=_char

        params={'purpose':'Remove New Line Character','analyzed_text':analyzed}     
        return render(request,'analyze_1.html',params)           

    #Space Remover

    elif spaceremover=='on':
        djtext=djtext.replace(" ","")

        params={'purpose':'Space Remover','analyzed_text':djtext}     
        return render(request,'analyze_1.html',params)   

    # Char count 
    
    elif charcount=='on':
        count=len(djtext)
        print(count)
        params={'purpose':'Character Count','analyzed_text':count}     
        return render(request,'analyze_1.html',params) 



    #Genreating Error Message if none of these check boc checked
    else:
        #analyzed='Error please check the check box'
        return HttpResponse("Error please check the check box")

        



"""
def about(request):
    return HttpResponse("This is about Page!!!! ")   

def removepunc(request):
    #get the text 
    djtext=(request.GET.get('text','default'))
    print(djtext)
    #analyze the text

    return HttpResponse("removepunc")

def capfirst(request):
    return HttpResponse('CapatilizeFirst')    

def newlineremove(request):
    return HttpResponse("NewLine Remove")

def spaceremove(request):
    return HttpResponse('''<a href='http://127.0.0.1:8000/'>Home Page</a>,<h1>Space Remover</h1> ''' ) 

def charcount(request):
    return HttpResponse("Charcount")

"""