import configparser

class configuracoes:
    
    def gravarCaminhoTcpUdp(caminho):
        """
        GRAVA NO ARQUIVO DE CONFIGURAÇÃO 'path.ini' O LOCAL DE EXPORTAÇÃO PARA VARREDURAS TCP/UDP

        :param path: CAMINHO DO LOCAL DE EXPORTAÇÃO
        :return: boolean
        """
        try:
            # Instância da classe ConfigParser
            config = configparser.ConfigParser()

            # Lê o arquivo e grava as seções e campos encontrados
            config.read('./path.ini')

            # Define que a informação do campo 'path' da seção 'PING' é igual ao caminho informado
            config['TCPUDP']['path'] = caminho

            # Grava o caminho de exportação das varreduras TCP UDP
            with open('./path.ini', 'w') as arquivo:
                config.write(arquivo)

            return True
        except:
            return False

    def gravarCaminhoPing(caminho):
        """
        GRAVA NO ARQUIVO DE CONFIGURAÇÃO 'path.ini' O LOCAL DE EXPORTAÇÃO PARA VARREDURAS PING

        :param path: CAMINHO DO LOCAL DE EXPORTAÇÃO
        :return: boolean
        """
        try:
            # Instância da classe ConfigParser
            config = configparser.ConfigParser()
            
            # Lê o arquivo e grava as seções e campos encontrados
            config.read('./path.ini')

            # Define que a informação do campo 'path' da seção 'PING' é igual ao caminho informado
            config['PING']['path'] = caminho

            # Grava o caminho de exportação das varreduras Ping
            with open('./path.ini', 'w') as arquivo:
                config.write(arquivo)
            return True
        except:
            return False

    def verCaminhoTcpUdp():
        """
        RETORNA O CAMINHO QUE CONSTA NO CAMPO 'path' DA SEÇÃO 'TCPUDP'

        :return: (string) diretório
        """

        config = configparser.ConfigParser()

        config.read('./path.ini')

        caminho = config['TCPUDP']['path']

        return caminho

    def verCaminhoPing():
        """
        RETORNA O CAMINHO QUE CONSTA NO CAMPO 'path' DA SEÇÃO 'PING'

        :return: (string) diretório
        """

        config = configparser.ConfigParser()

        config.read('./path.ini')

        caminho = config['PING']['path']

        return caminho