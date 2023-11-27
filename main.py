#=============================================================================================================================================================================
#=============================================================================================================================================================================
#=============================================================================================================================================================================
# IMPORTAÇÃO
import PySimpleGUI as sg
import os
import webbrowser
import dialogBox
from gui import gui
from validate import *
from configuracoes import configuracoes
from varredura import varredura

#=============================================================================================================================================================================
#=============================================================================================================================================================================
#=============================================================================================================================================================================
#FUNÇÕES
    
#Função de boas vindas
def welcome():

    # VERIFICA SE A IMAGEM DO NETZED ESTÁ NA PASTA DO NETZED
    if os.path.isfile("./netzed.png"):
        
        layout=[[sg.Frame("", layout=[[sg.Text("NETZED", justification='center', font=("Roboto", 14))],
                                      [sg.Image(key="-IMAGE-", filename="./netzed.png")],
                                      [sg.Text("DESENVOLVIDO POR MATHEUS QUELUCCI", justification='center', font=("Roboto", 14))]], 
                element_justification="center", pad=(0, 0), border_width=0)]]
        
        welcomeWindow = sg.Window("",no_titlebar=True, 
                                    auto_close=True, 
                                    auto_close_duration=2,
                                    layout=layout,
                                    icon="./netzed.ico")
        welcomeWindow.read()
        welcomeWindow.close()

    else:
        layout=layout=[[sg.Frame("", layout=[[sg.Text("NETZED", justification='center', font=("Roboto", 14))],
                                             [sg.Text("DESENVOLVIDO POR MATHEUS QUELUCCI", justification='center', font=("Roboto", 14))]], 
                        element_justification="center", pad=(0, 0), border_width=0)]]

        welcomeWindow = sg.Window("",no_titlebar=True, 
                                    auto_close=True,
                                    auto_close_duration=2,
                                    layout=layout,
                                    icon="./netzed.ico")
        welcomeWindow.read()
        welcomeWindow.close()

#Atualização do resumo pós-varredura
def AtualizaResumo(analisador,janela):

    #Varredura
    janela["Lbl-InicioVarredura"].update(analisador.lastSweepStartTime)
    janela["Lbl-FimVarredura"].update(analisador.lastSweepEndTime)
    janela["Lbl-StatusVarredura"].update(analisador.lastSweepStatus)
    janela["Lbl-TipoVarredura"].update(analisador.lastSweepType)
    #Exportação
    janela["Lbl-HorarioExportacao"].update(analisador.lastExportTime)
    janela["Lbl-NomeExportacao"].update(analisador.lastExportName)
    janela["Lbl-StatusExportacao"].update(analisador.lastExportStatus)
    #Log
    janela["Mtl_Saida"].update(analisador.ResultadoCompletoJson())

    return

