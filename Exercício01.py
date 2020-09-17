#Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o
#usuário digite um número fora desse intervalo, deverá aparecer uma mensagem
#informando que não existe mês com esse número
meses ={1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro."}
mesCorrespondente = int (input("Digite um valor CORRESPONDENTE aos meses do ano, ou seja, entre 1 e 12: "))
if mesCorrespondente in meses:
    print("Você escolheu o mês: ", meses.get(mesCorrespondente))
else:
    print("Esse número não corresponde aos meses do nosso calendário, amigo!")

