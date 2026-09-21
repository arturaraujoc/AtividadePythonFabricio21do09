class LuminariaSmart:
    def __init__(self, idDispositivo):
        self.idDispositivo = idDispositivo
        self.ligada = False
        self.intensidade = 0

    def inverterEstado(self):
        self.ligada = not self.ligada

    def ajustarIntensidade(self, intensidade):
        if intensidade < 0:
            self.intensidade = 0

        elif intensidade > 100:
            self.intensidade = 100

        else:
            self.intensidade = intensidade


def main():
    luminaria = LuminariaSmart(1)

    luminaria.inverterEstado()

    luminaria.ajustarIntensidade(75)

    print("ESTADO DA LUMINÁRIA:")
    print(f"ID do dispositivo: {luminaria.idDispositivo}")
    print(f"Ligada: {luminaria.ligada}")
    print(f"Intensidade: {luminaria.intensidade}%")


if __name__ == "__main__":
    main()