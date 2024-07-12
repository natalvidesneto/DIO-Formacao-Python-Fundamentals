# Estruturas condicionais

idade = 27
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

print("---------------------")

saldo = 2000.0
saque = float(input("Informe o valor do saque:"))

if(saldo >= saque):
    print("Realizando saque!")
if saldo < saque:
    print("Saldo insuficiente!")

print("---------------------")

escolhar = int(input("Qual doce deseja escolher:\n1-Doce de leite\n2-Pudim\n3-Doce de goiaba"))
if escolhar==1:
    print("Aproveite o doce de leitie....")
elif escolhar == 2:
    print("aproveite o pudim....")
elif escolhar == 3:
    print("aproveite o doce de goiaba...")
else:
    print("Erro na digitação....")