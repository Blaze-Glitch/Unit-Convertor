import PySimpleGUI as sg

TITLE = "Convertor"
layout = [
    [sg.Text("Choose Conversion"), sg.Spin(["km-mi", "kg-lb", "sec-min", "sec-hour", "min-hour", ], key = '-UNITS-')],
    [sg.Text("Value: "), sg.Input(key = '-VALUE-')],
    [sg.Button("Convert", key = '-CONVERT-'), sg.Button("Reverse Units", key = '-REVERSE-')],
    [sg.Text("Output: ") ,sg.Text("", key = '-OUTPUT-')]
]

window = sg.Window(TITLE, layout)

#Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    #Convert
    if event == '-CONVERT-' and values["-UNITS-"] == 'km-mi':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) * 0.6214)

    if event == '-CONVERT-' and values["-UNITS-"] == 'kg-lb':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) * 2.20462)

    if event == '-CONVERT-' and values["-UNITS-"] == 'sec-min':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) / 60)

    if event == '-CONVERT-' and values["-UNITS-"] == 'sec-hour':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) / 3600)

    if event == '-CONVERT-' and values["-UNITS-"] == 'min-hour':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) / 60)

    if event == '-CONVERT-' and values["-UNITS-"] == 'mi-km':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) / 0.6214)   

    if event == '-CONVERT-' and values["-UNITS-"] == 'lb-kg':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) / 2.20426)
    
    if event == '-CONVERT-' and values["-UNITS-"] == 'min-sec':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) * 60)

    if event == '-CONVERT-' and values["-UNITS-"] == 'hour-sec':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) * 3600)

    if event == '-CONVERT-' and values["-UNITS-"] == 'hour-min':
        input_value = values['-VALUE-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(float(values['-VALUE-']) * 60)            

    #Reverse Units
    if event == '-REVERSE-' and values['-UNITS-'] == 'km-mi':
        window['-UNITS-'].update('mi-km')
    elif event == '-REVERSE-' and values['-UNITS-'] == 'mi-km':
        window['-UNITS-'].update('km-mi')

    if event == '-REVERSE-' and values['-UNITS-'] == 'kg-lb':
        window['-UNITS-'].update('lb-kg')
    elif event == '-REVERSE-' and values['-UNITS-'] == 'lb-kg':
        window['-UNITS-'].update('kg-lb')

    if event == '-REVERSE-' and values['-UNITS-'] == 'sec-min':
        window['-UNITS-'].update('min-sec')
    elif event == '-REVERSE-' and values['-UNITS-'] == 'min-sec':
        window['-UNITS-'].update('sec-min')

    if event == '-REVERSE-' and values['-UNITS-'] == 'sec-hour':
        window['-UNITS-'].update('hour-sec')
    elif event == '-REVERSE-' and values['-UNITS-'] == 'hour-sec':
        window['-UNITS-'].update('sec-hour')

    if event == '-REVERSE-' and values['-UNITS-'] == 'min-hour':
        window['-UNITS-'].update('hour-min')
    elif event == '-REVERSE-' and values['-UNITS-'] == 'hour-min':
        window['-UNITS-'].update('min-hour')

window.close()