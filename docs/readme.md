## Запись в микроконтроллер 

Подключение по **COM** порту:

``` python
>>> ser = serial.Serial('COM3', 38400, timeout=0,
                     parity=serial.PARITY_EVEN, rtscts=1)
>>> s = ser.read(100)       # read up to one hundred bytes
                       # or as much is in the buffer
```

Создание и конфигурация порта:

``` python 
>>> ser = serial.Serial()
>>> ser.baudrate = 19200
>>> ser.port = 'COM1'
>>> ser
Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
>>> ser.open()
>>> ser.is_open
True
>>> ser.close()
>>> ser.is_open
False
```

Отправка бинарных строк по **COM** порту:

```python
with serial.Serial() as ser:
    ser.baudrate = 19200
    ser.port = 'COM1'
    ser.open()
    ser.write(b'hello')
```
Еще пару ссылок

https://stackoverflow.com/questions/20671412/using-pyserial-to-send-a-file


