from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.post_list,name="post_list"),
    path('hello/', views.hello,name='hello'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)