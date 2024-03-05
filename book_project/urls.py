from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('audio/', include('audio.urls')),
    path('video/', include('video.urls')),
    path('pravachan/', include('pravachan.urls')),
    path('vichar/', include('vichar.urls')),
    path('book/', include('book.urls')),
    path('privacy_policy/', include('privacy_policy.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
