import time
import datetime
import os
import pyautogui
import pygetwindow
import cv2
import mss
import requests
import numpy as np
from conf import *

# Altura e largura, são populados no print_screen()
screen_width = screen_height = 0

# Endereço da pasta das imagens
img_path = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'pics' + os.sep

# Janelas do navegador encontradas
windows = []


def telegram_send(text):
    """
    Envio de mensagens de texto pelo bot do telegram, conforme o link da api
    https://core.telegram.org/bots/api#sendmessage
    :param text: Mensagem a ser enviada
    :return: None
    """
    if telegram_notify:
        send = 'https://api.telegram.org/bot' + bot_token +\
               '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + text
        requests.get(send)
        time.sleep(1)


def telegram_send_photo(photo_path, caption):
    """
    Envio de fotos pelo bot do telegram, conforme o link da api
    https://core.telegram.org/bots/api#sendphoto
    :param photo_path: Caminho da foto
    :param caption: Um caption para a foto
    :return: None
    """
    url = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto'
    data = {'chat_id': chat_id, 'caption': caption}
    files = {'photo': open(photo_path, 'rb')}
    requests.post(url, files=files, data=data)


def get_windows_running_game():
    """
    Encontra as janelas com o jogo aberto e cria um dictionary de controle para cada uma,
    mesmo se o jogo estiver em browsers diferentes
    :return: None
    """
    i = 1
    for w in pygetwindow.getWindowsWithTitle('Bombcrypto - '):
        windows.append({
            'window': w,
            'index': str(i),
            'login': False,
            'working': False,
            'farming': False,
            'time_to_refresh': 0,
            'time_to_rest': 0
        })
        i += 1

    n = len(windows)
    s = '' if n == 1 else 's'
    telegram_send(f"Opa, encontrei {n} janela{s} do browser rodando o Bombcrypto, iniciando os trabalhos...")


def print_screen():
    """
    Print da primeira tela e atualização da altura e largura do monitor
    :return: Array
    """
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)
        global screen_width, screen_height
        screen_width, screen_height = sct_img.size
        sct_img = np.array(sct_img)

    return sct_img


def found_img(window, img, click=False, refresh=True):
    """
    Acha imagem requerida no print atual da tela
    :param window: Janela atual (multijanelas)
    :param img: Nome da imagem
    :param click: Se é para clicar na imagem quando achar
    :param refresh: Se é para recarregar o browser ao atingir o limite
    :return: Boolean
    """
    attempt = 0
    while attempt < max_attempt_found_img:
        img_rgb = print_screen()
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img_path + img, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if len(loc[0]) == 0:
            time.sleep(1)
            attempt += 1
            continue
        else:
            _, _, _, max_loc = cv2.minMaxLoc(res)
            loc = (max_loc[0] + w / 2, max_loc[1] + h / 2)
            if click:
                pyautogui.moveTo(loc[0], loc[1], duration=1.5, tween=pyautogui.easeInOutQuad)
                pyautogui.click()

            break

    if attempt == max_attempt_found_img:
        window['login'] = False
        telegram_send(f"Janela {window['index']}: {max_attempt_found_img} tentativas atingidas ao procurar a imagem {img}")
        if refresh:
            reload(window)

        return False
    else:
        return True
    '''for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
    cv2.imshow('image', img_rgb)
    cv2.waitKey(0)
    print(loc)'''


def accept_terms_if_did_not(window):
    """
    Aceita os termos de uso, inserido na versão 31 do jogo
    :param window: Janela atual (multijanelas)
    :return: Boolean
    """
    if not window['login']:
        if not found_img(window, "connect_wallet.png", refresh=False):
            if found_img(window, "i_accept.png", True):
                return found_img(window, "accept.png", True)


def connect_wallet(window):
    """
    Conecta e assina o smart contract
    :param window: Janela atual (multijanelas)
    :return: None
    """
    if not window['login']:
        if found_img(window, "connect_wallet.png", True):
            pyautogui.hotkey('ctrl', 'pgup')
            if found_img(window, "activity.png", True):
                if found_img(window, "signature_request.png", True, False):
                    if found_img(window, "sign.png", True):
                        if found_img(window, "assets.png", True):
                            pyautogui.hotkey('ctrl', 'pgup')
                            if found_img(window, "treasure_hunt.png"):
                                telegram_send(f"Janela {window['index']}: carteira conectada")
                                window['login'] = True
                                window['time_to_refresh'] = time.time()
                                if window['time_to_rest'] == 0:
                                    window['time_to_rest'] = time.time()
                else:
                    # As vezes ocorre de não aparecer a solicitação de assinatura, algum
                    # bug da metamask, voltamos ao estado inicial da tela da metamask, mudamos
                    # pro bomb e damos um reload
                    if found_img(window, "assets.png", True):
                        pyautogui.hotkey('ctrl', 'pgup')
                        reload(window)


