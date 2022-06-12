from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from news.api import NewsViewset
from syllabus.api import SyllabusViewSet
from notice.api import NoticeViewSet

router = DefaultRouter()
router.register('news', NewsViewset, basename='news')
router.register('syllabus', SyllabusViewSet, basename='syllabus')
router.register('notice', NoticeViewSet, basename='notice')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)