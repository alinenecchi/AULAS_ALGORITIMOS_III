
class Conta: 
    def __init__(self,codigo,saldo):
        self.codigo = codigo
        self.saldo = saldo


    def depositar(self,valor):
        self.saldo += valor

    def atualizar (self, taxa):
        self.saldo += (self.saldo * taxa)
         
    def sacar (self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            return True
        else:
            print ("Saldo insuficiente.")
            return False

class ContaEspecial(Conta):
    limite = 0.0
    def __init__(self,codigo,saldo,limite):
        self.codigo = codigo
        self.saldo = saldo
        self.limite = limite #cheque especial

    def depositar (self, valor):
        desconto = 0.0035 * valor
        self.saldo += (valor - desconto)
         
    def sacar (self, valor):
        desconto = 0.0035 * valor
        if (self.saldo + self.limite) >= (valor + desconto):
            self.saldo -= (valor + desconto)
            return True
        else:
            print ("Saldo insuficiente.")
            return False
             
    def atualizar (self, taxa):
        self.saldo += (2 * self.saldo * taxa)
         
    def saldoNegativo (self, taxa):
        self.saldo += (self.saldo * taxa)
         
    def imprimeSaldo (self):
        print ("Conta Especial.")
        print ("Conta:", self.codigo)
        print ("Saldo: %.2f" % (self.saldo))
        print ("Limite:",self.limite)
        
    def imprimeConta (self):
        print ("Conta Especial.")
        print ("Conta:", self.codigo)

class ContaComum(Conta):
    def atualizar (self, taxa):
        self.saldo += (3 * self.saldo * taxa)       
    def imprimeSaldo (self):
        print ("Conta Comum.")
        print ("Codigo:", self.codigo)
        print ("Saldo: %.2f" % (self.saldo))
    def imprimeConta (self):
        print ("Conta Comum.")
        print ("Conta:", self.codigo)
        
def relatorio (lC):
    print("Relatorio de Contas")
    if lC == []:# lC listaContas
        print ("Ainda nao existem contas cadastradas.")
    else:
        for conta in lC :
            conta.imprimeSaldo ()
def relatorioExc (lC):
    print("Relatorio para excluir")
    if lC == []:# lC listaContas
        print ("Ainda nao existem contas cadastradas.")
    else:
        for conta in lC :
            conta.imprimeConta()
def devedores (lC):
    for conta in lC:
        if conta.saldo < 0:
            print ("Cliente devedor:", conta.codigo)
        else: 
            print("Não existem registros de clientes devedores")
 
def insereConta (lC):
    tipo = input ("Digite 1 para Conta Especial ou 2 para Comum: ")
    if tipo == '1':
        codigo = int(input ("Digite o codigo da conta: "))
        saldo = int(input ("Digite o saldo inicial: "))
        limite = int(input ("Digite o limite do cliente: "))
        cE = ContaEspecial (codigo, saldo,limite)
        lC.append (cE)#c contaEspecial

    elif tipo == '2':
        codigo = int(input ("Digite o codigo da conta: "))
        saldo = int(input ("Digite o saldo inicial: "))
        
        cC= ContaComum (codigo,saldo)
        lC.append (cC) #contaComum
    else:
        print ("Tipo de conta inexistente.")
 
def excluiConta (lC,numero):
    for conta in lC:
        if conta.codigo == numero:
            lC.remove (conta)
            return
 
def jurosMes (lC):
    taxa = float(input ("Digite uma taxa: "))
     
    for conta in lC:
        conta.atualizar (taxa/100.0)
 
def imprimeMenu ():
    print
    print ("(1) Exibir Relatorio.")
    print ("(2) Incluir nova conta.")
    print ("(3) Excluir conta.")
    print ("(4) Atualizar contas...")
    print ("(5) Clientes devedores.")
    print ("(6) Sacar.")
    print ("(7) Depositar.")
    print ("(8) Sair.")
    print
 
def sacar (lC,codigo, valor):
    for conta in lC:
        if conta.codigo == codigo:
            conta.sacar (valor)
            return
        else: 
            print("Valor invalido")
    print ("Conta invalida.")
 
def depositar (lC, codigo, valor):
    for conta in lC:
        if conta.codigo == codigo:
            conta.depositar (valor)
            return
    print ("Conta invalida.")
 
####################################
## Programa vira' a partir daqui ###
####################################
 
lC = []
 
print ("Seja bem vindo ao Banco xxxx")
imprimeMenu ()
 
opcao = input ("Escolha uma das opcoes acima: ")
 
while opcao     != '8':
    if opcao    == '1':
        relatorio (lC)
    elif opcao  == '2':
        insereConta (lC)
    elif opcao  == '3':
        relatorioExc(lC)
        numero = int(input("Digite o numero da conta: "))
        excluiConta(lC, numero)
    elif opcao  == '4':
        jurosMes (lC)
    elif opcao  =='5':
        devedores (lC)
    elif opcao  == '6':
        relatorioExc(lC)
        codigo  = int(input ("Digite o numero da conta: "))
        relatorio(lC)
        valor   = float(input ("Quanto deseja sacar? "))
        sacar (lC, codigo, valor)
    elif opcao  == '7':
        codigo  = int(input ("Digite o numero da conta: "))
        valor   = float(input ("Quanto deseja depositar? "))
        depositar (lC, codigo, valor)
    else:
        print ("Opção Invalida")

    imprimeMenu()
    opcao = input("Escolha uma das opcoes acima: ")


