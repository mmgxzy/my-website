from django.shortcuts import render
from apps.geeks.models import Index, About_us, Other, Zagolovok, Team, Сheck, Slaid, History, Denga
# Create your views here.

def index(request):
    about_all = About_us.objects.all()
    index = Index.objects.latest('id')
    other = Other.objects.all()
    zagolovok = Zagolovok.objects.all()
    uchastnik = Team.objects.all()
    chislo = Сheck.objects.all()
    slaid = Slaid.objects.all()
    bla = History.objects.all()
    denga = Denga.objects.all()
    return render(request, "index.html", locals())