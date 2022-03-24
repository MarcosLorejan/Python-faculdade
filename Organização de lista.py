numeros = []

def inicio():

 numeros = (input("Adicione Valores a Lista: ").split())

 numeros = [int(x) for x in numeros]

 print("Lista Inicial", numeros, sep='\n')

 numeros_crescente = sorted(numeros)

 print("Lista em ordem crescente", numeros_crescente, sep='\n')

 numeros_decrescente = sorted(numeros, reverse=True)

 print("Lista em ordem decrescente", numeros_decrescente, sep='\n')

 
 print("Soma dos números da Lista", sum(numeros), sep='\n')

 pares = 0

 for i in numeros:
    if not i % 2:
        pares += i

 print("Soma dos números pares da Lista", pares, sep='\n')
 
 impares = 0

 for i in numeros:
    if i % 2:
        impares += i

 print("Soma dos números impares da Lista", impares, sep='\n')

 again()

def again():
 
 restart = input("Deseja adicionar novos valores?(1) para sim,(2) para não: ")
 
 if restart == "1": 
        
        inicio()
        

 elif restart == "2":
        print("Até Mais!")
        exit()

inicio()





    