#Função principal
def main():

    layout=[[gui().version, gui().Btn_Suporte, gui().Btn_Forum],
            [gui().build()]]

    window = sg.Window("NETZED",layout=layout,icon="./netzed.ico")

    analisador = None

    while True:

        events, values = window.read()

        if events == sg.WIN_CLOSED:
            break
        
        #Se o IP for de um host, define a máscara como "/32" e desabilita o input "Txt-Netmask"
        if events == "Rdb-Host":
            window["Txt-Netmask"].update("")
            window["Txt-Netmask"].update("32")
            window["Txt-Netmask"].update(disabled=True)
        
        #Se o IP for de rede, limpa e reabilita o input "Txt-Netmask"
        if events == "Rdb-Rede":
            window["Txt-Netmask"].update("")
            window["Txt-Netmask"].update(disabled=False)

        #Se desejar usar portas padrões
        if events == "Rdb-UsarPortasPadrao":
            window["Txt-PortasTCP"].update("")
            window["Txt-PortasTCP"].update(varredura().portasPadraoTCP)
            window["Txt-PortasTCP"].update(disabled=True)
            window["Txt-PortasUDP"].update("")
            window["Txt-PortasUDP"].update(varredura().portasPadraoUDP)
            window["Txt-PortasUDP"].update(disabled=True)
    
        #Se desejar personalizar as portas
        if events == "Rdb-NaoUsarPortasPadrao":
            window["Txt-PortasTCP"].update(disabled=False)
            window["Txt-PortasUDP"].update(disabled=False)

        # Varredura TCPUDP
        if events == "Btn-VarreduraTcpUdp":

            # Validação do IP e da máscara
            if validaIp(values["Txt-Ip"]) and validaMascara(values["Txt-Netmask"]):

                    # Instância da classe Varredura
                    analisador = varredura(values["Txt-Ip"],values["Txt-Netmask"])

                    # Usando portas padrões
                    if values["Rdb-UsarPortasPadrao"] == True:
                        if analisador.varrerTcpUdp(intensidade=values["Cmb-IntensidadeTcpUdp"],timeout=values["Txt-TimeoutTcpUdp"]):
                            exportar = dialogBox.popup_yes_no("Sucesso na varredura! Deseja exportar agora?")
                            if exportar == "Yes":
                                analisador.exportar(varreduraTcpUdp=True,caminhoTcpUdp=values["Txt-CaminhoTcpUdp"])
                                AtualizaResumo(analisador,window)
                            else:
                                AtualizaResumo(analisador,window)
                                dialogBox.notify("Dados salvos para exportação posterior na Aba de Saída")
                        else:
                            AtualizaResumo(analisador,window)
                    
                    # Usando portas personalizadas
                    elif values["Rdb-NaoUsarPortasPadrao"] == True:
                        if validaPortas(values["Txt-PortasTCP"], "TCP") and validaPortas(values["Txt-PortasUDP"], "UDP"):
                            if analisador.varrerTcpUdp(usarPortasPadrão=False,portasTCP=values["Txt-PortasTCP"],portasUDP=values["Txt-PortasUDP"],intensidade=values["Cmb-IntensidadeTcpUdp"],timeout=values["Txt-TimeoutTcpUdp"]):
                                exportar = dialogBox.popup_yes_no("Sucesso na varredura! Deseja exportar agora?")
                                if exportar == "Yes":
                                    analisador.exportar(varreduraTcpUdp=True,caminhoTcpUdp=values["Txt-CaminhoTcpUdp"])
                                    AtualizaResumo(analisador,window)
                                else:
                                    AtualizaResumo(analisador,window)
                                    dialogBox.notify("Dados salvos para exportação posterior na Aba de Saída")
                            else:
                                    AtualizaResumo(analisador,window)
                    
        # Varredura Ping
        if events == "Btn-VarreduraPing":

            # Validação do IP e da máscara
            if validaIp(values["Txt-Ip"]) and validaMascara(values["Txt-Netmask"]):
                    
                # Instância da classe Varredura
                analisador = varredura(values["Txt-Ip"],values["Txt-Netmask"])

                if analisador.varrePing(intensidade=values["Cmb-IntensidadePing"],timeout=values["Txt-TimeoutPing"]):
                    exportar = dialogBox.popup_yes_no("Sucesso na varredura! Deseja exportar agora?")
                    if exportar == "Yes":
                        analisador.exportar(varreduraPing=True,caminhoPing=values["Txt-CaminhoPing"])
                        AtualizaResumo(analisador,window)
                    else:
                        AtualizaResumo(analisador,window)
                        dialogBox.notify("Dados salvos para exportação posterior na Aba de Saída")
                else:
                    AtualizaResumo(analisador,window)

        #Exportação posterior
        if events == "Btn-Exportar":
            
            try:
                if isinstance(analisador, varredura):
                    if analisador.lastSweepType == "TCPUDP":
                        if analisador.exportar(varreduraTcpUdp=True,caminhoTcpUdp=values["Txt-CaminhoTcpUdp"]):
                            dialogBox.success("Exportado com sucesso")
                    elif analisador.lastSweepType == "PING":
                        if analisador.exportar(varreduraPing=True,caminhoPing=values["Txt-CaminhoPing"]):
                            dialogBox.success("Exportado com sucesso")
                    window["Lbl-HorarioExportacao"].update(analisador.lastExportTime)
                    window["Lbl-NomeExportacao"].update(analisador.lastExportName)
                    window["Lbl-StatusExportacao"].update(analisador.lastExportStatus)
            except Exception as e:
                dialogBox.erro(e)

        
        # Configuração de caminho de exportaçâo TCPUDP
        if events == "Btn-CaminhoTcpUdp":

            caminho = sg.filedialog.askdirectory()

            if os.path.exists(caminho):
                if os.path.isfile('./path.ini'):
                    if configuracoes.gravarCaminhoTcpUdp(caminho=caminho):
                        window["Txt-CaminhoTcpUdp"].update(caminho)
                        dialogBox.notify("CAMINHO PARA EXPORTAÇÃO\n DE VARREDURA TCP/UDP\nALTERADO COM SUCESSO!")
                    else:
                        dialogBox.erro("OCORREU ALGUM ERRO NA LEITURA/GRAVAÇÃO DO CAMINHO EM PATH.INI")
                else:
                    dialogBox.erro("O ARQUIVO PATH.INI NÃO FOI ENCONTRADO NA PASTA DO NETZED!")
            elif not caminho:
                dialogBox.erro("NENHUM CAMINHO INFORMADO!")
            else:
                dialogBox.erro("CAMINHO NÃO ENCONTRADO!")

        # Configuração de caminho de exportaçâo PING
        if events == "Btn-CaminhoPing":

            caminho = sg.filedialog.askdirectory()

            if os.path.exists(caminho):
                if os.path.isfile('./path.ini'):
                    if configuracoes.gravarCaminhoPing(caminho=caminho):
                        window["Txt-CaminhoPing"].update(caminho)
                        dialogBox.notify("CAMINHO PARA EXPORTAÇÃO\n DE VARREDURA PING\nALTERADO COM SUCESSO!")
                    else:
                        dialogBox.erro("OCORREU ALGUM ERRO NA LEITURA/GRAVAÇÃO DO CAMINHO EM PATH.INI")
                else:
                    dialogBox.erro("O ARQUIVO PATH.INI NÃO FOI ENCONTRADO NA PASTA DO NETZED!")
            elif not caminho:
                dialogBox.erro("NENHUM CAMINHO INFORMADO!")
            else:
                dialogBox.erro("CAMINHO NÃO ENCONTRADO!")

        #Abrir página de suporte
        if events == "Btn-Suporte":
            webbrowser.open("https://github.com/mquelucci/netzed/wiki/NETZED-VERS%C3%83O-2")

        #Abrir fórum
        if events == "Btn-Forum":
            webbrowser.open("https://github.com/mquelucci/netzed/discussions")
            

    window.close()

#=============================================================================================================================================================================
#=============================================================================================================================================================================
#=============================================================================================================================================================================        
# SISTEMA

sg.theme_global("LightBrown1")
welcome()
main()