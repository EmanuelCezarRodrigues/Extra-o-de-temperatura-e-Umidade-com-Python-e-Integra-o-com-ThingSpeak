# wifi_lib.py
import network
import time

def conecta(ssid, senha):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(1)
    return station

# main.py
from wifi_lib import conecta
import urequests
import machine
import dht
import time

# Configuração do sensor DHT11
d = dht.DHT11(machine.Pin(4))

# Configuração do pino do relé
r = machine.Pin(2, machine.Pin.OUT)

# Loop infinito
while True:
    # Realiza uma medição de temperatura e umidade com o sensor DHT11
    d.measure()

    # Imprime as leituras no console
    print("Temp = {}  Umid = {}".format(d.temperature(), d.humidity()))

    # Verifica se a temperatura é maior que 31°C ou a umidade é maior que 70%
    if d.temperature() > 31 or d.humidity() > 70:
        r.value(1)  # Ativa o relé
    else:
        r.value(0)  # Desativa o relé

    # Conecta-se à rede Wi-Fi
    station = conecta("Nome do wifi", "Senha do Wifi")

    # Verifica se a conexão foi bem-sucedida
    if station.isconnected():
        print("Conectando!...")

        # Acessa um site ou uma API com os dados da temperatura
        response = urequests.get("LINK DA API do FIELD1" + str(d.temperature()))
        print("Página acessada:")
        print(response.text)

        # Aguarda por 20 segundos
        time.sleep(20)

        # Acessa um site ou uma API com os dados da umidade
        response = urequests.get("LINK DA API do FIELD2" + str(d.humidity()))
        print("Página acessada:")
        print(response.text)

        # Desconecta da rede Wi-Fi
        station.disconnect()

        # Aguarda por mais 20 segundos antes de repetir o ciclo
        time.sleep(20)
