from machine import Pin, UART

uart = UART(0, 9600)

while True:
    if uart.any():
        perintah = uart.readline()
        print(perintah)
