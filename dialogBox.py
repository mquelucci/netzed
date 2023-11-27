"""
MÓDULO DE EXIBIÇÃO DE POPUPS PADRONIZADOS
"""

from PySimpleGUI import popup_yes_no, popup_error, popup_auto_close, popup_notify

    
def success(txt):
    """
    MENSAGEM DE SUCESSO
    """
    popup_auto_close(txt,
                    no_titlebar=True,
                    auto_close=True,
                    auto_close_duration=2,
                    background_color="darkblue",
                    text_color="white",
                    button_color="black")
    

def erro(txt):
    """
    MENSAGEM DE ERRO
    """
    popup_error(txt,
                no_titlebar=True,
                grab_anywhere=True,
                background_color="darkred",
                text_color="white") 

    

def notify(txt):
    """
    NOTIFICAÇÕES
    """
    popup_notify(txt,
                fade_in_duration=50,
                alpha=0.8,
                display_duration_in_ms=2000)
    
    

def yesno(txt):
    """
    POPUP DE SIM OU NÃO
    """
    option = popup_yes_no(txt,
                        no_titlebar=True,
                        background_color="darkblue",
                        text_color="white",
                        button_color="black")
    return option