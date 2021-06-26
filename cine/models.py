from django.db import models
from django.db.models.fields import DateField


class Person(models.Model):
    id = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = True, 
                  verbose_name ='ID')
    last_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    aliases=models.CharField(max_length=100)
    
    @property
    def movies_as_character(self):
        return list(self.movies_as_char.all())
    @property
    def movies_as_director(self):
        return list(self.movies_as_dir.all())
    @property
    def movies_as_producer(self):
        return list(self.movies_as_prod.all())


class Movie(models.Model):
    id = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = True, 
                  verbose_name ='ID')
    title = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    casting = models.ManyToManyField(Person, related_name="movies_as_char")
    directors = models.ManyToManyField(Person, related_name="movies_as_dir")
    producers = models.ManyToManyField(Person, related_name="movies_as_prod")

    def __str__(self):
        return self.title

    @property
    def casting_list(self):
        return list(self.casting.all())
    @property
    def directors_list(self):
        return list(self.directors.all())
    @property
    def producers_list(self):
        return list(self.producers.all())