def analisarTemperaturas(temperaturas):
    soma = 0
    alertasCalor = 0

    for temperatura in temperaturas:
        soma += temperatura

        if temperatura > 30.0:
            alertasCalor += 1

    media = soma / len(temperaturas)

    return media, alertasCalor


def main():
    temperaturas = [22.5, 25.0, 31.2, 28.4, 19.8]

    media, alertas = analisarTemperaturas(temperaturas)

    print(f"Temperatura média do dia: {media:.2f} °C")
    print(f"Alertas de calor: {alertas}")


if __name__ == "__main__":
    main()