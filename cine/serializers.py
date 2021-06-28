from rest_framework import serializers
from . import models
from .models import Person, Movie
from .api_utils import int_to_Roman

class MovieRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ('id', 'title','release_year')

class PersonRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id', 'last_name','first_name')


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = ('id', 'last_name', 'first_name', 'aliases', 'movies_as_char', 'movies_as_dir', 'movies_as_prod')

class MovieSerializer(serializers.ModelSerializer):
    roman_year = serializers.SerializerMethodField('get_roman')

    def get_roman(self, obj):
        if obj.release_year:
            return int_to_Roman(self, obj.release_year)
        else:
            return ''
        
    class Meta:
        model = models.Movie
        fields = ('id', 'title','release_year','roman_year', 'casting', 'directors', 'producers')

