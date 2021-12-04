from bipwallet.utils import HDPrivateKey, HDKey, Wallet
import requests
from bit import PrivateKey
from django.conf import settings
from account.models import User
import qrcode


def create_qr(address: str):
    filename = f"btc{address}.png"
    img = qrcode.make(address)
    img.save(filename)
    return filename


def gen_address(index: int) -> list:
    """
      Генерация BTC кошелька
    """
    # TODO: настроить получение фразы из JSON файла
    seed = settings.BTC_SEED
    master_key = HDPrivateKey.master_key_from_mnemonic(seed)
    root_keys = HDKey.from_path(master_key, "m/44'/0'/0'/0")[-1].public_key.to_b58check()
    xpublic_key = str(root_keys)
    address = Wallet.deserialize(xpublic_key, network='BTC').get_child(index, is_prime=False).to_address()
    rootkeys_wif = HDKey.from_path(master_key, f"m/44'/0'/0'/0/{index}")[-1]
    xprivatekey = str(rootkeys_wif.to_b58check())
    wif = Wallet.deserialize(xprivatekey, network='BTC').export_to_wif()

    return [address, str(wif)]


def send_btc(user: User, amount: float, address: str):
    # TODO: разобраться с fee
    try:
        fee = 5
        key = PrivateKey(wif=user.wif)
        tx_hash = key.create_transaction([(address, amount, 'btc')], fee=fee, absolute_fee=True)
        url = 'https://blockchain.info/pushtx'
        requests.post(url, data={'tx': tx_hash})
        return "success"
    except Exception as e:
        return str(e)
