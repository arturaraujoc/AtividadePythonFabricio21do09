class DispositivoIoT:
    def __init__(self, nome, bateria):
        self.nome = nome

        if bateria < 0:
            self.bateria = 0
        elif bateria > 100:
            self.bateria = 100
        else:
            self.bateria = bateria


class HubCentral:
    def __init__(self):
        self.dispositivos = []

    def adicionarDispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def relatorioBateriaBaixa(self):

        dispositivosBateriaBaixa = []

        for dispositivo in self.dispositivos:

            if dispositivo.bateria < 20:
                dispositivosBateriaBaixa.append(dispositivo.nome)

        if not dispositivosBateriaBaixa:
            return "Nenhum dispositivo com bateria baixa."

        return "Dispositivos com bateria baixa: " + ", ".join(
            dispositivosBateriaBaixa
        )


def main():

    dispositivo1 = DispositivoIoT("Sensor de Temperatura", 15)
    dispositivo2 = DispositivoIoT("Câmera de Segurança", 75)
    dispositivo3 = DispositivoIoT("Luminária Smart", 10)

    hub = HubCentral()

    hub.adicionarDispositivo(dispositivo1)
    hub.adicionarDispositivo(dispositivo2)
    hub.adicionarDispositivo(dispositivo3)

    relatorio = hub.relatorioBateriaBaixa()

    print("RELATÓRIO DO HUB CENTRAL:")
    print(relatorio)


if __name__ == "__main__":
    main()