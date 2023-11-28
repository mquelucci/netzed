# NETZED DOCS - 2023.11.2.2

## ESTRUTURA DO CÓDIGO

| Módulo | Função |
| ------ | ------ |
| _main_ | Principal. Integra os outros módulos e possui o controle da interface gráfica|
| _varredura_ | Classe _varredura_ que utiliza a biblioteca _python-nmap_ para realizar os _scans_ na rede e fazer a exportação em formato **JSON** nos caminhos de exportação |
| _configuracoes_ | Classe _configuracoes_ que faz a leitura e gravação do arquivo _PATH.ini_ com os caminhos de exportação |
| _dialogbox_ | Possui métodos para criação dos _pop-ups_ padrões do sistema para **sucesso**, **erro**, **notificação** e **requisição** |
| _validate_ | Possui métodos para validação de IP, máscaras de rede, portas, _timeout_ e intensidade de varredura |
| _gui_ | Classe _gui_ que utiliza componentes da biblioteca _PySimpleGUI_ para criar a interface do NETZED de maneira modular e que facilita a manutenção :) |

### Métodos da _main_

* `welcome` - Criação e exibição da tela de boas vinda com o ícone do NETZED
* `AtualizaResumo` - Atualiza campos da tab _Resumo_ com informações contidas nos atributos do objeto _analisador_ (que é do tipo _varredura_)
* `main` - Função **principal** que utiliza os outros módulos para trazer a funcionalidade do sistema e controle da interface gráfica

### Métodos da _varredura_

* `_init_` (none) - Construtor da classe _varredura_, que passa o IP e a máscara de rede para a classe que serão utilizados na varredura
* `varrerTcpUdp` (bool) - Realiza uma varredura nas portas TCP e UDP, padronizadas ou setadas manualmente pelo usuário
* `varrePing` (bool) - Realiza a varredura Ping
* `ResultadoScanJson` (string) - Obtém o resultado da varredura que é do tipo **dicionário**, filtra apenas o objeto **_scan_** e converte para **_string_ json**
* `ResultadoCompletoJson` (string) - Obtém o resultado da varredura que é do tipo **dicionário** e converte tudo para **_string_ json**
* `exportar` (bool) - Realiza a exportação da varredura no caminho de exportação informado nos parâmetros e obtido da _caixa de texto_ da _tab de Configurações_

### Métodos de _configuracoes_

* `gravarCaminhoTcpUdp` (string) - Grava o caminho de exportação da varredura TCP/UDP no arquivo _path.ini_
* `gravarCaminhoPing` (string) - Grava o caminho de exportação da varredura Ping no arquivo _path.ini_
* `verCaminhoTcpUdp` (string) - Lê o caminho de exportação da varredura TCP/UDP no arquivo _path.ini_
* `verCaminhoPing` (string) - Lê o caminho de exportação da varredura Ping no arquivo _path.ini_

### Métodos de _dialogbox_

* `success` (none) - Cria um _auto close pop-up_ para mensagens destinadas a operações realizadas com êxito
* `erro` (none) - Cria um _error pop-up_ para mensagens destinadas a falhas em operações
* `notify` (none) - Cria uma _notify pop-up_ para mensagens de aviso destinadas a alterações importantes que foram realizadas
* `yesno` (none) - Cria um _yes no pop-up_ para mensagens de confirmação de operação

### Métodos de __validate_

* `validaIp` (bool) - Verifica se o endereço IPv4 é válido
* `validaMascara` (bool) - Verifica se a máscara de rede é válida e está na notação do _CIDR_
* `validaPortas` (bool) - Verifica se as portas informadas são válidas dentro do escopo de portas TCP e UDP
* `validaTimeout` (bool) - Verifica se o _timeout_ informado é válido
* `validaIntensidade` (bool) - Verifica se a intensidade de varredura informada é válida

### Métodos de _gui_

* `build` (PySimpleGui.TabGroup) - Através das propriedades da classe _gui_, a função `build` monta e retorna o layout do sistema
