#ler a idade e classificar: até 9 anos: mirim, 9-14: infantil, 14-19: junior, 19-20: sênior, acima: master
idade = int(input('Indique a idade do aluno(a): '))
if idade < 9:
    input ('Devido a idade de {} do inscrito, ele fará parte da turma mirim (abaixo de 9 anos).'.format(idade))
elif idade >= 9 and idade < 14:
    input ('Devido a idade de {} do inscrito, ele fará parte da turma infantil (entre 9 e 13 anos).'.format(idade))
elif idade >= 14 and idade < 19:
    input ('Devido a idade de {} do inscrito, ele fará parte da turma junior (entre 14 e 18 anos).'.format(idade))
elif idade >= 19 and idade == 20:
    input ('Devido a idade de {} do inscrito, ele fará parte da turma sênior (entre 19 e 20 anos.'.format(idade))
elif idade > 20:
    input ('Devido a idade de {} do inscrito, ele fará parte da turma master (acima de 20 anos).'.format(idade))