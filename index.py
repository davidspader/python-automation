import pyautogui
import pyperclip
import time
import pandas

pyautogui.PAUSE = 0.5

pyautogui.click(x=958, y=1054)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://drive.google.com/drive/folders/1YlfO_VVBlaM4MYPnHUSbOG3JHGJ81CDp?usp=sharing")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=501, y=283)
pyautogui.click(x=603, y=702)

time.sleep(5)

tabela = pandas.read_csv(r"/home/david/Downloads/compras.csv", sep=";")
total = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total / quantidade

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=70, y=174)
pyautogui.write('davidspader97@gmail.com')
pyautogui.press('tab', presses=2)
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey("ctrl", "v")
pyautogui.press('tab')
text = f"""
Relatório de vendas:

Total gasto: R$ {total:,.2f}
Quantidade: {quantidade:,}
Preço médio: R$ {preco_medio:,.2f}

"""
pyperclip.copy(text)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")