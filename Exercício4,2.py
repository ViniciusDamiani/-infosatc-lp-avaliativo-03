#Incompleto
S=0
usuario=0
print("Olá, para ser um doador você precisa se encaixar nos requisitos: Ter entre 16 e 69 anos, mais de 50kg, ter dormido pelo menos 6h nas últimas 24horas")
doadorIdade = int(input("Informe sua idade:"))
doadorPeso = float(input("Informe seu peso:"))
doadorSono = float(input("Na noite anterior, quantas horas você dormiu? "))

#Verificando se o doador se adequa na idade
if (doadorIdade>16) and (doadorIdade<69):
    print("Você possui idade para doar sangue!")
else:
    print("Ah não! Você não possui idade para doar")

#Verificando se o doador se adequa no peso
if doadorPeso>50:
    print("Você está no peso ideal para doar sangue!")
else:
    print("Você não se adequa ao peso que requesitamos")

#Verificando se o doador se adequa nas horas de sono
if doadorSono>6:
    print("Sua noite de sono foi bela, você já pode doar!")
else:
    print("Você não pode doar. Volte para casa e descanse")

#Verificando se o doador deseja se cadastrar
cadastro = float(input("Você deseja se cadastrar conosco (S/N)?"))
if cadastro == S:
    usuario=(input("Informe seu nome completo:"))

    

