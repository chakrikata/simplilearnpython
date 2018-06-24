from django.conf.urls import include,url
from django.contrib import admin
from store import views

urlpatterns = [

    url(r'^store/', views.store, name='store'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^store/', include('store.urls'), name='store'),

]
