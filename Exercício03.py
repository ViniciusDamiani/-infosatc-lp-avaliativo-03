#Ler do teclado a idade e o sexo de 10 pessoas. Calcule e imprima:
#A. Idade média das mulheres.
#B. Idade média dos homens.
#C. Idade média do grupo.
nFeminino=0
nMasculino=0
idadeF=0
idadeM=0
for sexo in range(1,4):
    sexo=(input("Informe seu sexo. M para Masculino e F para Feminino: "))
    if sexo=="M":
         nMasculino=nMasculino+1
         idadeM=idadeM+(int(input("Informe sua idade: ")))
    else:
        nFeminino=nFeminino+1
        idadeF=idadeF+(int(input("Informe sua idade: ")))

#Média da idade das Mulheres
mediaIdadeF = (idadeF/nFeminino)
#Média da idade dos Homens
mediaIdadeM = (idadeM/nMasculino)
#Média de idade do grupo
mediaGrupo = ((idadeM+idadeF)/(nMasculino+nFeminino))
print("A média de idade das Mulheres foi de ", "%.2f" % mediaIdadeF," já a dos Homens foi de ", "%.2f" % mediaIdadeM," e a média de idade total do grupo foi de", "%.2f" % mediaGrupo)
   
    
       
        
    
