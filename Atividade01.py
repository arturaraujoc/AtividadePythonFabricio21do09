nivelAcesso = int(input("Digite seu nível de acesso: "))
portaDestravada = False

if nivelAcesso >= 5:
    portaDestravada = True
    print("Acesso liberado")
else:
    print("Acesso negado, Permissão insuficiente")