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
from miscellaneous.api import MiscellaneousListViewSet, MiscellaneousDetailViewSet, DownloadViewSet
from page.api import PageViewSet
from general.api import BoardMembersViewSet, OrganizationStructureViewSet, ContactViewSet, TestimonialViewSet
from home.api import HomeViewSet
from menu.api import MenuViewSet

router = DefaultRouter()

router.register('news', NewsViewset, basename='news')
router.register('syllabus', SyllabusViewSet, basename='syllabus')
router.register('notice', NoticeViewSet, basename='notice')
router.register('gallery', GalleryViewSet, basename='gallery')
router.register('event', EventViewSet, basename='event')
router.register('miscellaneous-list', MiscellaneousListViewSet,
                basename='miscellaneous-list')
router.register('miscellaneous-detail', MiscellaneousDetailViewSet, basename='miscellaneous-detail')
router.register('download', DownloadViewSet, basename='download')
router.register('about', PageViewSet, basename='about')
router.register('board-members', BoardMembersViewSet, basename='board-members')
router.register('organization-structure',
                OrganizationStructureViewSet, basename='organization-structure')
router.register('contact', ContactViewSet, basename='contact')
router.register('home', HomeViewSet, basename='home')
router.register('testimonial', TestimonialViewSet, basename='testimonial')
router.register('menu', MenuViewSet, basename='menu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notices/latest/', LatestNotice.as_view(), name='latest-notice'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
