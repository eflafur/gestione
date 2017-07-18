from django.db import models


class Genere(models.Model):
	nome=models.CharField(max_length=50)
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
	articolo=models.CharField(max_length=50)
	def __str__(self):
		return "%s" % (self.articolo)
	
class Produttore(models.Model):
	settore=models.ManyToManyField(Settore)
	regione=models.CharField(max_length=20,null=True)
	citta=models.CharField(max_length=20,null=True)
	azienda=models.CharField(max_length=50,unique=True)
	contatto=models.CharField(max_length=50)
	indirizzo=models.CharField(max_length=60,null=True)
	acquisizione=models.DateField(null=True)
	capacita=models.CharField(max_length=10,null=True)
	email=models.EmailField(null=True)
	tel=models.CharField(max_length=15,null=True)
	trpag=models.IntegerField(null=True)
	margine=models.IntegerField(null=True)
	fatturato=models.IntegerField(null=True)
	def __str__(self):
		return "%s %s %s %s" % (self.azienda,self.regione,self.contatto,self.citta)	
	
class Area(models.Model):
	regione=models.CharField(max_length=30)
	def __str__(self):
		return "%s" % (self.regione)	
	
class Sito(models.Model):
	area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
	citta=models.CharField(max_length=20,null=True)
	sigla=models.CharField(max_length=5,null=True)
	comune=models.CharField(max_length=30,null=True)
	def __str__(self):
		return "%s" % (self.citta)	








