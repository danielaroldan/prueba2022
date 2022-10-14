from django.conf.urls import url,include
from veterinaria.views import principal

urlpatterns = [
    url(r'^$', principal),
]