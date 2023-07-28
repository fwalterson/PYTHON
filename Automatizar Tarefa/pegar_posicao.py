import time
import pyautogui

# Espera 5 segundos depois vc coloca na posição do navegador 
# Onde vc quer colocar informação vai aparecer as cordenadas
# depois  copia essa posição por exemplo x=484,y403 e coloca
# no codigo pyautogui.click(x=685, y=451)
time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(200)