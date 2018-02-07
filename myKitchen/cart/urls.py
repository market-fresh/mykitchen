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

from cart.views import CartListView, CartDetailedView, ItemListView, ItemDetailedView

urlpatterns = [
    url(
        regex=r'^$',
        view=CartListView.as_view(),
        name='cart_list_api'
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/$',
        view=CartDetailedView.as_view(),
        name='cart_detail_api'
    ),
    url(
        regex=r'^item/$',
        view=ItemListView.as_view(),
        name='item_list_api'
    ),
    url(
        regex=r'^item/(?P<uuid>[-\w]+)/$',
        view=ItemDetailedView.as_view(),
        name='item_detail_api'
    )
]
