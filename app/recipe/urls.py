from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from app.recipe import views

router = DefaultRouter()

router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientsViewSet)

app_name = 'recipe'
urlpatterns = [
    url(r'^admin/', router.urls),

]