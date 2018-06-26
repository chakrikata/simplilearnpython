from django.conf.urls import include, url
from django.contrib import admin
from store import views

urlpatterns = [

    url(r'^store/', views.store, name='store'),
    url(r'^$', views.store, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
]
