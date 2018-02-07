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
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^home/', TemplateView.as_view(template_name="home.html")),
    url(r'^recipe_list/', TemplateView.as_view(template_name="recipe_list.html")),
    url(r'^recipe_create/', TemplateView.as_view(template_name="recipe_create.html")),
    url(r'^profile/', TemplateView.as_view(template_name="profile.html")),
    url(r'^profile_edit/', TemplateView.as_view(template_name="profile_main_edit.html")),
    url(r'^profile_address_edit/', TemplateView.as_view(template_name="profile_address_edit.html")),
    url(r'^profile_recipe_list/', TemplateView.as_view(template_name="profile_recipe_list.html")),
    url(r'^admin_app/', TemplateView.as_view(template_name="admin.html")),

    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls')),
    url(r'^category/', include('categories.urls')),
    url(r'^recipe/', include('recipes.urls')),
    url(r'^store/', include('stores.urls')),
    url(r'^subscriptions/', include('subscriptions.urls')),
    url(r'^user/', include('users.urls')),
    url('^', include('django.contrib.auth.urls'))

]
