from django.conf.urls import url

from . import views
#from Fatturazione import viewsF

urlpatterns = [
    url('logout',views.Logout),
    url('login',views.Login),
    url('produttore',views.Produttore),
    url('articolo',views.Articolo),
    url('mp',views.MP),
    url('ma',views.MA),
    url('addart',views.AddArt),
    url('delart',views.DelArt),
    url('ricercaP',views.LKProduttore),
    url('ricercaA',views.LKPArticolo),
    url('ricercaM',views.LKPMargine),
    url('RCAM',views.LKPNomeMargine),
    url('fe',views.DelFornitore),
    url('logo',views.Logo),
    url('ppp',views.ImportTable),
    url('base',views.Base),
    url(r'^$',views.Login),
]