'''O sistema deve permitir que o cliente:
1. Realize vendas de veículos para a empresa.
2. Alugue veículos da empresa por um período determinado.
3. Compre veículos disponíveis para venda.'''
#-----------------------------------------------
#secção das tuplas e listas.
#Tabela fipe
Cliente={}
Carros = {}
quantidade_carros={
    "CIVIC":1,"FIT":1,"HR-V":1,
    "MOBI":1,"ARGO":1,"TORO":1,
    "ONIX":1,"TRACKER":1,"MONTANA":1
}
lista_fipe = {
    "HONDA":{"CIVIC":100000,"FIT":90000,"HR-V":150000},
    "FIAT":{"MOBI":60000,"ARGO": 75000,"TORO":135000},
    "CHEVROLET":{"ONIX":59000,"TRACKER":95000,"MONTANA":80000}
}
lista_veiculos = {
    "HONDA":["CIVIC","FIT","HR-V"],
    "FIAT":["MOBI","ARGO","TORO"],
    "CHEVROLET":["ONIX","TRACKER","MONTANA"]
}

lista_locação = ["FIT","ONIX","ARGO","MOBI"]

#-----------------------------------------------
#Cadastro do cliente.
#O cliente deve informar seu nome, telefone e saldo disponível no início do sistema.
print("-----CADASTRO DO CLIENTE-----")
nome = str(input("Informe o nome do cliente: "))
telefone = str(input("Informe o telefone do cliente: "))
saldo = float(input("Informe o saldo: "))

Cliente[nome]= f"{nome} -- Telefone: {telefone} -- Saldo: {saldo}"



#----------------------------------------------
#Start do sitema.
#O sistema deve funcionar com base em um menu interativo que permite ao cliente escolher entre venda, aluguel ou compra de veículos.
while True:
    print("------SISTEMA DE COMPRA, VENDA E ALUGUEL DE VEÍCULOS------")
    print("1. Venda\n2. Aluguel\n3. Comprar\n4. Exibir saldo e dados do cliente\n5. SAIR")
    menu = int(input())
    #Secção para vendas
    if menu == 1:
        print(f"-----AUTOMÓVEIS QUE BUSCAMOS COMPRA-----\n{lista_veiculos.keys()}")
        marca_venda = str(input("Informe a marca do carro que deseja vender: ")).upper()
        if marca_venda in lista_fipe:
            print(f"{lista_veiculos[marca_venda]}")
            modelo_venda = (input("Informe o modelo que deseja vender: ")).upper()
                
            if modelo_venda in lista_fipe[marca_venda]:
                    
                valor_fipe = lista_fipe[marca_venda][modelo_venda]
                valor_com_desconto = valor_fipe - (valor_fipe * 0.12)
                print(f"Valor com desconto {valor_com_desconto}")
                confirmar_venda = float(input("Deseja realmente vender o carro?\n1 - SIM\n2 - NÃO\n"))

                if confirmar_venda == 1:
                    saldo += valor_com_desconto
                    print(f"Saldo Atual R$ - {saldo}")
                    #adicionar um item a lsita!!!!
                    att_valor_qtd = quantidade_carros[modelo_venda]
                    quantidade_carros[modelo_venda] = att_valor_qtd + 1
                    print(f"Quantidade atual do modelo {modelo_venda} em estoque apos a venda {quantidade_carros[modelo_venda]} unidades")
                    
                elif confirmar_venda == 2:
                    print("VENDA CANCELADA!!!")
                else:
                    print("VALOR INADEQUADO")
            else:
              print(f"{modelo_venda} não está disponível")               
        else:
            print(f"{marca_venda} não está disponível") 



    #Secção para aluguel
    if menu == 2:
        print(f"CARROS DISPONÍVEIS PARA LOCAÇÃO:\n {lista_locação}")
        alugar = input("Digite o nome do carro que deseja alugar: \n").upper()
        if alugar in lista_locação:
            qtd_dias = int(input(f"Por quantos dias deseja alugar o carro modelo ({alugar})?"))
            custo_aluguel = qtd_dias * 77

            print(f"O custo total do aluguel é R$ - {custo_aluguel:.2f}")
            confirmar_aluguel = int(input("Deseja confirma a locação do carro? (1-S/2-N)"))
            if (alugar in lista_locação) and (confirmar_aluguel == 1) and (saldo >= custo_aluguel):
                saldo -= custo_aluguel
                lista_locação.remove(alugar)
                print("Sucesso")
            elif (alugar not in lista_locação):
                print("Carro indisponível para alugar!!")
            elif (saldo < custo_aluguel):
                print("Saldo insulficiente")
            else:
                print("Locação cancelada!!")
        else:
            print(f"O carro do modelo {alugar} não está disponível!")
    #Secção para Comprar
    if menu == 3:
        print(f"-----AUTOMÓVEIS QUE BUSCAMOS COMPRA-----\n{lista_veiculos.keys()}")
        marca_compra = str(input("Informe a marca do carro que deseja vender: ")).upper()
        if marca_compra in lista_fipe:
            print(f"{lista_veiculos[marca_compra]}")
            modelo_compra = (input("Informe o modelo que deseja vender: ")).upper()
                
            if modelo_compra in lista_fipe[marca_compra] and quantidade_carros[modelo_compra] >= 1:
                    
                valor_fipe = lista_fipe[marca_compra][modelo_compra]
                valor_com_aumento = valor_fipe + (valor_fipe * 0.25)
                print(f"Valor total de compra R${valor_com_aumento}")########
                confirmar_compra = float(input("Deseja realmente comprar o carro?\n1 - SIM\n2 - NÃO\n"))

                if confirmar_compra == 1:
                    saldo -= valor_com_aumento
                    print(f"Saldo Atual R$ - {saldo}")
                    #remover um item da lista!!!!
                    att_valor_qtd = quantidade_carros[modelo_compra]
                    quantidade_carros[modelo_compra] = att_valor_qtd - 1
                    print(f"Quantidade atual do modelo {modelo_compra} em estoque apos a venda {quantidade_carros[modelo_compra]} unidades")
                    print("PARABÉNS PELA AQUISIÇÃO!!!!")
                    
                elif confirmar_compra == 2:
                    print("VENDA CANCELADA!!!")
                else:
                    print("VALOR INADEQUADO")
            else:
              print(f"{modelo_compra} não está disponível!")               
        else:
            print(f"{marca_compra} não está disponível!") 

    #Secção para exibir dados
    if menu == 4:
        print(f"NOME DO CLIENTE: {nome}")
        print(f"TELEFONE PARA CONTATO: {telefone}")
        print(f"SALDO ATUAL DO CLIENTE: {saldo}")


    #Secção para SAIR
    if menu == 5:
        break

