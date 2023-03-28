aluno=1
nota_impar=0
for alunos_impares in range (1,50,2):
    nota_atual = float(input("Você está digitando as notas dos alunos ímpares.\n Por favor, insira a nota do aluno de número {}: ".format(aluno)))
    aluno = aluno + 2
    nota_impar = nota_impar + nota_atual
    media_impar = nota_impar/25

aluno=2
nota_par=0
for alunos_pares in range (1,50,2):
    nota_atual = float(input("Você está digitando as notas dos alunos pares.\n Por favor, insira a nota do aluno de número {}: ".format(aluno)))
    aluno = aluno + 2
    nota_par = nota_par + nota_atual
    media_par = nota_par/25
print("\nA média de notas dos alunos ímpares foi: {:.2f}.".format(media_impar))
print("\nA média de notas dos alunos pares foi: {:.2f}.".format(media_par))

if media_impar > media_par:
    print("\nA maior nota média foi dos alunos ímpares!")
elif media_par > media_impar:
    print("\nA maior nota média foi dos alunos pares!")
else:
    print("\nHouve empate, os alunos ímpares e pares tiveram a mesma média de notas.")