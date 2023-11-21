from django.contrib import admin
from django.urls import path, include
from ordain_app.views import default_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('ordain_app.urls')),
    path('',default_view,name="default_view" )
]
