## Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Letra = input('Digite "M" para masculino ou "F" para feminino. ')
if Letra == 'M':
    print('Sexo masculino.')
elif Letra == 'F':
    print('Sexo feminino.')
else:
    print('Você digitou um caracter inválido.')