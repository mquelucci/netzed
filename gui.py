import PySimpleGUI as sg
from varredura import varredura
from configuracoes import configuracoes


class gui():
    """
    CLASSE DE MONTAGEM DA INTERFACE GRÁFICA DO USUÁRIO
    """
    
    # Cabeçalho de versão
    version = sg.Text("Versão: 2023.11.2.2",font=("Roboto",12,"underline"))

    # Frame de IP e máscara de rede
    frameEnderecamento = [sg.Frame("Endereçamento",
                                   [[sg.Text("Endereço IPv4: ",font=("Roboto",10),text_color="black"),
                                     sg.Input(key="Txt-Ip",size=(15,1),font=("Roboto",10))],

                                    [sg.Radio("Rede","targetType",key="Rdb-Rede",enable_events=True,default=True,font=("Roboto",10),text_color="black"),
                                     sg.Radio("Host","targetType",key="Rdb-Host",enable_events=True,font=("Roboto",10),text_color="black")],

                                    [sg.Text("Máscara de rede (CIDR /XX): ",font=("Roboto",10),text_color="black"),
                                     sg.Input(key="Txt-Netmask",size=(5,1),font=("Roboto",10))]],
                                     
                                     font=("Roboto",12))] # Fonte do frame

    # Frame de portas TCP/UDP
    framePortas = [sg.Frame("Portas TCP/UDP",
                                     [[sg.Radio("Usar padrão","stdPorts",key="Rdb-UsarPortasPadrao",default=True,enable_events=True,font=("Roboto",10),text_color="black"),
                                       sg.Radio("Personalizar","stdPorts",key="Rdb-NaoUsarPortasPadrao",enable_events=True,font=("Roboto",10),text_color="black")],

                                      [sg.Text("Portas TCP: ",font=("Roboto",10),text_color="black"),
                                       sg.Multiline(varredura().portasPadraoTCP,disabled=True,key="Txt-PortasTCP",size=(30,3),font=("Roboto",10))],

                                      [sg.Text("Portas UDP: ",font=("Roboto",10),text_color="black"),
                                       sg.Multiline(varredura().portasPadraoUDP,disabled=True,key="Txt-PortasUDP",size=(30,3),font=("Roboto",10))]],
                                       
                                       font=("Roboto",12))] # Fonte do frame

    # Frame de configuração de timeout e intensidade varredura
    frameConfiguracaoTimeoutIntensidade = [sg.Frame("Configurações de Varredura",
                                                    [[sg.Text("Timeout TCP/UDP (segundos): ",font=("Roboto",10),text_color="black"),
                                                      sg.Input("180",key="Txt-TimeoutTcpUdp",size=(5,1),font=("Roboto",10))],

                                                     [sg.Text("Intensidade da Varredura TCP/UDP (1 a 5): ",font=("Roboto",10),text_color="black"),
                                                     sg.InputCombo(["1","2","3","4","5"],default_value="3",key="Cmb-IntensidadeTcpUdp",size=(5,1),font=("Roboto",10))],
 
                                                     [sg.Text("Timeout PING (segundos): ",font=("Roboto",10),text_color="black"),
                                                     sg.Input("180",key="Txt-TimeoutPing",size=(5,1),font=("Roboto",10))],
                                                    
                                                     [sg.Text("Intensidade da Varredura PING (1 a 5): ",font=("Roboto",10),text_color="black"),
                                                     sg.InputCombo(["1","2","3","4","5"],default_value="3",key="Cmb-IntensidadePing",size=(5,1),font=("Roboto",10))]],
                                                     
                                                     font=("Roboto",12))] # Fonte do frame

    # Frame de configuração dos locais de exportação
    frameConfiguracaoLocalExportacao = [sg.Frame("Local de exportação",
                                                 [[sg.Text("TCP/UDP: ",size=(10,1),justification='right',font=("Roboto",10),text_color="black"),
                                                   sg.Input(configuracoes.verCaminhoTcpUdp(),key="Txt-CaminhoTcpUdp",size=(30,1),font=("Roboto",10)),
                                                   sg.Button("PESQUISAR", key="Btn-CaminhoTcpUdp",font=("Roboto",10))],

                                                  [sg.Text("PING: ",size=(10,1),justification='right',font=("Roboto",10),text_color="black"),
                                                    sg.Input(configuracoes.verCaminhoPing(),key="Txt-CaminhoPing",size=(30,1),font=("Roboto",10)),
                                                    sg.Button("PESQUISAR", key="Btn-CaminhoPing",font=("Roboto",10))]],
                                                    
                                                    font=("Roboto",12))] # Fonte do frame
    # Frame de resumo da varredura
    frameResumo = [sg.Frame("Resumo",
                            [[sg.Column([[sg.Text("Hora de início da última varredura: ",font=("Roboto",10),text_color="black"), 
                                          sg.Text(f"SEM DADOS",key="Lbl-InicioVarredura",font=("Roboto",10))],

                                         [sg.Text("Hora de fim da última varredura: ",font=("Roboto",10),text_color="black"), 
                                          sg.Text(f"SEM DADOS",key="Lbl-FimVarredura",font=("Roboto",10))],

                                         [sg.Text("Status da última varredura: ",font=("Roboto",10),text_color="black"), 
                                          sg.Text(f"SEM DADOS",key="Lbl-StatusVarredura",font=("Roboto",10))],

                                         [sg.Text("Tipo da última varredura: ",font=("Roboto",10),text_color="black"), 
                                          sg.Text(f"SEM DADOS",key="Lbl-TipoVarredura",font=("Roboto",10))]]),

                                          sg.VerticalSeparator(),
                                          
                                          sg.Column([[sg.Text("Hora da última exportação: ",font=("Roboto",10),text_color="black"), 
                                                      sg.Text(f"SEM DADOS",key="Lbl-HorarioExportacao",font=("Roboto",10))],
                                       
                                                     [sg.Text("Status da última exportação: ",font=("Roboto",10),text_color="black"), 
                                                      sg.Text(f"SEM DADOS",key="Lbl-StatusExportacao",font=("Roboto",10))],

                                                     [sg.Text("Nome da última exportação: ",font=("Roboto",10),text_color="black"), 
                                                      sg.Text(f"SEM DADOS",key="Lbl-NomeExportacao",font=("Roboto",10))]],

                                                      vertical_alignment="top")],
                              
                              [sg.Column([[sg.Multiline(size=(80,20),key="Mtl_Saida",disabled=True)]])]],
                              
                              font=("Roboto",12),
                              element_justification="center")] # Fonte do frame

                                      
    
    Btn_VarreduraTcpUdp = [sg.Button("VARREDURA TCP/UDP",
                                     key="Btn-VarreduraTcpUdp",
                                     button_color="purple",
                                     mouseover_colors="violet",
                                     size=(30,1),
                                     font=("Roboto",10))]
    
    Btn_VarreduraPing = [sg.Button("VARREDURA PING",
                                   key="Btn-VarreduraPing",
                                   button_color="darkblue",
                                   mouseover_colors="blue",
                                   size=(30,1),
                                   font=("Roboto",10))]
    
    Btn_Exportar = [sg.Button("EXPORTAR A ÚLTIMA VARREDURA",
                              key="Btn-Exportar",
                              button_color="darkgreen",
                              mouseover_colors="green",
                              size=(30,1),
                              font=("Roboto",10))]
    
    Btn_Suporte = sg.Button("SUPORTE",
                             key="Btn-Suporte",
                             button_color="red",
                             mouseover_colors="darkred",
                             size=(15,1),
                             font=("Roboto",10))
    
    Btn_Forum = sg.Button("FÓRUM",
                           key="Btn-Forum",
                           button_color="#FF8C00",
                           mouseover_colors="#FFA500",
                           size=(15,1),
                           font=("Roboto",10))

    # Tab Principal (Endereçamento e Botões de varredura
    tabPrincipal = sg.Tab("Principal", [frameEnderecamento,
                                        framePortas,
                                        Btn_VarreduraTcpUdp,
                                        Btn_VarreduraPing],
                                        element_justification="center") 
    
    # Tab de configurações (Timeout, Intensidade, Caminhos de exportação)
    tabConfiguracoes = sg.Tab("Configurações",[frameConfiguracaoTimeoutIntensidade,
                                               frameConfiguracaoLocalExportacao],
                                               element_justification="center") 
    # Tab de status e resultado da varredura (Status, CSV, Exportação posterior) 
    tabSaida = sg.Tab("Saída",[frameResumo,
                               Btn_Exportar],
                               element_justification="center")

    def build(self):
        
        Tbg_Netzed = sg.TabGroup([[self.tabPrincipal],[self.tabConfiguracoes],[self.tabSaida]],tab_location="top")

        return Tbg_Netzed