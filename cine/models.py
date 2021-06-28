from django.db import models

class Person(models.Model):
    id = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = True, 
                  verbose_name ='ID')
    last_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    aliases=models.CharField(max_length=100)
    

class Movie(models.Model):
    id = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = True, 
                  verbose_name ='ID')
    title = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()
    casting = models.ManyToManyField(Person, related_name="movies_as_char")
    directors = models.ManyToManyField(Person, related_name="movies_as_dir")
    producers = models.ManyToManyField(Person, related_name="movies_as_prod")

    def __str__(self):
        return self.title
