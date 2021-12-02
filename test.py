from bipwallet.utils import *
import requests
from bit import PrivateKey, PrivateKeyTestnet


def gen_address(index):
    # Наша seed фраза
    # seed = 'vivid area able second bicycle advance demand alpha flip stable drift route'
    seed = 'second jealous still tree tongue pill october royal elder prison video mandate'

    # Мастер ключ из seed фразы
    master_key = HDPrivateKey.master_key_from_mnemonic(seed)

    # Public key из мастер ключа по пути 'm/44/0/0/0'
    root_keys = HDKey.from_path(master_key, "m/44'/0'/0'/0")[-1].public_key.to_b58check()

    # Extended public key
    xpublic_key = str(root_keys)

    # Адрес дочернего кошелька в зависимости от значения index
    address = Wallet.deserialize(xpublic_key, network='BTC').get_child(index, is_prime=False).to_address()

    rootkeys_wif = HDKey.from_path(master_key, f"m/44'/0'/0'/0/{index}")[-1]

    # Extended private key
    xprivatekey = str(rootkeys_wif.to_b58check())

    # Wallet import format
    wif = Wallet.deserialize(xprivatekey, network='BTC').export_to_wif()

    return address, str(wif)


print(gen_address(1))

wallet = "1j4kHXEZhBFVcQZBNddPhxB9nfQFoof7k"

url = f'https://blockchain.info/rawaddr/{wallet}'
x = requests.get(url)
wallet = x.json()

print('Итоговый баланс:' + str(wallet['final_balance']))
# print('Транзакции:' + str(wallet['txs']))
print(type(wallet['txs']))

if wallet['total_received'] == 0:
    print('баланс пустой')

wif = "KwrvP1BZs2qTnGWR3xJxLwkutm4zwaZbRtnbNRsbFu2VDDBknHN5"

# Приватный ключ из wif
# my_key = PrivateKey(wif=wif)
my_key = PrivateKeyTestnet(wif=wif)
test_key = PrivateKeyTestnet(wif="KxN6jvhrFuvtmLEBnwGyhRQYSV94uk6L6ZwcX8z5g2GJQaTR7QDs")

# Количество долларов перевода, можно поменять на btc
money = 0.1
print(test_key.get_balance())
# Кошелек куда будут переведены деньги
wallet = test_key.address

# Коммисия перевода, если поставить слишком маленькую, то транзакцию не примут
# И чем больше коммисия, тем быстрее пройдет перевод
fee = 5

# Генерация транзакции
tx_hash = my_key.create_transaction([(wallet, money, 'usd')], fee=fee, absolute_fee=True)
url = 'https://blockchain.info/pushtx'
r = requests.post(url, data={'tx': tx_hash})
print(r.text)
