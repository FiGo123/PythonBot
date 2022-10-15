import webbrowser
import pyautogui
from PIL import Image

url = 'https://chrome.google.com/webstore/detail/landscape-scroller/mafdngjdmflchchladjendpnoajdfcok?hl=en&authuser=3'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows

# Linux


webbrowser.get(chrome_path).open(url)

for x in range(30):
    print(x)
    pyautogui.sleep(3)

    add_btn = pyautogui.locateCenterOnScreen('prva.png', confidence=0.9)
    pyautogui.moveTo(add_btn.x / 2, add_btn.y / 2)  # move mouse to the window
    pyautogui.dragTo(add_btn.x / 2, add_btn.y / 2, button='left')  # focus the window
    pyautogui.click(add_btn.x / 2, add_btn.y / 2, button='left')

    pyautogui.sleep(2)

    confirm_btn = pyautogui.locateCenterOnScreen('druga.png', confidence=0.9)

    pyautogui.moveTo(confirm_btn.x / 2, confirm_btn.y / 2)  # move mouse to the window
    pyautogui.dragTo(confirm_btn.x / 2, confirm_btn.y / 2, button='left')  # focus the window
    pyautogui.click(confirm_btn.x / 2, confirm_btn.y / 2, button='left')

    pyautogui.sleep(2)

    all_ex_btn = pyautogui.locateCenterOnScreen('choose_ext.png', confidence=0.9)

    pyautogui.moveTo(all_ex_btn.x / 2, all_ex_btn.y / 2)  # move mouse to the window
    # focus the window
    pyautogui.click(all_ex_btn.x / 2, all_ex_btn.y / 2, button='left')

    pyautogui.sleep(2)

    helper_img = pyautogui.locateCenterOnScreen('peta.png', confidence=0.8)
    before_remove = pyautogui.locateAllOnScreen('sesta.png', confidence=0.9)

    if helper_img is None:
        print("noneJe")
        pyautogui.moveTo(all_ex_btn.x / 2, all_ex_btn.y / 2)  # move mouse to the window
        pyautogui.click(all_ex_btn.x / 2, all_ex_btn.y / 2, button='left')
        pyautogui.sleep(2)
        helper_img = pyautogui.locateCenterOnScreen('peta.png', confidence=0.9)
        before_remove = pyautogui.locateAllOnScreen('sesta.png', confidence=0.9)
        if helper_img is None:
            print("noneJe2")
            pyautogui.moveTo(all_ex_btn.x / 2, all_ex_btn.y / 2)  # move mouse to the window
            pyautogui.click(all_ex_btn.x / 2, all_ex_btn.y / 2, button='left')
            pyautogui.sleep(2)
            helper_img = pyautogui.locateCenterOnScreen('peta.png', confidence=0.9)
            before_remove = pyautogui.locateAllOnScreen('sesta.png', confidence=0.9)

    pyautogui.sleep(2)
    y = 0
    list = []
    list2 = []

    for i in before_remove:
        list.append(i.top / 2)
        list2.append(i.left / 2)

    x_axis = min(list2, key=lambda x: abs(x - helper_img.x / 2))
    y_axis = min(list, key=lambda x: abs(x - helper_img.y / 2))

    pyautogui.moveTo(x_axis, y_axis)  # move mouse to the window
    pyautogui.click(x_axis, y_axis, button='left')

    pyautogui.sleep(5)

    before_last_btn = pyautogui.locateCenterOnScreen('sedma.png', confidence=0.9)

    pyautogui.moveTo(before_last_btn.x / 2, before_last_btn.y / 2)  # move mouse to the window
    pyautogui.click(before_last_btn.x / 2, before_last_btn.y / 2, button='left')

    pyautogui.sleep(2)

    last_btn = pyautogui.locateCenterOnScreen('zadnja.png', confidence=0.9)

    pyautogui.moveTo(last_btn.x / 2, last_btn.y / 2)  # move mouse to the window
    pyautogui.click(last_btn.x / 2, last_btn.y / 2, button='left')

    pyautogui.sleep(2)

    choose_ext_btn = pyautogui.locateCenterOnScreen('choose_ext.png', confidence=0.9)
    pyautogui.moveTo(choose_ext_btn.x / 2, choose_ext_btn.y / 2)  # move mouse to the window
    pyautogui.click(choose_ext_btn.x / 2, choose_ext_btn.y / 2, button='left')

    pyautogui.sleep(2)

    vpn_ext_btn = pyautogui.locateCenterOnScreen('vpn_ext.png', confidence=0.9)
    pyautogui.moveTo(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2)  # move mouse to the window
    pyautogui.dragTo(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2, button='left')  # focus the window
    pyautogui.click(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2, button='left')

    pyautogui.sleep(2)

    if x == 0:
        print(x)
        turn_on_bright_data_btn = pyautogui.locateCenterOnScreen('turn_on_bright_data.png', confidence=0.9)

        pyautogui.moveTo(turn_on_bright_data_btn.x / 2, turn_on_bright_data_btn.y / 2)  # move mouse to the window
        pyautogui.click(turn_on_bright_data_btn.x / 2, turn_on_bright_data_btn.y / 2, button='left')
        pyautogui.sleep(2)
    else:
        vpn_ext_btn = pyautogui.locateCenterOnScreen('turn_of_bright_data.png', confidence=0.9)
        if vpn_ext_btn is None:
            choose_ext_btn = pyautogui.locateCenterOnScreen('choose_ext.png', confidence=0.9)
            pyautogui.moveTo(choose_ext_btn.x / 2, choose_ext_btn.y / 2)  # move mouse to the window
            pyautogui.click(choose_ext_btn.x / 2, choose_ext_btn.y / 2, button='left')

            pyautogui.sleep(2)

            vpn_ext_btn = pyautogui.locateCenterOnScreen('vpn_ext.png', confidence=0.9)
            pyautogui.moveTo(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2)  # move mouse to the window
            pyautogui.dragTo(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2, button='left')  # focus the window
            pyautogui.click(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2, button='left')

        pyautogui.moveTo(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2)  # move mouse to the window
        pyautogui.dragTo(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2, button='left')  # focus the window
        pyautogui.click(vpn_ext_btn.x / 2, vpn_ext_btn.y / 2, button='left')

        pyautogui.sleep(2)
        pyautogui.moveTo(turn_on_bright_data_btn.x / 2, turn_on_bright_data_btn.y / 2)  # move mouse to the window
        pyautogui.click(turn_on_bright_data_btn.x / 2, turn_on_bright_data_btn.y / 2, button='left')
        pyautogui.sleep(2)

        pyautogui.moveTo(turn_on_bright_data_btn.x / 2 - 100, turn_on_bright_data_btn.y / 2)  # move mouse to the window
        pyautogui.click(turn_on_bright_data_btn.x / 2 - 100, turn_on_bright_data_btn.y / 2, button='left')

    pyautogui.sleep(2)
    all_exit = pyautogui.locateAllOnScreen('exit.png', confidence=0.9)
    goodbye_page = pyautogui.locateCenterOnScreen('good_bye.png', confidence=0.8)

    listAllexitBtnsX = []
    listAllexitBtnsY = []
    for i in all_exit:
        listAllexitBtnsX.append(i.left / 2)
        listAllexitBtnsY.append(i.top / 2)

    x_axis_x_btn = min(listAllexitBtnsX, key=lambda x: abs(x - goodbye_page.x / 2 + 1000))
    y_axis_x_btn = min(listAllexitBtnsY, key=lambda x: abs(x - goodbye_page.y / 2))

    pyautogui.moveTo(x_axis_x_btn + 4, y_axis_x_btn + 2)  # move mouse to the window
    pyautogui.click(x_axis_x_btn + 4, y_axis_x_btn + 2, button='left')

    pyautogui.sleep(2)
    if x > 2:
        print("king")
        all_exit = pyautogui.locateAllOnScreen('exit.png', confidence=0.9)
        goodbye_page = pyautogui.locateCenterOnScreen('good_bye.png', confidence=0.8)

        listAllexitBtnsX = []
        listAllexitBtnsY = []
        for i in all_exit:
            listAllexitBtnsX.append(i.left / 2)
            listAllexitBtnsY.append(i.top / 2)

        x_axis_x_btn = min(listAllexitBtnsX, key=lambda x: abs(x - goodbye_page.x / 2 - 100))
        y_axis_x_btn = min(listAllexitBtnsY, key=lambda x: abs(x - goodbye_page.y / 2))

        pyautogui.moveTo(x_axis_x_btn + 4, y_axis_x_btn + 2)  # move mouse to the window
        pyautogui.click(x_axis_x_btn + 4, y_axis_x_btn + 2, button='left')

    pyautogui.sleep(2)

    before_history_three_dots_btn = pyautogui.locateCenterOnScreen('before_history_three_dots.png', confidence=0.9)
    pyautogui.moveTo(before_history_three_dots_btn.x / 2,
                     before_history_three_dots_btn.y / 2)  # move mouse to the window
    pyautogui.click(before_history_three_dots_btn.x / 2, before_history_three_dots_btn.y / 2, button='left')

    pyautogui.sleep(2)
    before_history_btn = pyautogui.locateCenterOnScreen('history_drag.png', confidence=0.8)
    pyautogui.moveTo(before_history_btn.x / 2,
                     before_history_btn.y / 2)  # move mouse to the window
    pyautogui.dragTo(before_history_btn.x / 2, before_history_btn.y / 2, button='left')
    pyautogui.sleep(2)
    pyautogui.moveTo(before_history_btn.x / 2 - 100,
                     before_history_btn.y / 2)
    pyautogui.sleep(2)# move mouse to the window
    pyautogui.dragTo(before_history_btn.x / 2 - 100, before_history_btn.y / 2, button='left')
    pyautogui.click(before_history_btn.x / 2 - 100, before_history_btn.y / 2, button='left')

    pyautogui.sleep(2)
    clear_browsing_data_btn = pyautogui.locateCenterOnScreen('clear_browsing_data_btn.png', confidence=0.7)
    pyautogui.moveTo(clear_browsing_data_btn.x / 2,
                     clear_browsing_data_btn.y / 2)  # move mouse to the window
    pyautogui.click(clear_browsing_data_btn.x / 2, clear_browsing_data_btn.y / 2, button='left')

    pyautogui.sleep(2)
    clear_data_btn = pyautogui.locateCenterOnScreen('clear_data_btn.png', confidence=0.8)
    pyautogui.moveTo(clear_data_btn.x / 2,
                     clear_data_btn.y / 2)  # move mouse to the window
    pyautogui.click(clear_data_btn.x / 2, clear_data_btn.y / 2, button='left')



    #

    all_exit = pyautogui.locateAllOnScreen('exit.png', confidence=0.9)
    goodbye_page = pyautogui.locateCenterOnScreen('good_bye.png', confidence=0.8)

    listAllexitBtnsX = []
    listAllexitBtnsY = []
    for i in all_exit:
        listAllexitBtnsX.append(i.left / 2)
        listAllexitBtnsY.append(i.top / 2)

    x_axis_x_btn = min(listAllexitBtnsX, key=lambda x: abs(x - goodbye_page.x / 2 + 1000))
    y_axis_x_btn = min(listAllexitBtnsY, key=lambda x: abs(x - goodbye_page.y / 2))

    pyautogui.moveTo(x_axis_x_btn + 4, y_axis_x_btn + 2)  # move mouse to the window
    pyautogui.click(x_axis_x_btn + 4, y_axis_x_btn + 2, button='left')

    pyautogui.sleep(2)
    if x > 2:

        print("king")
        all_exit = pyautogui.locateAllOnScreen('exit.png', confidence=0.9)
        goodbye_page = pyautogui.locateCenterOnScreen('good_bye.png', confidence=0.8)

        listAllexitBtnsX = []
        listAllexitBtnsY = []
        for i in all_exit:
            listAllexitBtnsX.append(i.left / 2)
            listAllexitBtnsY.append(i.top / 2)

        x_axis_x_btn = min(listAllexitBtnsX, key=lambda x: abs(x - goodbye_page.x / 2 - 100))
        y_axis_x_btn = min(listAllexitBtnsY, key=lambda x: abs(x - goodbye_page.y / 2))

        pyautogui.moveTo(x_axis_x_btn + 4, y_axis_x_btn + 2)  # move mouse to the window
        pyautogui.click(x_axis_x_btn + 4, y_axis_x_btn + 2, button='left')
    #

    webbrowser.get(chrome_path).open_new_tab(url)
