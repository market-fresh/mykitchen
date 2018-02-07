"""myKitchen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from subscriptions.views import FeaturedRecipesListView, FeaturedRecipesCreateView, LikesView, ViewsView, LikesDetailView, ViewsDetailView

urlpatterns = [
    url(
        regex=r'^featured/$',
        view=FeaturedRecipesListView.as_view(),
        name='featured_api'
    ),
    url(
        regex=r'^featured/create/$',
        view=FeaturedRecipesCreateView.as_view(),
        name='create_featured_api'
    ),
    url(
        regex=r'^likes/$',
        view=LikesView.as_view(),
        name='likes_api'
    ),
    url(
        regex=r'^views/$',
        view=ViewsView.as_view(),
        name='views_api'
    ),
    url(
        regex=r'^likes/(?P<uuid>[-\w]+)/$',
        view=LikesDetailView.as_view(),
        name='likes_api'
    ),
    url(
        regex=r'^views/(?P<uuid>[-\w]+)/$',
        view=ViewsDetailView.as_view(),
        name='views_api'
    )
]
