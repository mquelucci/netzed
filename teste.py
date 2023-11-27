from varredura import varredura
import PySimpleGUI as sg

layout = [[sg.Input(key="-IP-")],
          [sg.Input(key="-PORT-")],
          [sg.Button("Testar",key="-TESTE-")],
          [sg.Multiline(auto_size_text=True,key="-SAIDA-")]]

janela = sg.Window("Teste",layout=layout)

while True:

    events, values = janela.read()

    if events == sg.WIN_CLOSED:
        break

    if events == "-TESTE-":
        rede = varredura(values["-IP-"],values["-PORT-"])
        rede.varrerTcpUdp(intensity="5",timeout="600")
        print(rede.getResult())
        #janela["-SAIDA-"].update(rede.getResult())