def go_to_work(window):
    """
    Bota os bhero pra trabalhar
    :param window: Janela atual (multijanelas)
    :return: None
    """
    if window['login'] and not window['working']:
        if found_img(window, "heroes.png", True):
            if found_img(window, "work_all.png", True):
                if found_img(window, "close_work.png", True):
                    if found_img(window, "treasure_hunt.png"):
                        window['working'] = True
                        telegram_send(f"Janela {window['index']}: Todos os bhero colocados para trabalhar")


def go_to_treasure_hunt(window):
    """
    Clica no modo treasure hunt para começar a farmar
    :param window: Janela atual (multijanelas)
    :return: None
    """
    if window['login'] and not window['farming']:
        if found_img(window, "treasure_hunt.png", True):
            window['farming'] = True
            telegram_send(f"Janela {window['index']}: farmando no treasure hunt...")


def go_back_main_if_no_error(window):
    """
    Volta para a tela inicial se não tem mensagem de erro
    :param window: Janela atual (multijanelas)
    :return: None
    """
    if window['login']:
        found_error_bar = False
        for error_bar in ['error_bar_.png', 'error_bar.png']:
            img_rgb = print_screen()
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(img_path + error_bar, 0)
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= threshold)
            if len(loc[0]) > 0:
                found_error_bar = True
                break

        if not found_error_bar and found_img(window, "back.png", True):
            telegram_send(f"Janela {window['index']}: voltando para a tela inicial")
            time.sleep(3)


def notify_ammount_bcoin(window):
    """
    Notifica pelo telegram sobre o total de bcoin até o momento
    :param window: Janela atual (multijanelas)
    :return: None
    """
    hr_now = datetime.datetime.now().time()
    hr_config = datetime.datetime.strptime(time_notify_ammount_of_bcoin, '%H:%M')
    hr_max = hr_config + datetime.timedelta(seconds=time_to_refresh)
    hr_config = hr_config.time()
    hr_max = hr_max.time()
    if window['login'] and window['farming'] and hr_config <= hr_now < hr_max:
        if found_img(window, "chest.png", True):
            time.sleep(3)
            img_rgb = print_screen()
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(img_path + "bcoins.png", 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            # Threshold tem que ser 0.8 mesmo, é proposital, pq a imagem
            # "bcoins.png" não possui o número de moedas, daí um match de
            # 0.9 pra cima é impossível
            loc = np.where(res >= 0.8)
            if len(loc[0]) > 0:
                _, _, _, max_loc = cv2.minMaxLoc(res)
                crop = img_rgb[max_loc[1]:max_loc[1] + h, max_loc[0]:max_loc[0] + w]
                write_status = cv2.imwrite(img_path + "ammount_bcoin.jpg", crop)
                if write_status is True and found_img(window, "close_chest.png", True):
                    msg = f"Janela {window['index']}: total de BCOIN até o momento"
                    telegram_send_photo(img_path + "ammount_bcoin.jpg", msg)
                    os.remove(img_path + "ammount_bcoin.jpg")


def reload(window):
    """
    Recarrega o browser
    :param window: Janela atual (multijanelas)
    :return: None
    """
    pyautogui.hotkey('ctrl', 'shift', 'r')
    time.sleep(3)
    telegram_send(f"Janela {window['index']}: recarregando o browser...")


def actions(window):
    """
    Ações a serem executadas
    :param window: Janela atual (multijanelas)
    :return: None
    """
    if (time.time() - window['time_to_refresh']) >= time_to_refresh:
        if (time.time() - window['time_to_rest']) >= time_to_rest:
            window['time_to_rest'] = time.time()
            window['working'] = False
            telegram_send(f"Janela {window['index']}: Tempo máximo de descanso de {time_to_rest} segundos "
                          f"iniciado, os bhero trabalharão após o login")

        notify_ammount_bcoin(window)
        go_back_main_if_no_error(window)
        telegram_send(f"Janela {window['index']}: Tempo máximo de {time_to_refresh} segundos para recarregar "
                      f"iniciado, para fugir do bug dos blocos indestrutíveis ou corrigir algum bhero bugado")
        window['time_to_refresh'] = time.time()
        window['login'] = window['farming'] = False
        reload(window)

    accept_terms_if_did_not(window)
    connect_wallet(window)
    go_to_work(window)
    go_to_treasure_hunt(window)


if __name__ == '__main__':
    get_windows_running_game()
    while True:
        for current in windows:
            current['window'].activate()
            if not current['window'].isMaximized:
                current['window'].maximize()

            actions(current)
            time.sleep(2)
