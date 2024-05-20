import cv2
import numpy as np
import pyautogui as pg

screenshot = pg.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
img = cv2.imread("img/c_mercado.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
limite = pg.locateOnScreen(img_cinza, confidence=0.7)
centro = pg.center(limite)

print(limite)
pg.moveTo(centro.x, centro.y)
cv2.imshow('Screenshot', screenshot)

