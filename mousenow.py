#! python3
import pyautogui
print('Control-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + str(pyautogui.screenshot().getpixel((x, y)))
        print(positionStr)

except KeyboardInterrupt:
    print('\nDone.')