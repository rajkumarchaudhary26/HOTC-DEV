from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from home.api import HomeViewSet
from news.api import NewsViewset
from syllabus.api import SyllabusViewSet
from notice.api import NoticeViewSet, LatestNotice
from gallery.api import GalleryViewSet
from event.api import EventViewSet
from miscellaneous.api import MiscellaneousViewSet
from download.api import DownloadViewSet
from about.api import AboutViewSet
from board_members.api import BoardMembersViewSet
from organization_structure.api import OrganizationStructureViewSet
from contact.api import ContactViewSet
from home.api import HomeViewSet
from testimonial.api import TestimonialViewSet

router = DefaultRouter()
router.register('news', NewsViewset, basename='news')
router.register('syllabus', SyllabusViewSet, basename='syllabus')
router.register('notice', NoticeViewSet, basename='notice')
router.register('gallery', GalleryViewSet, basename='gallery')
router.register('event', EventViewSet, basename='event')
router.register('miscellaneous', MiscellaneousViewSet, basename='miscellaneous')
router.register('download', DownloadViewSet, basename='download')
router.register('about', AboutViewSet, basename='about')
router.register('board-members', BoardMembersViewSet, basename='board-members')
router.register('organization-structure', OrganizationStructureViewSet, basename='organization-structure')
router.register('contact', ContactViewSet, basename='contact')
router.register('home', HomeViewSet, basename='home')
router.register('testimonial', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notices/latest/', LatestNotice.as_view(), name='latest-notice'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)