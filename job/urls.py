from . import views
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()



router = DefaultRouter()
router.register("Jobs", JobViewSet, basename='jobs')
router.register("Blog", BlogViewSet, basename='blog')
router.register("Tags", TagViewSet, basename='tags')
router.register("ScholarShips", ScholarShipViewSet, basename='scholarships')
router.register("Companies", CompanyViewSet, basename='companies')
urlpatterns =  router.urls