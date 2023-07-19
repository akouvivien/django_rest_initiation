from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from crudProjet_api.views import AuthorViewSet,BookViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
