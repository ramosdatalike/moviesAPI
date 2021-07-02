from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie, Person
from .forms import MovieForm, PersonForm
from django.contrib.auth.mixins import LoginRequiredMixin
class MovieList(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

class MovieCreation(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('cine:list')
class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('cine:list')
class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirmdelete.html'
    success_url = reverse_lazy('cine:list')


#PersonForm

class PersonList(ListView):
    model = Person
    template_name = 'persons/person_list.html'

class PersonDetail(DetailView):
    model = Person
    template_name = 'persons/person_detail.html'

class PersonCreation(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'persons/person_form.html'
    success_url = reverse_lazy('cine:list_p')
class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'persons/person_form.html'
    success_url = reverse_lazy('cine:list_p')
class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'persons/person_confirmdelete.html'
    success_url = reverse_lazy('cine:list_p')

class Index(TemplateView):
    template_name = 'index.html'