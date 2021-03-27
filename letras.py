import PySimpleGUI as sg

def programa():
    sg.theme('DarkBrown1')
    estilo = [
        [sg.Text('--PROGRAMA QUE MOSTRA QUANTAS LETRA TEM UMA PALAVRA--')],
        [sg.Text('palavra', key='t'), sg.Input(key='a')],
        [sg.Text(size=(30, 2), key='renovar')],
        [sg.Button('mostrar'), sg.Button('sair')]
    ]
    janela = sg.Window('PROGRAMA QUE MOSTRA AS LETRA').layout(estilo)
    while True:
        e,v = janela.read()
        if e == sg.WINDOW_CLOSED or e == 'sair':
            break
        if e == 'mostrar':
            janela['renovar'].update('a palavra {} tem {} letras'.format(v['a'],len(v['a'])))

programa()