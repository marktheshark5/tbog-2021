#!/usr/bin/python3
import threading
import PySimpleGUI as gui
from temp_humi.temp_humi import aht20_interface

# definitions for sizes, these can be changed when we update the GUI to look nice
font1 = 'Helvetica 60'
font2 = 'Helvetica 45'
font3 = 'Helvetica 30'
font4 = 'Helvetica 15'
gui.theme('Dark Blue') 

# Window layout
layout = [  [ gui.Text('Temp (deg C):',size=(12,1),font=font4), gui.Text('-',key='-TEMP-',size=(12,1),font=font4), gui.Text('Humidity:',size=(12,1),font=font4), gui.Text('0',key='-HUMI-',size=(12,1),font=font4)],
            [ gui.Text('',size=(1,2), font = font2)],
            [gui.Text('km/h',size=(12,1),font=font1), gui.Text('Tilt',size=(12,1),font=font1)],
            [gui.Text('0',key='-SPEED-',size=(12,1),font=font1), gui.Text('-',key='-TILT-',size=(12,1),font=font1)],
            [ gui.Text('',size=(1,2))],
            [gui.Button('Start',button_color='Blue',size=(10,1), font=font3), gui.Button('Stop',button_color='Grey',disabled=True,size=(10,1), font=font3)] ]

# Create the Window
window = gui.Window('UBC Concrete Toboggan', layout,size=(1000,600), text_justification='center',element_justification='center', finalize = True) # expect size=(800,480)
print('Concrete toboggan gui started')

# create instances of sensor classes
aht20 = aht20_interface()

# functions for threaded updates
def temp_humi_update():
    # reads values from aht20 and updates the window
    values = aht20.read_values()
    temp_val = str(round(values['temp']))
    humi_val = str(round(values['humi']))
    window['-TEMP-'].update(temp_val)
    window['-HUMI-'].update(humi_val)
    # start a recursive thread that exits cleanly on program stop
    t = threading.Timer(0.5, temp_humi_update)
    t.daemon = True
    t.start()

# start the periodic update threads before entering the main loop
temp_humi_update()

# Event Loop to process "events" (run our thing)
while True:
    event, values = window.read()
    
    if event == 'Start':
        window['Start'].update(disabled=True, button_color='Grey')
        window['Stop'].update(disabled=False, button_color='Blue')
        # start continuous data measurement

    if event == 'Stop':
        window['Stop'].update(disabled=True, button_color='Grey')
        window['Start'].update(disabled=False, button_color='Blue')
        # stop continuous data measurement
        

    if event == gui.WIN_CLOSED: # if user closes window
        break

print("Exiting gui")
window.close()



