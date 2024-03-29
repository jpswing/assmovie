"""assmovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from movie.urls import movie_urls
from ticket.urls import ticket_urls
from coupon.urls import coupon_urls

from user.views import login, register

urlpatterns = [
    path('movies', include(movie_urls)),
    path('tickets', include(ticket_urls)),
    path('coupon', include(coupon_urls)),
    path('login', login),
    path('register', register),
]
