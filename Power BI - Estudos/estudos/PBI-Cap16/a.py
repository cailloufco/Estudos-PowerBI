def validar_senha(senha:str):
    temMaiuscula = False
    temNumero = False
    if len(senha) > 6:
        for caracter in senha:
            if caracter.isnumeric():
                temNumero = True
            if caracter.isupper():
                temMaiuscula = True
    else:
        return False;
    if temMaiuscula and temNumero:
        return True;
    else:
        return False;


senha = input("Digite sua senha: ")
if validar_senha(senha):
    print("Entrada permitida!")
else:
    print("Entrada negada!")