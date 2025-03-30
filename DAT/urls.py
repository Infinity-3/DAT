"""
URL configuration for DAT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from tool import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools',views.tools,name='tools'),
    path('login', include('login.urls'), name='login'), 
    path('notes', include('notes.urls'), name='notes'),  
    path('', views.main, name='main'),  
    path('main', views.main, name='main'),
    path('redirect/<str:idpath>/', views.redirect, name='redirect'),  
    path('about', views.about, name='about'), 
    path('ronum',views.rom2num,name='ronum'),
    path('nurom',views.num2rom,name='nurom'),
    path('numbin',views.num2bin,name='numbin'),
    path('binnum',views.bin2num,name='binnum'),
    path('binchar',views.bin2char,name='binchar'),
    path('charbin',views.char2bin,name='charbin'),
    path('asciichar',views.ascii2char,name='asciichar'),
    path('charascii',views.char2ascii,name='charascii'),
    path('octdec',views.oct2dec,name='octdec'),
    path('decoct',views.dec2oct,name='decoct'),
    path('octbin',views.oct2bin,name='octbin'),
    path('octhex',views.oct2hex,name='octhex'),
    path('binoct',views.bin2oct,name='binoct'),
    path('binhex',views.bin2hex,name='binhex'),
    path('dechex',views.dec2hex,name='dechex'),    
    path('hexoct',views.hex2oct,name='hexoct'),    
    path('hexdec',views.hex2dec,name='hexdec'),
    path('hexbin',views.hex2bin,name='hexbin'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)