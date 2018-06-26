from django.conf.urls import include, url
from django.contrib import admin
from store import views
from django.conf import settings
from django.conf.urls.static import static
from tastypie.api import Api
from store.api import ReviewResource
import debug_toolbar

v1_api = Api(api_name='v1')
v1_api.register(ReviewResource())

urlpatterns = [

    url(r'^store/', views.store, name='store'),
    url(r'^$', views.store, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^api/', include(v1_api.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
