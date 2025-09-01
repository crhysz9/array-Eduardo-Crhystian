# Criando um array (lista) com 5 nomes de colegas da turma
colegas = ["Eduardo", "Neto", "Samuel", "Marcos", "JP"]

# Mostrando o primeiro, segundo e terceiro elemento usando índices
print("Primeiro nome:", colegas[0])
print("Segundo nome:", colegas[1])
print("Terceiro nome:", colegas[2])

# Verificando se um nome está na lista
p1 = input('Pesquise um nome: ')

if p1 in colegas:
    print(f"'{p1}' está na lista.")
    print('LISTA:', colegas)
else:
    print(f"'{p1}' não foi encontrado na lista.")
    print('LISTA:', colegas)
