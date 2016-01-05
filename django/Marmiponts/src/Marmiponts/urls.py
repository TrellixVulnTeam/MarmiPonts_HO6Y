from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$','Home.views.home',name='home'),
	url(r'^about/$', 'Home.views.about', name='about'),
	url(r'^contact/$', 'Home.views.contact', name='contact'),

	url(r'^dashboard/$', 'Core.views.dashboard', name='dashboard'),
	url(r'^personalinfo/$','Core.views.personalinfo', name='personalinfo'),
	url(r'^ingredients/$','Core.views.ingredients', name='ingredients'),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
