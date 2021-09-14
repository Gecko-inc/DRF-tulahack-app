from .models import Config
import hashlib
import time
import random
import pyqiwi


def get_qiwi_url(user_token: str) -> str:
    """
      Generate url for pay
    """
    try:
        phone = Config.objects.get(key="qiwi_phone").value
        price = float(Config.objects.get(key="subscribe_price").value)
        url = pyqiwi.generate_form_link("99", phone, price, comment=user_token)

        return url + f"&comment={user_token}"
    except Config.DoesNotExist:
        return "config empty"


def check_qiwi_pay(user_token: str) -> bool:
    """
      Payment verification
    """
    try:
        token = Config.objects.get(key="qiwi_token").value
        phone = Config.objects.get(key="qiwi_phone").value
        price = float(Config.objects.get(key="subscribe_price").value)
        qiwi = pyqiwi.Wallet(token, number=phone, contract_info=True, auth_info=True, user_info=True)
        for item in qiwi.history().get('transactions'):
            if item.comment == user_token and item.sum.amount >= price:
                return True
    except Config.DoesNotExist:
        return False

    return False


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


def generate_token(unique_arg: str = "arg") -> str:
    """
      Generate unique token
    """
    return hashlib.md5(
            f'{unique_arg}{random.randint(0, 999)}{time.time()}{random.randint(1000, 9999)}'.encode('utf-8')
    ).hexdigest()[:121]
