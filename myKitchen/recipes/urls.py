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

from recipes.views import RecipeListView, RecipeCreateView, RecipeDetailView


urlpatterns = [
    url(
        regex=r'^$',
        view=RecipeListView.as_view(),
        name='recipe_list_api'
    ),
    url(
        regex=r'^create/$',
        view=RecipeCreateView.as_view(),
        name='recipe_create_api'
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/$',
        view=RecipeDetailView.as_view(),
        name='recipe_detail_api'
    )
]
