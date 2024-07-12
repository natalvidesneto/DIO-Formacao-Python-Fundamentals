idade = input("Digite sua idade:")
print('O valor digitado: '+idade)
print(type(idade))
print(f"O valor é {idade} do tipo {type(idade)}")

ano = int(input("Digite o ano:"))
print(f'O ano digitado {ano} do tipo {type(ano)}')

print('******************************')

nome = "Daemon"
sobrenome = "Targaryen"
print(nome,sobrenome)
print(nome,sobrenome, end="...\n")
print(nome, sobrenome,sep="#")

print('******************************')

print(nome+sobrenome)
print(nome,sobrenome)
print("Daemon Targaryen","Dragão",sep="---",end="......\n")