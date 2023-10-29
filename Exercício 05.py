## Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
## A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
## A mensagem "Reprovado", se a média for menor do que sete;
## A mensagem "Aprovado com Distinção", se a média for igual a dez.

NotaUm = float(input('Entre com a primeira nota. Entre 0 e 10. '))
NotaDois = float(input('Entre com a segunda nota. Entre 0 e 10. '))

Média = (NotaUm + NotaDois) / 2

if Média >= 7 and Média < 10:
    print('A média foi {} e você foi aprovado.'.format(Média))
elif Média < 7:
    print('A média foi {} e você foi reprovado. '.format(Média))
else:
    print('A sua média foi 10 e você foi aprovado com distinção. ')
