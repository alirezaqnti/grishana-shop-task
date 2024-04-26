from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewset, ProductViewset


router = DefaultRouter()
router.register("v1/categories", CategoryViewset, basename="CategoryViewset")
router.register("v1/products", ProductViewset, basename="ProductViewset")
urlpatterns = []
urlpatterns += router.urls
