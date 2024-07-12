# Estruturas de Repetição

print("**************")

print("Comando FOR\n")
texto = "Nome de Usuário"
for letra in texto:
    print(f"Letra: {letra}")

print("**************")

print("Função Range\n")
for numero in range(0,11):
    print(numero)
for numero in range(0,51,5):
    print(numero, end="  ")

print("**************")

print("Comando While")

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Extrato...")