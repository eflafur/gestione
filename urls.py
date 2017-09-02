from django.conf.urls import url

from . import views
from Magazzino import Mviews
from Fatturazione import Fviews
from Rimanenza import Rviews
urlpatterns = [
    url('logout',views.Logout),
    url('login',views.Login),
    url('produttore',views.Produttore),
    url('articolo',views.CreaArticolo),
    url('mp',views.ModProd),
    url('ma',views.DelArt),
    url('addart',views.AddCod),
#    url('delart',views.DelArtbyProd),
    url('ricercaP',views.LKProduttore),
    url('ricercaA',views.LKPArticolo),
    url('ricercaM',views.LKPMargine),
#    url('RCAM',views.LKPNomeMargine),
    url('fe',views.DelFornitore),
    url('logo',views.Logo),
#    url('ppp',views.ImportTable),
    url('base',views.Base),
    url(r'^$',views.Login),
    url('ioio',views.Graffo),
    
    
    #MAGAZZINO
    url('entrata',Mviews.CreaBolla),
    url('elimina',Mviews.EliminaBolla),
    url('lkfornitore',Mviews.LKCaricoFornitore),
    url('lkprodotto',Mviews.LKCaricoProdotto),
    url('lktotale',Mviews.LKCaricoTotale),
    url('gioco',Mviews.Gioco),

#    url('lkprodotto',Mviews.LKCaricoProdotto),

    #URL DI FATTURAZIONE
    url('lkftrcln',Fviews.LKFatturabyCliente),
    url('lkftr',Fviews.LKFattura),
    url('lksps',Fviews.SospesabyCliente),
    url('fattura',Fviews.Fattura),
    url('sospesa',Fviews.Sospesa),
    url('fatt',Fviews.FBase),
    url('ca',Fviews.CreaAnagrafica),
    url('delcliente',Fviews.DelCliente),
    url('modana',Fviews.ModificaAnagrafica),
    
    #URL DI RIMANENZA
    url('lkrgraph',Rviews.LKRGraph),
    url('rim',Rviews.RBase),
   
]