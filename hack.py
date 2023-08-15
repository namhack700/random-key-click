import pyautogui, random, time
import keyboard


print('tool auto combo:)')
print('injecting...')
time.sleep(1)
print('injected')
time.sleep(1)
print('1%')
print('25%')
print('50%')
print('60%')
print('75%')
print('100%')
print('')

time.sleep(1)
msg = input("Nhap key can spam: ").split("|")
n = int(input("Nhap so lan spam > "))
m = float(input("nhap so time delay: "))
print('can co key')
keysysinp=input('key >')

keycheck = open('dll injector.inp')
if keysysinp == keycheck:
    time.sleep(4)
    for i in range(n):
        key = (random.choice(msg))
        pyautogui.press(key)
        time.sleep(m)
