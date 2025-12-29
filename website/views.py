
from django.shortcuts import render
def home(r): return render(r,'website/home.html')
def features(r): return render(r,'website/features.html')
def pricing(r): return render(r,'website/pricing.html')
def contact(r): return render(r,'website/contact.html')

#abas a serem criadas: inicio produtos planos blog contato empresa/atuacao