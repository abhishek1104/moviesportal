from django.db import models

# Create your models here.

class heros(models.Model):
    name=models.CharField(max_length=100,blank=False)
    age=models.IntegerField(blank=False)

class heroens(models.Model):
    name=models.CharField(max_length=100,blank=False)
    age=models.IntegerField(blank=False)


class movies(models.Model):
    movie_geners = (
    ('Action', 'Action'),
    ('Animation', 'Animation'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Documentry', 'Documentry'),
    ('Family', 'Family'),    
    ('Horror', 'Horror'),    
    ('Comedy', 'Comedy'),)

    name=models.CharField(max_length=100,blank=False,null=False)
    heroes=models.ForeignKey(heros)
    heroens=models.ForeignKey(heroens)
    release_date = models.DateField()
    genere_choices = models.CharField(max_length=20,choices=movie_geners)
    def __unicode__ (self): # __str__() (Python 3)
        return self.name,self.release_date

