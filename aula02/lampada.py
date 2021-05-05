class Lampada:
    def _init_(self):
        self.botao = 0
        self.carga= 0
   
    def ligar(self):
        self.carga= 1
        input("Luz ligada")
    
    def desligar(self):
        self.carga = 0
        input("Luz desligada")
   
    def aperta_botao(self):
        self.status()
        if self.carga == 0:
            self.carga = 1
            print("Você ligou a lampada")
        else:
            self.carga = 0
            print("Você desligou a lampada")
    def status(self):
        if self.carga == 0:
            return "APAGADA"
        else:
            return "LIGADA"
    
    
lampada = Lampada()

while True:
    print(lampada)
    escolha = input(""" 

    Controle da lampada 
    1- Deixa lampada ligada
    2- Deixa lampada desligada
    3- Verifica se a lampada esta ligada ou desligada 
    4- Aperta o botão (mudança de estado) 
    Escolha: """)

    if escolha == '1':
        lampada.ligar()
    if escolha == '2':
        lampada.desligar()
    if escolha == '3':
        lampada.status()
    if escolha == '4':
        lampada.aperta_botao()
    