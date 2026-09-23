class DispositivoIoT:
    def __init__(self, nome, bateria):
        self.nome = nome
        self.bateria = bateria

class HubCentral:
    def __init__(self):
        self.dispositivosConectados = []

    def adicionarDispostivo(self, dispositivo):
        self.dispositivosConectados.append(dispositivo)

    def relatorioBateriaBaixa(self):
        for dispositivo in self.dispositivosConectados:
            if (dispositivo.bateria < 20):
                print(dispositivo.nome)

dispositivo1 = DispositivoIoT("lampada", 25)
dispositivo2 = DispositivoIoT("Relogio", 18)
dispositivo3 = DispositivoIoT("Celular", 10)

hub = HubCentral()

hub.adicionarDispostivo(dispositivo1)
hub.adicionarDispostivo(dispositivo2)
hub.adicionarDispostivo(dispositivo3)

hub.relatorioBateriaBaixa()

