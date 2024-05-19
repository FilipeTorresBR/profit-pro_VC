import cv2
import numpy as np
import pyautogui as pg

screenshot = pg.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
img = cv2.imread("img/c_limite2.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
limite = pg.locateOnScreen(img, confidence=0.5)
#cv2.rectangle(
#    screenshot,
#    (limite.left, limite.top),
#    (limite.left + limite.width, limite.top + limite.height),
#    (0, 0, 255),
#    2
#)
print(limite)
pg.moveTo(limite)
cv2.imshow('Screenshot', screenshot)

cv2.waitKey(0)