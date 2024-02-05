from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djforms(request):
    ENFO=NameForm()#empty name form object
    d={'ENFO':ENFO}
    if request.method=='POST':
        NFDO=NameForm(request.POST)#name form data object
        if NFDO.is_valid():
            #return HttpResponse(NFDO.cleaned_data)
            return HttpResponse(NFDO.cleaned_data['sname'])
        else:
            return HttpResponse('Data is not valid')

    
    return render(request,'djforms.html',d)