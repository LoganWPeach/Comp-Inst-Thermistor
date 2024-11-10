from machine import Pin,ADC
import time
import math

adc=ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

filename = "values.txt"
with open(filename, "w", encoding="utf-8") as writeto:
        writeto.write("")

resistance = 1000 # Replace this value with whatever ohm resistance is known
maxvolts = 3.3 # Replace this value with the maximum voltage of the power supply

iterations = 0

led = Pin(23, Pin.OUT)
led.value(1)

target = int(input("What is the minimum resistance value in ohms?\n"))

while iterations < 241:
    iterations += 1
    adcValue = adc.read()
    voltage = adcValue/4095*3.3
    Rt = -1 * (resistance * voltage)/(voltage - maxvolts)
    passval = f"{voltage} Volts, {Rt} Ohms\n"
    print(passval);
    with open(filename, "a", encoding="utf-8") as writeto:
        writeto.write(passval)
    if Rt < target:
        led.value(1)
    else:
        led.value(0)
    
    time.sleep_ms(1000)

led.value(1)