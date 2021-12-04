# Вид JSON-файла :
В корне проекта, нужно создать папку local и в нее закинуть config.json
```
{
    "secret_key": "123",
    "seed": "simple text",
    "db_type": "sqlite3 or psql",
    "database": "db_name",
    "user": "db_user",
    "host": "localhost",
    "password": "db_password",
    "port": "1234"
}

```
___
# Запуск проекта    
1)Установим необходимые библиотеки    
```pip install -r requirements.txt```    
2)Сделаем миграции    
```manage.py migrate```    
3)Создадим супер пользователя    
```manage.py createsuperuser```
