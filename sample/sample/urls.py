"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.views.static import serve
from django.urls import path, include
from sampleapp import views
from sampleapp import urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',views.index , name='index'),
    path('contact',views.contact , name='contact'),
    path('FAQ',views.FAQ, name='FAQ'),
    path('mission', views.mission, name='mission'),
    path('services', views.services, name='services'),
    path('indexlog',views.indexlog , name='indexlog'),
    path('contactlog',views.contactlog , name='contactlog'),
    path('FAQlog',views.FAQlog, name='FAQlog'),
    path('missionlog', views.missionlog, name='missionlog'),
    path('serviceslog', views.serviceslog, name='serviceslog'),
    path('sign', views.sign, name='sign'),
    path('otp', views.otp, name='otp'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('campaign',views.campaign, name='campaign'),
    path('person',views.person,name='person'),
    path('index1',views.index1,name='index1'),
    path('upImages', views.upImages,name='upImages'),
    path('upFiles',views.upFiles,name='upFiles'),
    path('upCampaignFiles',views.upCampaignFiles,name='upCampaignFiles'),
    path('updatecampfiles',views.updatecampfiles,name='updatecampfiles'),
    path('updateimg',views.updateimg,name='updateimg'),
    path('updatefiles',views.updatefiles,name='updatefiles'),
    path('updateperson',views.updateperson,name='updateperson'),
    path('donate',views.donate,name='donate'),
]
handler404="sampleapp.views.handle_not_found"


if settings.DEBUG:
    urlpatterns= urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

