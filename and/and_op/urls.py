
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student/', views.student, name='student'),
    path('hello/', views.hello, name='hello'),
    # path('__debug__/', include('debug_toolbar.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    