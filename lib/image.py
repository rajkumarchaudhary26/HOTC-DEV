from html.parser import HTMLParser

from django.conf import settings
from django.db.models import Model
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def warm(instance):
    if hasattr(instance, 'SIZES') and type(instance.SIZES) == dict:
        for field, set in instance.SIZES.items():
            if getattr(instance, field):
                for key, value in set.items():
                    warmer = VersatileImageFieldWarmer(
                        instance_or_queryset=instance,
                        rendition_key_set=[(key, value)],
                        image_attr=field
                    )
                    try:
                        warmer.warm()
                    except AttributeError:
                        pass


def warm_bulk(queryset):
    if hasattr(queryset.model, 'SIZES'):
        SIZES = queryset.model.SIZES
        if type(SIZES) == dict:
            for field, set in SIZES.items():

                for key, value in set.items():
                    warmer = VersatileImageFieldWarmer(
                        instance_or_queryset=queryset,
                        rendition_key_set=[(key, value)],
                        image_attr=field
                    )
                    try:
                        warmer.warm()
                    except AttributeError:
                        pass


class FirstImageParser(HTMLParser):
    first_image = None

    def handle_starttag(self, tag, attrs):
        if tag == 'img' and not self.first_image:
            for attr in attrs:
                if attr[0] == 'src':
                    self.first_image = attr[1]
                    # break


def get_first_image(markup):
    parser = FirstImageParser()
    parser.feed(markup)
    return parser.first_image


def save_thumbnail(instance: Model, *args, **kwargs):
    original = instance.thumbnail if instance.thumbnail else None
    post_save = False

    header_image = kwargs.pop('header_image', None)
    if not header_image:
        if hasattr(instance, 'header_image'):
            header_image = instance.header_image
        elif hasattr(instance, 'header_photo'):
            header_image = instance.header_photo

    if header_image:
        instance.thumbnail = header_image
        if not original or instance.thumbnail != original:
            post_save = True
    else:
        if hasattr(instance, 'description'):
            content = instance.description
        elif hasattr(instance, 'content'):
            content = instance.content
        else:
            raise AttributeError('Content attribute could not be detected!')

        first_image = get_first_image(content)
        if first_image:
            valid_media_prefixes = []
            if hasattr(settings, 'MEDIA_URL'):
                valid_media_prefixes.append(settings.MEDIA_URL)
                if not settings.MEDIA_URL.startswith('http') and hasattr(settings, 'BACKEND_URL'):
                    valid_media_prefixes.append('{}{}'.format(settings.BACKEND_URL, settings.MEDIA_URL))
            # TODO Generated media file url isn't absolute
            if hasattr(settings, 'ADDITIONAL_MEDIA_URLS'):
                valid_media_prefixes.extend(settings.ADDITIONAL_MEDIA_URLS)

            if first_image.startswith(tuple(valid_media_prefixes)):
                instance.thumbnail = first_image.split(settings.MEDIA_URL)[-1]
                if not original or instance.thumbnail != original.url:
                    post_save = True
            elif instance.thumbnail:
                instance.thumbnail = None
                post_save = True
        elif instance.thumbnail:
            instance.thumbnail = None
            post_save = True
    if post_save:
        if kwargs.get('force_insert'):
            kwargs['force_insert'] = False
        super(instance.__class__, instance).save(*args, **kwargs)
