from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CommandsView.as_view(), name='commands'),
    path('create/', views.CreateCommandView.as_view(), name='create_commands'),
    path('<id>/', views.InfoCommandView.as_view(), name='id'),
    path('player/<int:id>/', views.InfoPlayerView.as_view(), name='player'),
    path('capitan/<int:id>/', views.CreateCapitanView.as_view(), name='create_capitan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
