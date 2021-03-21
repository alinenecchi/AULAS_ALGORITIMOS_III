class Aluno():
    nome = ''
    curso = ''
    matricula = 0
    notas = [0,0,0,0]
    def __init__(self,nome,curso,matricula):
        self.nome  = nome
        self.curso = curso
        self.matricula = matricula
        
    def rec_nome(self):
       return self.nome
    
    def rec_notas(self,semestre,nota):
        self.notas[semestre]= nota

    def rec_media(self):
        notas = 0
        media = 0
        i = 0
        while (i < 4):
            notas += self.notas[i]
            i+=1
        media = notas/4
        return media 
# Iniciando o programa
nome        = str(input("Nome do aluno: "))
curso       = str(input("Curso: "))
matricula   = str(input("Matricula: "))
aluno = Aluno(nome=nome, curso=curso, matricula = matricula)
i = 0

while (i < 4):
    Nota = float(input("Digite a %sª nota: " % str(i+1)))
    aluno.rec_notas(semestre=i, nota=Nota)
    i += 1

print("O aluno %s terminou o ano com média %f" % (aluno.rec_nome(),aluno.rec_media()))