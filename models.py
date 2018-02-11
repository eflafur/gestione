from django.db import models
from datetime import date,datetime


class Prodotto(models.Model):
	tipo=models.CharField(max_length=30)

class Pagamento(models.Model):
	tipo=models.CharField(max_length=30)
	giorni=models.IntegerField(default=0)

class Genere(models.Model):
	nome=models.CharField(max_length=50)
	iva=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	def __str__(self):
		return "%s" % (self.nome)

class Preferenza(models.Model):
	artic=models.CharField(max_length=20,null=True)
	margine=models.FloatField(max_length=20,null=True)
	fatturato=models.IntegerField()
	class Meta:
		unique_together = (('artic', 'margine'),)	

class Settore(models.Model):
	genere=models.ForeignKey(Genere,on_delete=models.CASCADE,null=True)
	articolo=models.CharField(max_length=50,null=True)
	def __str__(self):
		return "%s" % (self.articolo)

class Specifica(models.Model):
	settore=models.ManyToManyField(Settore)
	nome=models.CharField(max_length=30,unique=True,null=True,blank=True)
	def __str__(self):
		return "%s" % (self.nome)	

class Tipo(models.Model):
	nome=models.CharField(max_length=15)
	
class Produttore(models.Model):
	settore=models.ManyToManyField(Settore)
	regione=models.CharField(max_length=20,null=True)
	citta=models.CharField(max_length=50,null=True)
	azienda=models.CharField(max_length=50,unique=True,blank=True,default=" ")
	contatto=models.CharField(max_length=50,blank=True,default=" ")
	indirizzo=models.CharField(max_length=60,null=True,blank=True,default=" ")
	acquisizione=models.DateField(default=date.today)
	email=models.EmailField(null=True,blank=True)
	tel=models.CharField(max_length=15,null=True,blank=True,default=" ")
	trpag=models.IntegerField(null=True,blank=True,default=0)
	margine=models.IntegerField(null=True,blank=True,default=0)
	fatturato=models.IntegerField(null=True,blank=True,default=0)
	pi=models.CharField(max_length=11,default=" ")
	def __str__(self):
		return "%s %s %s %s" % (self.azienda,self.regione,self.contatto,self.citta)

class IDcod(models.Model):
	cod=models.CharField(max_length=60,null=True)
	genere=models.ForeignKey(Genere,on_delete=models.CASCADE,null=True)
	settore=models.ForeignKey(Settore,on_delete=models.CASCADE,null=True)
	specifica=models.ForeignKey(Specifica,on_delete=models.CASCADE,null=True)
	produttore=models.ForeignKey(Produttore,on_delete=models.CASCADE,null=True)
	tipo=models.ForeignKey(Tipo,on_delete=models.CASCADE,null=True)
	def __str__(self):
		return "%s" % (self.cod)	

class Area(models.Model):
	regione=models.CharField(max_length=30)
	def __str__(self):
		return "%s" % (self.regione)	

class Sito(models.Model):
	area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
	citta=models.CharField(max_length=50,null=True)
	sigla=models.CharField(max_length=5,null=True)
	comune=models.CharField(max_length=2,null=True)
	cap=models.CharField(max_length=6,null=True)
	def __str__(self):
		return "%s" % (self.citta)
	
class ExCsBl(models.Model):
	facc=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,default=0)
	trasporto=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	vari=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)	

class Carico(models.Model):
	idcod=models.ForeignKey(IDcod,on_delete=models.CASCADE,null=True)
	q=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	cassaexit=models.IntegerField(null=True,blank=True,default=0)
	cassa=models.IntegerField(null=True,blank=True,default=0)
	data=models.DateField(default=date.today)
	datafatt=models.DateField(default=date.today)
	bolla=models.CharField(max_length=20,null=True)
	costo=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=0)
	p=models.SmallIntegerField(default=0)
	cv=models.IntegerField(null=True,blank=True,default=0)
	mrg=models.SmallIntegerField(default=0)
	fattimp=models.DecimalField(max_digits=14,decimal_places=2,null=True,blank=True,default=0)
	fatt=models.CharField(max_length=10,null=True)
	pagato=models.BooleanField(default=0)
	note=models.TextField(max_length=30,default="")
	qn=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	tara=models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True,default=0)
	excsbl=models.ForeignKey(ExCsBl,on_delete=models.CASCADE,null=True)
	def __str__(self):
		return "%s" % (self.bolla)	
	
	
class Saldo(models.Model):
	idcod=models.ForeignKey(IDcod,on_delete=models.CASCADE,null=True)
	q=models.IntegerField(null=True,blank=True,default=0)
	data=models.DateField(default=date.today)	


#FATTURAZIONE

class Cliente(models.Model):
	regione=models.CharField(max_length=20,null=True)
	citta=models.CharField(max_length=50,null=True)
	azienda=models.CharField(max_length=50,unique=True,blank=True,default=" ")
	indirizzo=models.CharField(max_length=60,null=True,blank=True,default=" ")
	acquisizione=models.DateField(default=date.today,)
	email=models.EmailField(null=True,blank=True)
	tel=models.CharField(max_length=15,null=True,blank=True,default=" ")
	trpag=models.IntegerField(null=True,blank=True,default=0)
	pi=models.CharField(max_length=11,null=True,blank=True,default=" ")

class Scarico(models.Model):
	idcod=models.ForeignKey(IDcod,on_delete=models.CASCADE,null=True)
	cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
	q=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	cassa=models.IntegerField(null=True,blank=True,default=0)
	prezzo=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True,default=0)
	data=models.DateField(default=date.today)
	fattura=models.TextField(max_length=10,null=True,blank=True)
	lotto=models.CharField(max_length=50,null=True)
	iva=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	scadenza=models.DateField(default=date.today)	
	pagato=models.BooleanField(default=0)
	note=models.TextField(max_length=30,default="")
	tara=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	rs=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	rscassa=models.IntegerField(null=True,blank=True,default=0)

