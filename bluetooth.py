#Diyprojectslab.com

from machine import Pin, UART

uart = UART(0, 9600)
led = Pin(16, Pin.OUT)

while True:
  if uart.any() > 0:
    data = uart.read().decode('utf-8').strip()
    print(data)
    if "on" in data:
      led.value(1)
      print('LED menyala \n')
      uart.write('LED menyala \n')
    elif "off" in data:
      led.value(0)
      print('LED mati \n')
      uart.write('LED mati \n')
