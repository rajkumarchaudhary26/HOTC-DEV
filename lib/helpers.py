import re
import random
from django.template.defaultfilters import striptags
from django.utils import timezone


def today():
    return timezone.localdate()


def smart_truncate(content, length=158, suffix=' …'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix


# Also check model_utils package for alternate version
def get_excerpt(st):
    st = st.replace('&nbsp;', ' ')
    st = striptags(st)
    # Remove tabs
    st = st.replace('\t', '')
    # Combine white spaces
    st = re.sub(r'(\s)\1{1,}', r'\1', st.replace('\r\n', '\n'))
    return smart_truncate(st.strip())


def shuffle_dict(dct):
    l = list(dct.items())
    random.shuffle(l)
    return dict(l)

def merge_dicts(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(merge_dicts(dict1[k], dict2[k])))
            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield (k, dict2[k])
                # Alternatively, replace this with exception raiser to alert you of value conflicts
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])
