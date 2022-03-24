import csv
import os


print("Menu")
print("1 - Abrir arquivo de configuração")
print("2 - Adicionar arquivo de configuração")
print("3 - Visualizar arquivo de configuração")
print("4 - Sair")


opcao = 0 

while opcao <= 3:

    opcao = int(input("qual o numero da opção? \n"))

    if opcao == 1:

      nome_arquivo = input("Qual o nome do arquivo? \n") #faltou caminho do Arquivo
      arquivo = open(nome_arquivo+".csv", "a", newline='')
      arquivo.write("Nome  ,   IP  ,   Hostname\n")
      print (f"{nome_arquivo} criado com sucesso ")
      arquivo.close()
        
    
    elif opcao == 2:

        try:
          arquivo = open(nome_arquivo+".csv","a", newline='')
          arquivo.write(input("Adicionar Nome, Ip e hostname: (separados por vírgula) \n"))
          arquivo.close()
        except NameError:
          print("Por favor, abra o arquivo de configuração")
    
    elif opcao == 3:
      try:
       
       with open("teste.csv") as visu:
        reader = csv.reader(visu)
        for row in reader:
             print(" ".join(row))
      except NameError:
        print("Por favor, abra o arquivo de configuração")


else:
  print("Até Mais")
         