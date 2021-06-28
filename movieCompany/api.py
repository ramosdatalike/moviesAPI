from rest_framework import routers
from cine import api_views as cine_views

router = routers.DefaultRouter()
router.register(r'movies', cine_views.MovieViewset)
router.register(r'persons', cine_views.PersonViewset)

