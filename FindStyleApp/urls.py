"""
URL configuration for FindStyleApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from servicios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path ('signup/', views.signup, name='signup'),
    path ('servicios/', views.servicios, name='servicios'),
    path ('servicios/add/', views.add_servicios, name='add_servicios'),
    path('servicios/<int:servicio_id>/', views.servicio_detail, name='servicio_detail'), #va cambiando
    path('servicios/<int:servicio_id>/delete/', views.delete_servicio, name='delete_servicio'),
    path ('logout/', views.cerrarsesion, name='logout'),
    path('signin/', views.signin, name='signin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
