from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from loja.views import MotoListView, SignUpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('loja.urls')),
    path('home/', MotoListView.as_view(), name='home'),

    path('', RedirectView.as_view(pattern_name='home', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
