from django.urls import path
from . import views 

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    path("", views.vpn, name="vpn-checks"),
    path("index", views.index, name="index"),
]