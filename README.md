## Загрузчик файлов в микроконтроллер

![Загрузчик файлов в микроконтроллер](docs/img.png)


Task:

1. [x] Конвертирование Intel hex в bin файл. `python`
2. [x] Отправка тестовых данных для проверки работы с портом 
3. [x] Выбор COM порта для прошивки. `python`
4. [x] Выбор битрейта для COM порта. `python`
5. [x] Возможность отправки как bin так и hex файла.
6. [x] Форма для удобной загрузки `PyQt5 python`
7. [x] Проверчная сумма для отправленного файла.
8. Чтение отправленных данных через COM порт
9. [x] Отправка команд для МК по COM порту
10. Проверка последнего прошитого файла с выбранным файлом (получение последней прошивки осуществляется через команду в COM порт, с COM порта приходит старая прошивка и сравнивается с выбранным bin файлом)
11. [x]  Список комманд на отправку в ком порт в виде выподающего меню
12. [x]  Добавление команд в меню ( или в список )
