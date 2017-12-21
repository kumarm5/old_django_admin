from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
