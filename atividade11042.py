#Faça um programa em python que solicite um código referente ao tipo da diária de hospedagem e também a quantidade de diárias desejadas por um cliente. calcule e mostre usando estrutura condicional aninhada, o valor total a pagar pelo cliente conforme a tabela abaixo:

#Tipo de diária | Quarto  | Valor da diária
#S                Simples    225.50
#D                Duplo      305.50
#T                Triplo     360.50



codDiaria =  (input("Digite o tipo do quarto \nS - Simples \nD - Duplo \nT - Tripla:"))
qtdiaria =  int(input("Digite a quantidade de diarias:"))


if codDiaria == "S" or "s":
    print("Tipo de quarto simples", "Total a pagar:", qtdiaria * 255.50)
elif  codDiaria == "D" or "d":
    print("Tipo de quarto duplo", "Total a pagar", qtdiaria * 305.50)
elif codDiaria == "T" or "t":
    print("Tipo de quarto triplo", "Total a pagar", qtdiaria * 360.50)
else:
    print("Tipo da diaria invalido! Digite S para quarto simples, D para quarto Duplo ou T para quarto triplo")