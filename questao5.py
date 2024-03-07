#inverter string

palavras = ["maçã","visto","acordado","terrestre","lua","cimento"]

nova_saida = []
for palavra in palavras:
    nova_palavra = palavra[::-1]
    nova_saida.append(nova_palavra)

print("Original: ", palavras)
print("Ao contrário: ",nova_saida)
