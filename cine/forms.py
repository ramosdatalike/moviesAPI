from django import forms
from cine.models import Movie, Person
from django.db import models

class PersonMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.last_name + ' ' + obj.first_name

class MovieMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'casting', 'directors', 'producers']
    
    casting = PersonMultipleChoiceField(Person.objects.all(), widget=forms.CheckboxSelectMultiple)
    directors = PersonMultipleChoiceField(Person.objects.all(), widget=forms.CheckboxSelectMultiple)
    producers = PersonMultipleChoiceField(Person.objects.all(), widget=forms.CheckboxSelectMultiple)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'aliases']