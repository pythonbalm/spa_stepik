import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView
from spa import views
# from . import views

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('spa/img/favicon-16x16.png'))),
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('', views.home, name='home'),

    path('post/', views.post, name='post'),
    path('contacts/', views.contacts, name='contacts'),
    path('thanks/', views.thanks, name='thanks'),
    # path('new/', views.new_house, name='new_house'),
    path('new/', views.formset_view, name='new_house'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('search/', views.search, name='search'),
    path('house/<int:pk>/', views.ViewHouse.as_view(), name='house'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)