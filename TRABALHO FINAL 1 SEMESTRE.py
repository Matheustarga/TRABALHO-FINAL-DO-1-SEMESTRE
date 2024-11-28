'''O sistema deve permitir que o cliente:
1. Realize vendas de veículos para a empresa.
2. Alugue veículos da empresa por um período determinado.
3. Compre veículos disponíveis para venda.'''
#-----------------------------------------------
#secção das tuplas e listas.
#Tabela fipe

# Listas contendo respectivamente a quantidade de carros em estoque. A lista com os valores de cada carro com divisões por marca. listas com os nomes dos veiculos
#para fins visuais, a lista de locação é utilizada para verificar a disponibilidade do modelo.
quantidade_carros={
   "CIVIC":1,"FIT":1,"HR-V":1,
    "MOBI":1,"ARGO":1,"TORO":1,
    "ONIX":1,"TRACKER":1,"MONTANA":1,
    "COROLLA":1,"CROSS":1,"SW4":1,
    "KICKS":1,"FRONTIER":1,"SENTRA":1
}
lista_fipe = {
    "HONDA":{"CIVIC":100000,"FIT":90000,"HR-V":150000},
    "FIAT":{"MOBI":60000,"ARGO": 75000,"TORO":135000},
    "CHEVROLET":{"ONIX":59000,"TRACKER":95000,"MONTANA":80000},
    "TOYOTA":{"COROLLA":155000,"CROSS":180000,"SW4":380000},
    "NISSAN":{"KICKS":115000,"FRONTIER":240000,"SENTRA":160000}
}
lista_veiculos = {
    "HONDA":["CIVIC","FIT","HR-V"],
    "FIAT":["MOBI","ARGO","TORO"],
    "CHEVROLET":["ONIX","TRACKER","MONTANA"],
    "TOYOTA":["COROLLA","CROSS","SW4"],
    "NISSAN":["KICKS","FRONTIER","SENTRA"]
}

lista_locação = {
    "HONDA":["CIVIC","FIT","HR-V"],
    "FIAT":["MOBI","ARGO","TORO"],
    "CHEVROLET":["ONIX","TRACKER","MONTANA"],
    "TOYOTA":["COROLLA","CROSS","SW4"],
    "NISSAN":["KICKS","FRONTIER","SENTRA"]
}

#-----------------------------------------------
#Cadastro do cliente.
#O cliente deve informar seu nome, telefone e saldo disponível no início do sistema.
print("-----CADASTRO DO CLIENTE-----")
nome = str(input("Informe o nome do cliente: "))
telefone = str(input("Informe o telefone do cliente: "))
saldo = float(input("Informe o saldo: "))

