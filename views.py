from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_widok(request,*args,**kwargs):
	return render(request,'dom.html',{})

def kontakt(request,*args,**kwargs):
	kontekst = { 
		'moje_dane':'Oto moje dane',
		'nr_telefonu':'123456789',
		'moja_lista':[5,44,33,111],
	}
	return render(request,'kontakt.html',kontekst)

def wykonawcy(*args,**kwargs):
	return HttpResponse("<h1>wykonawcy nazwisko</h1>")