from data import Data

if __name__ == '__main__':
    
    def verificaData():
        print("Digite uma data")
        dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
        dataP= int(dia),int(mes),int(ano)
        data = Data._valida(dataP)
        print("{}/{}/{}".format(dia,mes,ano))
        if data == True:
            print("Data valida")
        else:
            print("Data invalida")
            
    def verificaBisexto():
        print("Digite um ano")
        ano = int(input("Ano:"))
        data = Data._bisexto(ano)
        print(ano)
        print(data)
        if data == True:
            print("Este ano é bisexto")
        else:
            print("Este ano não é bisexto")
        
    def verificarPasca():# fonte de pesquisa utilisada https://pipeless.blogspot.com/2008/10/calculando-data-da-pscoa-em-python.html
        ano = int(input('Digite o ano desejado para calcularmos o dia da páscoa: '))
        a = int(ano % 19)
        b = int(ano / 100)
        c = int(ano % 100)
        d = int(b / 4)
        e = int(b % 4)
        f = int((b + 8) / 25)
        g = int((b - f + 1) / 3)
        h = ((19 * a + b - d - g + 15) % 30)
        i = int(c / 4)
        k = int(c % 4)
        L = ((32 + 2 * e + 2 * i - h - k) % 7)
        m = int((a + 11 * h + 22 * L) / 451)
        mes = int((h + L - 7 * m + 114) / 31)
        if mes == 1:
            mes = 'Janeiro'
        elif mes == 2:
            mes = 'Fevereiro'
        elif mes == 3:
            mes = 'Março'
        elif mes == 4:
            mes = 'Abril'
        elif mes == 5:
            mes = 'Maio'
        elif mes == 6:
            mes = 'Junho'
        elif mes == 7:
            mes = 'Julho'
        elif mes == 8:
            mes = 'Agosto'
        elif mes == 9:
            mes = 'Setembro'
        elif mes == 10:
            mes = 'Outubro'
        elif mes == 11:
            mes = 'Novembro'
        else:
            mes = 'Dezembro'
        mes1 = mes
        dia = (((h + L - 7 * m + 114) % 31) + 1)
        print(" A pascoa do ano de {} foi dia {} de {}.".format(ano, dia, mes1))

    def escreverExtenso():
        dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
        meses = ['janeiro', 'fevereiro', 'março', 'abril',
                 'maio', 'junho', 'julho', 'agosto', 'setembro',
                 'outubro', 'novembro', 'dezembro']
        print('Data:')
        print('%s de %s de %s' % (dia, meses[int(mes) - 1], ano))

def imprimeMenu ():
    print ("(1) Teste data valida.")
    print ("(2) Teste ano bisexto.")
    print ("(3) Teste data por extenso.")
    print ("(4) Teste data Pascoa.")
    print ("(0) Sair.")

imprimeMenu()
opcao = input("Escolha uma das opcoes acima: ")
while opcao != '0':
    if opcao == '1':
        verificaData()
    elif opcao == '2':
        verificaBisexto()
    elif opcao == '3':
        escreverExtenso()
    elif opcao == '4':
        verificarPasca()
    else:
        print("Opção Invalida")

    imprimeMenu()
    opcao = input("Escolha uma das opcoes acima: ")
