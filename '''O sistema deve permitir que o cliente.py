'''O sistema deve permitir que o cliente:
1. Realize vendas de veículos para a empresa.
2. Alugue veículos da empresa por um período determinado.
3. Compre veículos disponíveis para venda.'''
#-----------------------------------------------
#secção das tuplas e listas.
#Tabela fipe
Cliente={}
Carros = {}
lista_fipe = {
    "HONDA":{"Civic":100000,"FIT":90000,"HR-V":150000},
    "FIAT":{"Mobi":60000,"Argo": 75000,"Toro":135000},
    "CHEVROLET":{"ONIX":59000,"TRACKER":95000,"MONTANA":80000}
}
lista_veiculos = {
    "HONDA":["Civic","FIT","HR-V"],
    "FIAT":[],
    "CHEVROLET":[]
}

#-----------------------------------------------
#Cadastro do cliente.
#O cliente deve informar seu nome, telefone e saldo disponível no início do sistema.
print("-----CADASTRO DO CLIENTE-----")
nome = str(input("Informe o nome do cliente: "))
telefone = str(input("Informe o telefone do cliente: "))
saldo = float(input("Informe o saldo: "))

Cliente[nome]= f"Telefone: {telefone}---Saldo: {saldo}"



#----------------------------------------------
#Start do sitema.
#O sistema deve funcionar com base em um menu interativo que permite ao cliente escolher entre venda, aluguel ou compra de veículos.
while True:
    print("------SISTEMA DE COMPRA, VENDA E ALUGUEL DE VEÍCULOS------")
    print("1. Venda\n2. Aluguel\n3. Comprar\n4. SAIR")
    menu = int(input())
    #Secção para vendas
    


    #Secção para aluguel




    #Secção para Comprar



    #Secção para SAIR
    if menu == 4:
        break

