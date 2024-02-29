# Home_Calendar
This is the service to work with calendar.

## Требования:

— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление
— модель данных "Событие": ID, Дата, Заголовок, Текст
— локальное хранилище данных
— максимальная длина заголовка — 30 символов
— максимальная длина поля Текст — 200 символов
— нельзя добавить больше одного события в день
— API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" (по аналогии с заметкой)

Написать и протестировать приложение, по аналогии с сервисом заметок из Воркшопа.



### Проверка
Проверяем функцию create и _from_raw (обработчик данных)
```python
curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "1|2020-02-02|The train|I remember it"
```
Проверяем функцию list
```python
curl http://127.0.0.1:5000/api/v1/note/ -X GET 
```


