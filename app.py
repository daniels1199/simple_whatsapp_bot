import webbrowser
from time import sleep
from urllib.parse import quote
import pyautogui

def auto_send():
    
    msg = quote('Type your message here.')
    
    #Change the phone number in URL link bellow   
    url = f"https://web.whatsapp.com/send?phone='xxxxxxxxx'&text={msg}" 
    
    webbrowser.open_new_tab(url)
    sleep(15)
    click_coords = pyautogui.locateCenterOnScreen('send_button.png')
    pyautogui.click(click_coords[0], click_coords[1])
    sleep(1)
    pyautogui.hotkey('ctrl','w')    

if __name__ == '__main__':    
    try:
        auto_send()
        print("SUCESS!")
    except Exception as err:
        print(f"[ERROR]: {err=}")