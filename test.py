# Файл для тестовых функций
import pyqiwi

token = "984765f1efad088e7b0a61d35afa20a9"

qiwi = pyqiwi.Wallet(token, number="79813514374", contract_info=True, auth_info=True, user_info=True)

# print(pyqiwi.generate_form_link("99", "79813514374", 1.1, comment="123"))
for item in qiwi.history().get('transactions'):
    if item.comment == "Да" and item.sum.amount >= 1.11:
        print(True)
