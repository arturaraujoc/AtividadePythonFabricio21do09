nivelAcesso = int(input("Nível de acesso: "))
portaDestravada = False

if (nivelAcesso >= 5):
    portaDestravada = True
    print("Porta destravada")
else:
    print("nivel de acesso insuficiente!")