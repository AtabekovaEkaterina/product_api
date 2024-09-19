# product_api
Небольшой API с применением DRF для создания продуктов. Принимает только 2 типа запросов:
- GET - просмотр общего списка продуктов (продукты отсортированы по названию)
- POST - создание нового проудкт.
<br>
Реализован механизм валидации полей (благодаря использованию DRF, большая часть валидации работает из под капота и не требует дополнительного кода: пустные поля, уникальность полей, все что описано на уровне моделей).
Проект доступен, как в форме API, так и в версии с интерфесом для обычного пользователя. Создана простая HTML-страница с формой для добавления нового продукта. Страница отображает таблицу с общим списком продуктов. При добавлении нового объекта, таблица автоматически обновляется.

# Технологии
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) Python 3.12<br>
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) Django 5.0<br>
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) HTML5<br>
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) JavaScript

# Инструкция по запуску
1. Клонируйте репозиторий 
```
git@github.com:AtabekovaEkaterina/product_api.git
```
2. Установите и активируйте виртуальное окружение
```
python3 -m venv venv
```
```
source venv/bin/activate
```
3. Обновите pip и установите зависимости
```
python3 -m pip install --upgrade pip
```
```
pip install -r backend/requirements.txt
```
4. В дирктории backend/product_api запустите Django-проект:
```
python3 manage.py runserver
```
5. Откройте в браузере файл frontend/index.html


# Примеры запросов
**GET получить общий список**<br>
`http://127.0.0.1:8000/api/v1/products/`
<details><summary>Response 200 удачное выполнение запроса</summary>
[<br>
    {<br>
        "id": 0,<br>
        "name": "string",<br>
        "description": string,<br>
        "price": 0,000<br>
    }<br>
    {<br>
        "id": 0,<br>
        "name": "string",<br>
        "description": string,<br>
        "price": 0.000,<br>
    }<br>
]
</details>

**POST добавление нового продукта**<br>
`http://127.0.0.1:8000/api/v1/products/`
<details><summary>Request</summary>
{<br>
    "name": "string",<br>
    "description": string,<br>
    "price": 0,000<br>
}<br>
</details>
<details><summary>Response 200 удачное выполнение запроса</summary>
{<br>
    "name": "string",<br>
    "description": string,<br>
    "price": 0,000<br>
}<br>
</details>
<details><summary>Response 400 нарушение уникальности поля name</summary>
{<br>
    "name":["Product named 1 already exists."]
}<br>
</details>

# Автор
Екатерина Атабекова
