from .models import Config
import hashlib
import time
import random


def get_upload_to(instance, filename) -> str:
    """
      Returns the path to the media
    """
    try:
        return f'{instance.IMAGE_PATH}/{instance.id}/{filename}'
    except Exception:
        # TODO: Exception?
        return f'upload/{instance.id}/{filename}'


def common_context() -> dict:
    """
      Returns the context that is present on all pages
    """
    context = dict()
    context['cfg'] = Config.get_cfg()
    return context


def generate_token(unique_arg: str = None) -> str:
    """
      Generate unique token
    """
    return str(hashlib.md5(f'{unique_arg}{random.randint(0, 999)}{time.time()}{random.randint(1000, 9999)}'))
