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

from users.views import UserListView, UserDetailView, UserAboutMeView, UserAddressView, UserMyRecipeView


urlpatterns = [
    url(
        regex=r'^$',
        view=UserListView.as_view(),
        name='user_list_api'
    ),
    url(
        regex=r'^(?P<pk>[-\w]+)/$',
        view=UserDetailView.as_view(),
        name='user_detail_api'
    ),
    url(
        regex=r'^aboutme/(?P<pk>[-\w]+)/$',
        view=UserAboutMeView.as_view(),
        name='user_aboutme_api'
    ),
    url(
        regex=r'^address/(?P<pk>[-\w]+)/$',
        view=UserAddressView.as_view(),
        name='user_address_api'
    ),
    url(
        regex=r'^recipes/(?P<pk>[-\w]+)/$',
        view=UserMyRecipeView.as_view(),
        name='user_recipe_api'
    )
]
