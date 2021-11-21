#!/usr/bin/python3

import PySimpleGUI as gui

font1 = 'Helvetica 60'
font2 = 'Helvetica 45'
font3 = 'Helvetica 30'
gui.theme('Dark Blue') 

# Window layout
layout = [  [ gui.Text('',size=(1,2), font = font2)],
            [gui.Text('km/h',size=(12,1),font=font1), gui.Text('Tilt',size=(12,1),font=font1)],
            [gui.Text('0',key='-SPEED-',size=(12,1),font=font1), gui.Text('0',key='-TILT-',size=(12,1),font=font1)],
            [ gui.Text('',size=(1,2))],
            [gui.Button('Start',button_color='Blue',size=(10,1), font=font3), gui.Button('Stop',button_color='Grey',disabled=True,size=(10,1), font=font3)] ]

# Create the Window
window = gui.Window('UBC Concrete Toboggan', layout,size=(800,480), text_justification='center',element_justification='center')
print('Concrete toboggan gui started')

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



