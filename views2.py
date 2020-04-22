from django.shortcuts import render
from .models import Produkt
from .fields import ProduktForm

# Create your views here.
def produkt_widok(request):
		form = ProduktForm(request.POST or None)
		if form.is_valid():
			form.save()
		context = {
			'form':form
		}
		return render(request,"produkty/prodkt_utworz.html",context)

def produkt_opis(request):
	obj=Produkt.objects.get(id=1)
	return render(request,'produkt/opis.html',{})