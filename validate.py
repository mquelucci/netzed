#VALIDAÇÃO DO ENDEREÇO IP
from dialogBox import erro

def validaIp(ip):
    """
    VERIFICA SE O ENDEREÇO IP INFORMADO É VÁLIDO PARA SER USADO

    :param ip: (String) Endereço IP a ser validado
    :return: (Boolean) True | False
    """
    ip = ip.strip()
    if ip == "":
        erro("ENDEREÇO IP VAZIO!")
        return False
    else:
        try:
            ipStringSplit = ip.split(".")
            if len(ipStringSplit) != 4:
                erro("ENDEREÇO IP INVÁLIDO! VERIFIQUE E TENTE NOVAMENTE")
                return False
            else:

                try:
                    ipIntSplit = []
                    for octal in ipStringSplit:
                        ipIntSplit.append(int(octal))
                    ipStringSplit.clear() #Alívio de memória
                    
                    octaisInvalidos = 0
                    for octal in ipIntSplit:
                        if octal < 0 or octal > 255:
                            erro(f"O {ipIntSplit.index(octal) + 1}º OCTETO DO ENDEREÇO IP É INVÁLIDO!")
                            octaisInvalidos = octaisInvalidos + 1
                    if octaisInvalidos == 0:
                        return True
                    else:
                        return False
                except (ValueError,TypeError):
                    erro("ENDEREÇO IP POSSUI ALGUM VALOR NÃO NUMÉRICO! VERIFIQUE E TENTE NOVAMENTE")
                    return False
        except Exception:
            erro("ENDEREÇO IP INVÁLIDO! VERIFIQUE E TENTE NOVAMENTE")
            return False


#VALIDAÇÃO DA MÁSCARA DE REDE
def validaMascara(netmask):
    """
    VERIFICA SE A MÁSCARA INFORMADA É VÁLIDA PARA SER USADA

    :param netmask: (String) Máscara a ser validada
    :return: (Boolean) True | False
    """
    netmask = netmask.strip()

    if netmask.isdigit():
        if int(netmask) > 32:
            erro("CIDR MAIOR QUE 32!")
            return False
        elif int(netmask) < 1:
            erro("CIDR MENOR QUE 1!")
            return False
        else:
            return True
    elif "/" in netmask:
        erro("NÃO USE BARRA NA MÁSCARA DE REDE!")
    else:
        erro("MÁSCARA INVÁLIDA!")
        return False


#VALIDAÇÃO DE PORTAS
def validaPortas(ports, protocol):
    """
    VERIFICA SE AS PORTAS SÃO VÁLIDAS PARA SEREM USADAS

    :param tcp: (String) Portas TCP para validação
    :param udp: (String) Portas UDP para validação
    :return: (Boolean) True | False
    """
    if not ports:
        return True
    ports = ports.strip()
    portsList = str(ports).strip().split(",")
    for port in portsList:
        port = str(port).strip()
        if port.isdigit():
            if int(port) <= 0:
                erro(f"A porta {protocol} : {port} é menor ou igual a 0! Posição: {portsList.index(port) + 1}")
                return False
            elif int(port) > 65535:
                erro(f"A porta {protocol} : {port} é maior que 65535! Posição: {portsList.index(port) + 1}")
                return False
        else:
            erro(f"A porta {protocol} {port if port != '' else 'vazia'} encontrada é inválida! Posição: {portsList.index(port) + 1}")
            return False
    return True


#VALIDAÇÃO DE TIMEOUT
def validaTimeout(timeout):
    """
    VERIFICA SE O TIMEOUT É VÁLIDO PARA SER USADO

    :param timeout: string, timeout para validação
    :return: Boolean, True se for válido, False se for inválido
    """

    if str(timeout).isdigit() and int(timeout) >= 0:
        return True
    elif str(timeout).isalpha() or str(timeout).isalnum():
        erro("O TEMPO DE TIMEOUT DEVE SER UM NÚMERO INTEIRO POSITIVO!")
        return False
    elif int(timeout) < 0:
        erro("O VALOR DO TIMEOUT DEVE SER POSITIVO!")
    else:
        erro("VALOR DE TIMEOUT INVÁLIDO!")
        return False
    

#VALIDAÇÃO DE INTENSIDADE
def  validaIntensidade(intensidade):
    """
    VERIFICA SE A INTENSIDADE É VÁLIDA PARA SER USADA

    :param timeout: string, timeout para validação
    :return: Boolean, True se for válido, False se for inválido
    """

    if str(intensidade).isdigit() and int(intensidade) > 0 and int(intensidade) < 6:
        return True
    elif str(intensidade).isalpha() or str(intensidade).isalnum():
        erro("O VALOR DA INTENSIDADE DEVE SER UM NÚMERO INTEIRO POSITIVO!")
        return False
    elif int(intensidade) <= 0:
        erro("O VALOR DA INTENSIDADE DEVE SER POSITIVO!")
        return False
    else:
        erro("VALOR DE TIMEOUT INVÁLIDO!")
        return False