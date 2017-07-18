from django.conf.urls import url

from . import views

urlpatterns = [
    #url('home',views.Home),
    url('produttore',views.Produttore),
    url('articolo',views.Articolo),
    url('mp',views.MP),
    url('ma',views.MA),
    url('ricercaP',views.LKProduttore),
    url('ricercaA',views.LKPArticolo),
    url('ricercaM',views.LKPMargine),
    url('fe',views.DelFornitore),
    url('logo',views.Logo),
    url('ppp',views.ImportTable),
    url(r'^$',views.Home),
]