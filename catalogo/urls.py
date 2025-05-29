from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from motos import views as motos_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/signup/', motos_views.signup, name='signup'),

    path('home/', motos_views.motos, name='home'),

    # Redireciona root / → /home/
    path('', RedirectView.as_view(pattern_name='home', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
