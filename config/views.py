from rest_framework.authtoken.models import Token

from account.models import User
from django.conf import settings
from finance.models import Expenses
from .models import Config


def init_user(request):
    """
        Получение пользователя по токену
    """
    user_id = Token.objects.get(key=request.headers.get("Authorization").replace("Token ", "")).user_id
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None


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
