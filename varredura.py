"""
MÓDULO DE VARREDURA
"""
import nmap
from datetime import datetime
import dialogBox
import json

class varredura:

    # Portas TCP e UDP padronizadas
    portasPadraoTCP = "137,138,139,445,3389,21,69,25,143,110,22,23,53,67,68,80,443,161,162,1900,123,5353,514,3306,5432,3050"
    portasPadraoUDP = "137,138,139,445,67,68,53,69,111,161,162,1900,123,5353,514"
    lastSweepStartTime = "SEM DADOS" # Horário de início da última varredura
    lastSweepEndTime = "SEM DADOS" # Horário de fim da última varredura
    lastSweepType = "SEM DADOS" # Tipo da última varredura feita
    lastSweepStatus = "SEM DADOS" # Status da última varredura feita
    lastExportTime = "SEM DADOS" # Horário da última exportação feita
    lastExportStatus = "SEM DADOS" # Status da última exportação feita
    lastExportName = "SEM DADOS" # Nome da última exportação feita

    def __init__(self, ip="", netmask=""):
        """
        Construtor da classe

        Parâmetros
        - ip (string): IP da rede ou do host a ser analisado
        - netmask (string): Máscara de rede
        """
        self.ip = ip
        self.netmask = netmask
        self.network = nmap.PortScanner()


    def varrerTcpUdp(self,usarPortasPadrão=True,portasTCP="",portasUDP="",intensidade="",timeout="60"):

        """
        Função de varredura TCP/UDP\n
        Realiza uma varredura nas portas TCP e UDP, padronizadas ou setadas manualmente pelo usuário\n

        Parâmetros:
        - usarPortasPadrão (boolean): Usar (ou não) as portas TCP e UDP padrões do Netzed
        - portasTCP (string): Portas a serem usadas no lugar das portas TCP padrão
        - portasUDP (string): Portas a serem usadas no lugar das portas UDP padrão
        - intensidade (string): Nível da intensidade da varredura, de 1 a 5.
        - timeout (string): Tempo de expiração em segundos. (padrão: 60 segundos)

        Retorno:
        - (boolean) Caso a varredura seja bem sucedida, retorna [True]. Do contrário, retorna [False]

        """
        try:
            self.lastSweepStartTime = datetime.now().strftime("%H:%M:%S") # Horário de início da última varredura
            
            if usarPortasPadrão:
                stringPortas = f"T:{self.portasPadraoTCP},U:{self.portasPadraoUDP}"
                self.result = self.network.scan(f"{self.ip}/{self.netmask}", arguments=f"-p {stringPortas} -T{intensidade} -sS -sU -O",timeout=int(timeout))
            else:
                # Se nenhuma porta TCP foi informada, mas alguma UDP foi
                if portasTCP=="" and portasUDP!="":
                    self.result = self.network.scan(f"{self.ip}/{self.netmask}", arguments=f"-p U:{portasUDP} -T{intensidade} -sU",timeout=int(timeout))
                # Se nenhuma porta UDP foi informada, mas alguma TCP foi
                elif portasUDP=="" and portasTCP!="":
                    self.result = self.network.scan(f"{self.ip}/{self.netmask}", arguments=f"-p T:{portasTCP} -T{intensidade} -sS -O",timeout=int(timeout))
                # Se nenhuma porta TCP e UDP foram informadas
                elif portasUDP=="" and portasTCP=="":
                    self.result = self.network.scan(f"{self.ip}/{self.netmask}", arguments=f" -T{intensidade} -sS -O",timeout=int(timeout))
                # Se alguma porta TCP e alguma UDP foram informadas
                else:
                    self.result = self.network.scan(f"{self.ip}/{self.netmask}", arguments=f"-p T:{portasTCP},U:{portasUDP} -T{intensidade} -sS -sU -O",timeout=int(timeout))
                        
            self.lastSweepEndTime =  datetime.now().strftime("%H:%M:%S") # Horário de fim da última varredura
            self.lastSweepType = "TCPUDP" # Tipo da última varredura feita
            self.lastSweepStatus = "SUCESSO" # Status da última varredura feita
            self.lastExportName = "SEM ARQUIVO"
            self.lastExportStatus = "AGUARDANDO EXPORTAÇÃO"
            self.lastExportTime = "AGUARDANDO EXPORTAÇÃO"
            return True
        except Exception as e:
            self.lastSweepEndTime =  datetime.now().strftime("%H:%M:%S") # Horário de fim da última varredura
            self.lastSweepType = "TCPUDP" # Tipo da última varredura feita
            self.lastSweepStatus = "ERRO NA VARREDURA!" # Status da última varredura feita
            self.lastExportName = "SEM DADOS"
            self.lastExportStatus = "SEM DADOS"
            self.lastExportTime = "SEM DADOS"
            dialogBox.erro(f"Erro na varredura\n({e})")
            return False
        except KeyboardInterrupt:
            dialogBox.erro("A varredura foi interrompida")

    def varrePing(self,intensidade="",timeout="60"):

        """
        Função de varredura PING\n

        Parâmetros:
        - intensidade (string): Nível da intensidade da varredura, de 1 a 5
        - timeout (string): Tempo de expiração em segundos (padrão: 60 segundos)

        Retorno:
        - (boolean) Caso a varredura seja bem sucedida, retorna [True]. Do contrário, retorna [False]
        """
        try:
            self.lastSweepStartTime = datetime.now().strftime("%H:%M:%S") # Horário de início da última varredura
            self.result = self.network.scan(f"{self.ip}/{self.netmask}", arguments=f"-sn -T{intensidade}",timeout=int(timeout))
            self.lastSweepEndTime =  datetime.now().strftime("%H:%M:%S") # Horário de fim da última varredura
            self.lastSweepType = "PING" # Tipo da última varredura feita
            self.lastSweepStatus = "SUCESSO!" # Status da última varredura feita
            self.lastExportName = "SEM ARQUIVO"
            self.lastExportStatus = "AGUARDANDO EXPORTAÇÃO"
            self.lastExportTime = "AGUARDANDO EXPORTAÇÃO"
            return True
        except Exception as e:
            self.lastSweepEndTime =  datetime.now().strftime("%H:%M:%S") # Horário de fim da última varredura
            self.lastSweepType = "PING" # Tipo da última varredura feita
            self.lastSweepStatus = "ERRO NA VARREDURA!" # Status da última varredura feita
            self.lastExportName = "SEM DADOS"
            self.lastExportStatus = "SEM DADOS"
            self.lastExportTime = "SEM DADOS"
            dialogBox.erro(f"Erro na varredura\n({e})")
            return False
        except KeyboardInterrupt:
            dialogBox.erro("A varredura foi interrompida")

    def ResultadoScanJson(self):
        """
        OBTÉM O SCAN DA VARREDURA NA ESTRUTURA DE DICIONÁRIO\n
        E CONVERTE PARA JSON STRING

        Retorno:
        - (string) Scan da varredura
        """
        if self.result["scan"] == "":
            stringJson = "{}"
        stringJson = json.dumps(self.result["scan"],indent=4)
        return stringJson

    def ResultadoCompletoJson(self):
        """
        OBTÉM O RESULTADO COMPLETO DA VARREDURA NA ESTRUTURA DE DICIONÁRIO\n
        E CONVERTE PARA JSON STRING

        Retorno:
        - (string) Resultado completo da varredura
        """
        if self.result == "":
            stringJson = "{}"
        stringJson = json.dumps(self.result,indent=4)
        return stringJson
    
    def exportar(self,varreduraPing=False,varreduraTcpUdp=False,caminhoPing="",caminhoTcpUdp=""):

        """
        Função de exportação da varredura em arquivo CSV para o caminho de exportação informada de acordo com o tipo de varredura

        
        Parâmetros
        - varreduraPing (boolean): True se o dados são de uma varredura PING / False se não forem
        - varreduraTcpUdp (boolean): True se o dados são de uma varredura TCP-UDP / False se não forem
        - caminhoPing (string): Caminho para salvar o arquivo CSV da varredura Ping
        - caminhoTcpUdp (string): Caminho para salvar o arquivo CSV da varredura TCP-UDP

        Retorno
        - (boolean) True se conseguir exportar; False se não conseguir
        """
        if varreduraTcpUdp:
            try:
                horarioDeExportacao = datetime.now().strftime("%d.%m.%y_%H.%M")
                with open(f"{caminhoTcpUdp}/TCPUDP_{self.ip}_{self.netmask}_{horarioDeExportacao}.json","x",encoding="utf-8") as arquivo:
                    arquivo.write(self.ResultadoScanJson())
                self.lastExportName = f"TCPUDP_{self.ip}_{self.netmask}_{horarioDeExportacao}.json"
                self.lastExportStatus = "SUCESSO"
                self.lastExportTime = datetime.now().strftime("%H:%M:%S")
                return True    
            except Exception as e:
                self.lastExportName = ""
                self.lastExportStatus = "ERRO NA EXPORTAÇÃO"
                self.lastExportTime = datetime.now().strftime("%H:%M:%S")
                dialogBox.erro(f"Erro na exportação\n({e})")
                return False
        
        elif varreduraPing:
            try:
                horarioDeExportacao = datetime.now().strftime("%d.%m.%y_%H.%M")
                with open(f"{caminhoPing}/PING_{self.ip}_{self.netmask}_{horarioDeExportacao}.json","x",encoding="utf-8") as arquivo:
                    arquivo.write(self.ResultadoScanJson())
                self.lastExportName = f"PING_{self.ip}_{self.netmask}_{horarioDeExportacao}.json"
                self.lastExportStatus = "SUCESSO"
                self.lastExportTime = datetime.now().strftime("%H:%M:%S")
                return True
            except Exception as e:
                self.lastExportName = ""
                self.lastExportStatus = "ERRO NA EXPORTAÇÃO"
                self.lastExportTime = datetime.now().strftime("%H:%M:%S")
                dialogBox.erro(f"Erro na exportação\n({e})")
                return False