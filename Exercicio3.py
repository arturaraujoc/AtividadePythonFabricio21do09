class LuminariaSmart:
    def __init__(self, id):
        self.id = id
        self.ligada = False
        self.intensidade = 0

    def ligaDesliga(self, resp):
        if (resp == True):
            self.ligada = True
        else:
            self.ligada = False

    def ajustarIntensidade(self, valor):
        if (0 <= (self.intensidade + valor) <= 100):
            self.intensidade += valor
        else:
            print("Valor invalido!")

    def estadoAtual(self):
        print("ID: ", self.id,
              self.ligada,
              "Intensidade: ", self.intensidade)

luminaria = LuminariaSmart(1)

luminaria.ligaDesliga(True)

luminaria.ajustarIntensidade(75)

luminaria.estadoAtual()
        