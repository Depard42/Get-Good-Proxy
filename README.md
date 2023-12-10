# Парсер proxy c https://free-proxy-list.net/

## Установка зависимостей и запуск
```bash
$ pip3 install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Запуск 
```bash
$ source venv/bin/activate
$ python3 main.py
``` 
Список прокси сохраниться в файл 'proxy.json' в директории проекта.

## Как библиотека
```
from get_proxy.main import get_proxy

proxy = get_proxy()
```

## Формат вывода
```
[
    {
        "ip": "190.1.11.111",
        "port": "80",
        "code": "AR",
        "country": "Argentina",
        "anonimity": "anonymous",
        "google": "",
        "https": "yes",
        "checked": "9 secs ago"
    },
    ...
]
```