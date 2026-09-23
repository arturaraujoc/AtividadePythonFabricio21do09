def analisarTemperaturas(temp):
    soma = 0
    quantidadeDeAnalises = 0
    media = 0
    ultrapassou30 = 0
    contador = 0

    while (contador < len(temp)):
        soma += temp[contador]
        quantidadeDeAnalises += 1
        if (temp[contador] > 30):
            ultrapassou30 += 1
        contador += 1

    media = soma/quantidadeDeAnalises

    return media, ultrapassou30



temperaturas = []
while True:
    temperatura = float(input("Digite a temperatura: "))
    if temperatura == 0:
        break
    temperaturas.append(temperatura)

print(analisarTemperaturas(temperaturas))



    
