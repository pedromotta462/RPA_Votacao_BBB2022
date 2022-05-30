'''
Automatizar o processo de votação na eliminação do BBB22
Pré-requisitos: Ter o navegador Edge instalado, estar logado na sua conta da globo no site do gshow
'''

import pyautogui
import time

def vota(op):
    pyautogui.press('down', presses=8)
    time.sleep(3)
    if op == 1:
        pyautogui.moveTo(564,217)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(6)
        pyautogui.moveTo(552,355)
        time.sleep(2)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(10)
        pyautogui.press('up', presses=5)
        time.sleep(1)
        pyautogui.moveTo(628,427)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(5)
        
    if op == 2:
        pyautogui.moveTo(596,349)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(6)
        pyautogui.moveTo(552,370)
        time.sleep(2)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(10)
        pyautogui.press('up', presses=5)
        time.sleep(1)
        pyautogui.moveTo(628,427)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(5)

    if op == 3:
        pyautogui.moveTo(617,481)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(6)
        pyautogui.moveTo(553,373)
        time.sleep(2)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(10)
        pyautogui.press('up', presses=5)
        time.sleep(1)
        pyautogui.moveTo(628,427)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(5)

a = False
while a==False:
    op = int(input('Qual opção você quer votar?Digite 1, 2 ou 3: '))
    if op == 1 or op == 2 or op == 3:
        x = int(input('Agora digite quantas vezes você quer votar nessa opção: '))
        a = True
    else:    
        print('Opção inválida digite novamente!') 


pyautogui.alert("O código vai começar, quando clicar no 'ok', não toque no teclado nem no mouse durante a execução do código")
pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('Edge')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.write('https://gshow.globo.com/realities/bbb/bbb22/votacao/paredao-bbb22-vote-para-eliminar-gustavo-pedro-scooby-ou-vinicius-46bd16d5-60b3-40db-85ee-8d6cf784150a.ghtml')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)

aux = 0
while aux < x:
    vota(op)
    aux +=1
    
time.sleep(2)
pyautogui.alert("O código terminou de rodar")
 