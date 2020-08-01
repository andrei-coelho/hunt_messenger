'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*********************************************************************************
*                                                                               *
*                                                                               *
*                      _______________________________________                  *
*                    /_________                                \                *
*                    |_________/       ____      ____          /|               *
*                     ____    /       /   /     /   /         / /               *
*                   /____/|  /       /   /     /   /         / /                *
*                   |____|/ /       /   /     /   /         / /                 *
*                    __    /       /___/     /___/         / /                  *
*                  /__/|  /      _________________        / /                   *
*                  |__|/ /      /_/_/_/_/_/_/_/_/        / /                    *
*                       /      /_/_/_/_/_/_/_/_/        / /                     *
*                      /      ------------------       / /                      *
*                     /                               / /                       *
*                     \______________________________/ /                        *
*                     \_______________________________/                         *
*                                                                               *
*                                                                               *
*        ____     ____     ____      ____     _____________     ____________    *
*       /   /|   /   /|   /   /|    /   /|   /    ____     /|  /___    ____/|   *
*      /   /_/__/   / /  /   / /   /   / /  /   /  ___/   / /  |__/   / ____/   *
*     /    ____    / /  /   / /   /   / /  /   / /   /   / /     /   / /        *
*    /   / ___/   / /  /   /_/___/   / /  /   / /   /   / /     /   / /         *
*   /___/ /  /___/ /  /_____________/ /  /___/ /   /___/ /     /___/ /          *
*   |____/   |____/   |______________/   |____/    |____/      |____/           *
*                                                                               *
*                                                                               *
*********************************************************************************
*                                                                               *
*                      ****  AUTHOR: Andrei Coelho  ***                         *
*                                                                               *
*********************************************************************************
*                                 MESSENGER                                     *
*********************************************************************************
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# python C:\\python-projects\\hunt_messenger\\hunt.py

from modules.fb import login, messenger 
from modules.helper import api, log


import sys, time

lista = api.get_list()
drivers = []
timer   = 5 # 600 = 10 minutos para cada conta

def get_next_driver(keyDriver, count = 0):

    totalDrivers   = len(drivers)

    if(totalDrivers == 0 or count == totalDrivers):
        return False

    if(keyDriver == totalDrivers):
        keyDriver  = 0

    if(drivers[keyDriver]['keyConta'] > len(drivers[keyDriver]['contas'])):
        keyDriver += 1
        count     += 1
        return get_next_driver(keyDriver, count)

    return [drivers[keyDriver], keyDriver]


if lista:

    if len(sys.argv) < 2:
        log.start(api.get_total()) # avisa que iniciou o processo com sucesso

    for conta in lista:
        driver  = login.login(conta)
        drivers.append({"driver":driver, "keyConta":0, "contas":conta['msgs']})

    key = 0
    timer = int(timer / len(drivers))

    while True:

        driverObj = get_next_driver(key)

        if driverObj:
            driver = driverObj[0]
            key    = driverObj[1]
            messenger.send_message_for(driver['contas'][driver['keyConta']], driver['driver'])
            driver['keyConta'] += 1
            time.sleep(timer)

        else:break


    # chrome.quit()
# pega e usa o cookie ou faz o login da conta selecionada

    # envia a mensagem para o perfil 
    # envia a informação para a API de que a mensagem foi enviada
    # aguarde 2,5 minutos para executar o próximo

# quando terminar informe a quantidade total de envios



