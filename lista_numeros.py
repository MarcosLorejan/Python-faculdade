lista_numeros = [int(valor) for valor in input().split(",")]

print(lista_numeros)
print(sorted(lista_numeros))
print(sorted(lista_numeros, reverse=True))
print(sum(lista_numeros))
print(sum([valor for valor in lista_numeros if valor % 2 == 0]))
print(sum([valor for valor in lista_numeros if valor % 2 > 0]))