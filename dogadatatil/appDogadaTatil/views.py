from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    title ='Anasayfa'

    
    context = {
        "title":title
    }
    return render(request, 'index.html',context)

def karavan(request):
    
    title= 'Karavan'
    karavanlar = Karavanlar.objects.all()
    context = {
        "karavanlar": karavanlar,
        "title":title
    }
    return render(request,'karavan.html', context)

def detayKaravan(request,id):
    karavan = Karavanlar.objects.get(id = id)
    title_header = karavan.title
    comments = Comment.objects.filter(karavan_category=karavan)

    if request.method == "POST":
        name2 = request.POST["name"]
        title2 = request.POST["title"]
        text2 = request.POST["text"]

        comment = Comment(name=name2, title=title2, text=text2, karavan_category=karavan)
        comment.save()
        return redirect("/karavan/"+ id)
    context={
        "karavan": karavan,
        "title":title_header,
        "comments":comments,
    }
    return render(request, 'detaykaravan.html',context)

def bungalov(request):
    title = 'Bungalov'
    bungalov = Bungalov.objects.all()
    context = {
        "bungalov": bungalov,
        "title":title
    }
    return render(request,'bungalov.html', context)

def detayBungalov(request, id):
    detBungalov = Bungalov.objects.get(id = id)
    title = detBungalov.title
    context ={
        "detBungalov": detBungalov,
        "title": title
    }
    return render(request, 'detaybungalov.html', context)

def tents(request):
    title = "Çadır"
    tents = Tent.objects.all()
    context ={
        "tents":tents,
        "title": title
    }
    return render(request, 'tents.html',context)

def detailTent(request,id):
    detail_tent = Tent.objects.get(id = id)
    title = detail_tent.title
    context ={
        "detail_tent":detail_tent,
        "title":title
    }
    return render(request,'detailtent.html',context)


#USER Login
def loginUser(request):
    context ={}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password) #authenticate ile kontrol yapılıyor(databasede olup olmadığı).. Eğer yoksa değeri None döner..
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            context.update({"hata":"kullanıcı adı veya şifre yanlış"})

    return render(request, 'login.html', context)

#User Logout
def logoutUser(request):

    logout(request)
    return redirect('index')

#User Register
def registerUser(request):
    context ={}
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if not User.objects.filter(username=username).exists(): # exist --> eğer kullanıcı varsa true gönderiyor. Bu nedenle yoksa anlamında olması için not operatörü kullanıldı.
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('loginUser')
            else:
                context.update({"hata":"kullanıcı adı daha önce alınmış"})
        else:
            context.update({"hata":"Lütfen 2. parolayı tekrar kontrol edin."})

    return render(request,'register.html', context)

    
class SearchBar(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("ara")
        context_data = super().get_context_data(**kwargs)
        context_data["queryset1"] = Karavanlar.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
        context_data["queryset2"] = Bungalov.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
        context_data["queryset3"] = Tent.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
        
        print(context_data)
        return context_data 
