import requests
import re
from lxml import html
from rest_framework.authtoken.models import Token

from account.models import User
from django.conf import settings
from finance.models import Expenses
from .models import Config


def scan_qr_code(qr_string: str, user: User) -> Expenses:
    # TODO: нужно протестить
    t = re.findall(r't=(\w+)', qr_string)[0]
    s = re.findall(r's=(\w+)', qr_string)[0]
    fn = re.findall(r'fn=(\w+)', qr_string)[0]
    i = re.findall(r'i=(\w+)', qr_string)[0]
    fp = re.findall(r'fp=(\w+)', qr_string)[0]
    n = re.findall(r'n=(\w+)', qr_string)[0]

    url = "https://proverkacheka.com/api/v1/check/get"

    r = requests.post(url, data={
        "fn": fn,
        "fp": fp,
        "fd": i,
        "t": t,
        "s": s,
        "n": n,
        "token": Config.objects.get(key="qr_token").value
    })

    print(r.json())
    title = r.json().get('data').get("json").get("user")
    page = requests.get(url=f"https://mcc-codes.ru/search?q={title.replace(' ', '+')}")
    tree = html.fromstring(page.content)

    mcc_code = tree.xpath('//*[@id="points-search-table"]/tbody/tr[1]/td[1]/a')[0].text

    expenses = Expenses.objects.create(
        title=title,
        money=float(s),
        category=settings.MCC_CODES.get(mcc_code).get("Название", "Оплата товаров и услуг"),
        user=user
    )

    return expenses


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
