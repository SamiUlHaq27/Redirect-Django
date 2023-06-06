from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ads.models  import Article
from movie.models import Link
import random

def index(request):
    # ------------------------------------------------------------------------------------------
    art = Article.objects.all().order_by("id")
    tot_arts = len(art)
    if tot_arts>2:
        recent_art = [art[tot_arts-1],art[tot_arts-2],art[tot_arts-3]]
    else:
        recent_art = []
    pageNo = request.GET.get("page")
    paginated = Paginator(art,per_page=7)
    tot_pag = paginated.num_pages
    list_page = [i for i in range(1,tot_pag+1)]
    page1 = paginated.get_page(pageNo)
    # ------------------------------------------------------------------------------------------
    ran = random.randint(0,tot_arts-1)
    ran = art[ran]
    # ------------------------------------------------------------------------------------------
    try:
        obj = Link.objects.get(movie_id=request.session["movieId"])
        btn = True
    except:
        btn = False
    return render(request, 'index.html',{
        'DisplayTopButton': btn,
        "DisplayBottomButton":False,
        "random":ran,
        "page_no":list_page,
        "articles":page1,
        "recent_articles":recent_art,
        })

def indexId(request, id):
    request.session["movieId"] = id
    return redirect("index")

def single(request, tit):
    # ------------------------------------------------------------------------------------------
    art = Article.objects.all().order_by("id")
    tot_arts = len(art)
    if tot_arts>2:
        recent_art = [art[tot_arts-1],art[tot_arts-2],art[tot_arts-3]]
    else:
        recent_art = []
    btn = False
    if "movieId" in request.session:
        btn = True
    # ------------------------------------------------------------------------------------------
    art = (Article.objects.filter(title=tit))[0]
    also_like = random.choices(Article.objects.all(),k=2)
    return render(request, 'single.html',{
        'DisplayTopButton': btn,
        "DisplayBottomButton":btn,
        "recent_articles":recent_art,
        "article":art,
        "also_articles":also_like
        })

def download(request):
    link = (Link.objects.get(movie_id=request.session["movieId"])).target_link
    del request.session["movieId"]
    return redirect(link)

def category(request, cat):
    # ------------------------------------------------------------------------------------------
    art = Article.objects.all().order_by("id")
    tot_arts = len(art)
    if tot_arts>2:
        recent_art = [art[tot_arts-1],art[tot_arts-2],art[tot_arts-3]]
    else:
        recent_art = []
    return render(request, 'category.html',{'DisplayTopButtons': False,"DisplayBottomButton":False,"recent_articles":recent_art})

def contact(request):
    # ------------------------------------------------------------------------------------------
    art = Article.objects.all().order_by("id")
    tot_arts = len(art)
    if tot_arts>2:
        recent_art = [art[tot_arts-1],art[tot_arts-2],art[tot_arts-3]]
    else:
        recent_art = []
    return render(request, 'contact.html',{'DisplayTopButtons': False,"DisplayBottomButton":False,"recent_articles":recent_art})