#----------------------------------------------
#Start do sitema.
#O sistema deve funcionar com base em um menu interativo que permite ao cliente escolher entre venda, aluguel ou compra de veículos.
#O menu interarivo baseia-se em um LOOP principal que é quebrado quando o user solicita.
while True:
    #Mensagem padra do menu para selecionar a funcionalidade/secção desejada.
    print("------SISTEMA DE COMPRA, VENDA E ALUGUEL DE VEÍCULOS------")
    print("1. Venda\n2. Aluguel\n3. Comprar\n4. Exibir saldo e dados do cliente\n5. SAIR")
    menu = int(input())
    #Secção para vendas
    #no primeiro momento dessa secção é apresentada ao usuário as marcas de carros que a empresa trabalha, logo após o usuário deve digitar a marca para que seja realizada a verificação se a marca desejada está presente no portifólio da empresa
    #após isto, são apresentados os modelos da marca escolhida pelo usuário e novamente ele deve digitar o modelos desejado
    #com isso será aplicada da regra de negócio e será exibido o valor da venda e exibido o valor, depois será solicitado uma confirmação de venda para o usuário
    # caso seja confirmada a venda, será acrescentado o valor no saldo do cliente, se adicionar o carro a lista de estoque.
    if menu == 1:
        print(f"-----AUTOMÓVEIS QUE BUSCAMOS COMPRA-----\n{lista_veiculos.keys()}")
        marca_venda = str(input("Informe a marca do carro que deseja vender: ")).upper()
        if marca_venda in lista_fipe:
            print(f"{lista_veiculos[marca_venda]}")
            modelo_venda = (input("Informe o modelo que deseja vender: ")).upper()
                
            if modelo_venda in lista_fipe[marca_venda]:
                    
                valor_fipe = lista_fipe[marca_venda][modelo_venda]
                valor_com_desconto = valor_fipe - (valor_fipe * 0.12)
                print(f"Valor Total: {valor_com_desconto}")
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
    #Nesta secção será apresentado ao usuário os carros com disponibilidade de locação, onde o mesmo deverá buscar 1º a marca do carro desejado e 2º o modelo do carro, caso os dois valores
    #estiverem contidos nas listas o sistema pergunta a quantidade de dias que sera realizada a locação. Adiante será realizada a equação para calcular o valor do aluguel.
    #Com isso será exibida uma mensagem contendo o valor do aluguel e será solicitada a confirmação do usuário.
    #caso seja confirmado, o valor da locação sera debitado do saldo do usuário, o carro será retirado da lista de carros com disponibilidade para locaçao e será exibida uma mensagem de confirmação
    if menu == 2:
        print(f"CARROS DISPONÍVEIS PARA LOCAÇÃO:\n {lista_locação.keys()}")
        alugar_marca = input("Digite a marca do carro que deseja alugar: \n").upper()
        if alugar_marca in lista_locação:
            print(f"Lista dos carros disponíveis para locação:\n{lista_locação[alugar_marca]}")
            alugar_modelo = input("Digite o modelo que deseja alugar: ").upper()
            if alugar_modelo in lista_locação[alugar_marca]:

                qtd_dias = int(input(f"Por quantos dias deseja alugar o carro ({alugar_marca})({alugar_modelo})?"))
                custo_aluguel = qtd_dias * 77

                print(f"O custo total do aluguel é R$ - {custo_aluguel:.2f}")
                confirmar_aluguel = int(input("Deseja confirma a locação do carro? (1-S/2-N)"))
                if (alugar_marca in lista_locação) and (alugar_modelo in lista_locação[alugar_marca]) and (confirmar_aluguel == 1) and (saldo >= custo_aluguel):
                    saldo -= custo_aluguel
                    lista_locação[alugar_marca].remove(alugar_modelo)
                    print("Locação realizada com Sucesso!!!")
                elif (alugar_modelo not in lista_locação[alugar_marca]):
                    print("Carro indisponível para alugar!!")
                elif (saldo < custo_aluguel):
                    print("Saldo insulficiente")
                else:
                    print("Locação cancelada!!")
            else:
                print(f"O modelo {alugar_modelo} não está disponível")       
        else:
            print(f"A marca {alugar_marca} não está disponível!")
    #Secção para Comprar
    #utiliza os mesmos parametros de filtro e busca que as secções anteriores, a diferença aqui fica na regra de negócio, pois aqui é retirado do estoque da empresa o carro comprado
    #o valor da compra é debitado do saldo do cliente, e por fim é exibida a mensagem de confirmação de compra.
    if menu == 3:
        print(f"-----AUTOMÓVEIS QUE BUSCAMOS COMPRA-----\n{lista_veiculos.keys()}")
        marca_compra = str(input("Informe a marca do carro que deseja comprar: ")).upper()
        if marca_compra in lista_fipe:
            print(f"{lista_veiculos[marca_compra]}")
            modelo_compra = (input("Informe o modelo que deseja comprar: ")).upper()
                
            if modelo_compra in lista_fipe[marca_compra] and quantidade_carros[modelo_compra] >= 1:
                    
                valor_fipe = lista_fipe[marca_compra][modelo_compra]
                valor_com_aumento = valor_fipe + (valor_fipe * 0.25)
                print(f"Valor total de compra R${valor_com_aumento}")
                confirmar_compra = float(input("Deseja realmente comprar o carro?\n1 - SIM\n2 - NÃO\n"))

                if confirmar_compra == 1:
                    saldo -= valor_com_aumento
                    print(f"Saldo Atual R$ - {saldo}")
                    #remover um item da lista!!!!
                    att_valor_qtd = quantidade_carros[modelo_compra]
                    quantidade_carros[modelo_compra] = att_valor_qtd - 1
                    print(f"Quantidade atual do modelo {modelo_compra} em estoque apos a compra {quantidade_carros[modelo_compra]} unidades")
                    print("PARABÉNS PELA AQUISIÇÃO!!!!")
                    
                elif confirmar_compra == 2:
                    print("COMPRA CANCELADA!!!")
                else:
                    print("VALOR INADEQUADO")
            else:
              print(f"{modelo_compra} não está disponível!")               
        else:
            print(f"{marca_compra} não está disponível!") 

    #Secção para exibir dados
    #Informa os dados do cliente digitados posteriormente, assim como o saldo sempre atualizado com base nas operações realizadas.
    if menu == 4:
        print(f"NOME DO CLIENTE: {nome}")
        print(f"TELEFONE PARA CONTATO: {telefone}")
        print(f"SALDO ATUAL DO CLIENTE: {saldo}")


    #Secção para SAIR
    if menu == 5:
        print("FINALIZANDO O SISTEMA......")
        break
        
