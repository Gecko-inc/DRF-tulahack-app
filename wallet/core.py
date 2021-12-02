from bipwallet.utils import HDPrivateKey, HDKey, Wallet
import requests
from bit import PrivateKey

from account.models import User


def gen_address(index: int) -> list:
    """
      Генерация BTC кошелька
    """
    # TODO: настроить получение фразы из JSON файла
    seed = 'just text'
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
    fee = 5
    my_key = PrivateKey(wif=user.wif)
    tx_hash = my_key.create_transaction([(address, float, 'btc')], fee=fee, absolute_fee=True)
    url = 'https://blockchain.info/pushtx'
    requests.post(url, data={'tx': tx_hash})