class Sospese(models.Model):
	idcod=models.ForeignKey(IDcod,on_delete=models.CASCADE,null=True)
	cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
	q=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	cassa=models.IntegerField(null=True,blank=True,default=0)
	prezzo=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True,default=0)
	data=models.DateField(default=date.today)
	fatturas=models.TextField(max_length=10,null=True,blank=True)
	lotto=models.CharField(max_length=20,null=True)
	tara=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	def __str__(self):
		return "%s" % (self.fatturas)
	
class trasporto(models.Model):
	idcod=models.ForeignKey(IDcod,on_delete=models.CASCADE,null=True)
	cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
	q=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	cassa=models.IntegerField(null=True,blank=True,default=0)
	prezzo=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True,default=0)
	data=models.DateField(default=date.today)
	ddt=models.TextField(max_length=10,null=True,blank=True)
	lotto=models.CharField(max_length=50,null=True)
	status=models.SmallIntegerField(default=0)
	tara=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	
class Tara(models.Model):
	cont=models.CharField(max_length=20,null=True)
	q=models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True,default=0)
	
class sp(models.Model):
	cod=models.CharField(max_length=20,null=True)
	attivo=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	passivo=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	
class ce(models.Model):
	cod=models.CharField(max_length=20,null=True)
	costi=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	ricavi=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)

class ivacliente(models.Model):
	dtreg=models.DateField(default=date.today)
	prot=models.IntegerField(null=True,blank=True,default=0)
	dtfatt=models.DateField(default=date.today)
	fatt=models.CharField(max_length=20,null=True)
	nome=models.CharField(max_length=20,null=True)
	iva=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	tot=models.DecimalField(max_digits=8,decimal_places=2,null=True)
	imp=models.DecimalField(max_digits=8,decimal_places=2,null=True)
	erario=models.DecimalField(max_digits=8,decimal_places=2,null=True)
	esenzione=models.CharField(max_length=20,null=True)
	saldo=models.DecimalField(max_digits=14,decimal_places=2,null=True,blank=True,default=0)
	
	
class contocln (models.Model):
	cod=models.CharField(max_length=2)
	sub=models.CharField(max_length=2)
	ssub=models.CharField(max_length=2,default="")
	dtreg=models.DateField(default=date.today)
	doc=models.CharField(max_length=20,null=True)
	dtdoc=models.DateField(default=date.today)
	dare=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	avere=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)	
	saldo=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	regis=models.CharField(max_length=60,null=True)
	cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
	
class contofrn (models.Model):
	cod=models.CharField(max_length=2)
	sub=models.CharField(max_length=2)
	ssub=models.CharField(max_length=2,default="")
	dtreg=models.DateField(default=date.today)
	doc=models.CharField(max_length=20,null=True)
	dtdoc=models.DateField(default=date.today)
	dare=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	avere=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)	
	saldo=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	regis=models.CharField(max_length=60,null=True)
	forn=models.ForeignKey(Produttore,on_delete=models.CASCADE,null=True)	
	
class contosp (models.Model):#(iva,banca,cassa,erario)
	cod=models.CharField(max_length=2)
	sub=models.CharField(max_length=2)
	ssub=models.CharField(max_length=2,default="")
	dtreg=models.DateField(default=date.today)
	doc=models.CharField(max_length=20,null=True)
	dtdoc=models.DateField(default=date.today)
	dare=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	avere=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)	
	regis=models.CharField(max_length=60,null=True)

class contoce (models.Model):#(cost,ricavi) 
	cod=models.CharField(max_length=2)
	sub=models.CharField(max_length=2)
	ssub=models.CharField(max_length=2,default="")
	dtreg=models.DateField(default=date.today)
	doc=models.CharField(max_length=20,null=True)
	dtdoc=models.DateField(default=date.today)
	dare=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	avere=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)	
	regis=models.CharField(max_length=60,null=True)
	
class ivaforn(models.Model):
	dtreg=models.DateField(default=date.today)
	prot=models.IntegerField(null=True,blank=True,default=0)
	dtfatt=models.DateField(default=date.today)
	fatt=models.CharField(max_length=20,null=True)
	nome=models.CharField(max_length=20,null=True)
	iva=models.DecimalField(max_digits=2,decimal_places=2,null=True,blank=True,default=0)
	tot=models.DecimalField(max_digits=8,decimal_places=2,null=True)
	imp=models.DecimalField(max_digits=8,decimal_places=2,null=True)
	erario=models.DecimalField(max_digits=8,decimal_places=2,null=True)
	esenzione=models.CharField(max_length=20,null=True)
	saldo=models.DecimalField(max_digits=14,decimal_places=2,null=True,blank=True,default=0)
	
class libro(models.Model):
	dtreg=models.DateField(default=date.today)
	prot=models.IntegerField(null=True,blank=True,default=0)
	doc=models.CharField(max_length=20,null=True)
	dtdoc=models.DateField(default=date.today)
	desc=models.CharField(max_length=60,null=True)
	conto=models.CharField(max_length=10,null=True)
	dare=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	avere=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True,default=0)
	
	
class saldocliente(models.Model):
	cliente=models.OneToOneField(Cliente,on_delete=models.CASCADE)
	attivo=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	passivo=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True,default=0)
	
class saldoprod(models.Model):
	prod=models.OneToOneField(Produttore,on_delete=models.CASCADE)
	attivo=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=0)
	passivo=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=0)
	
	
