# Home_Calendar
This is the service to work with calendar.

## Основные принципы.
1. Модель данных (События):
    - ID;
    - Дата;
    - Заголовок; 
    - Текст.


2. API интерфейс:
    - Добавление;
    - Список;
    - Чтение; 
    - Обновление;
    - Удаление.
   
Также были добавлены ограничения в виде максимальной длины заголвка (не более 30 символов), максимальной длины поля Текст (не более 200 символов) и нельзя добавлять больше одного события в день. Формат данных: "ГГГГ-ММ-ДД|заголовок|
текст".

### Установка программы 

1. Скачиваем (клонируем) репозиторий 
```python
git clone https://github.com/do-ordie/home_calendar.git
```
2. Запускаем виртуальное окружение
 ```python
source venv/bin/activate
```
4. Устанавливаем библиотеки
```python
pip install -r requirements.txt
```
5. Запускаем приложение
```python
python api.py
```


#### Тест curl:
Проверяем функцию create и _from_raw (обработчик данных)
```python
curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "1|2020-02-02|The train|I remember it"
```
Проверяем функцию list
```python
curl http://127.0.0.1:5000/api/v1/note/ -X GET 
```
Проверяем функцию read
```python
curl http://127.0.0.1:5000/api/v1/note/1/ -X GET 
```
Проверяем функцию update
```python
curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "1|2023-02-02|The train|I remember it" 
```
Проверяем функцию delate
```python
curl http://127.0.0.1:5000/api/v1/note/1/ -X DELET 
```
### Пример исполнения:
```python
$curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "1|2020-02-02|The train|I remember it"
$new id: 1

$curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "1|2020-02-02|The train|I remember it"
$new id: None

$curl http://127.0.0.1:5000/api/v1/note/ -X GET
$ 1|2020-02-02|The train|I remember it

$curl http://127.0.0.1:5000/api/v1/note/1/ -X GET
$ 1|2020-02-02|The train|I remember it

$curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "1|2023-02-01|The train|I 
remember it" 
$updated

$curl http://127.0.0.1:5000/api/v1/note/1/ -X DELET
$deleted


```