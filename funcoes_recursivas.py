'''
Aqui, desejamos saber qual o MENOR número inteiro divisível por 2, 3 e 10 ao mesmo tempo. Dessa forma, basta criar uma função recursiva começando do 1, retornando o primeiro número encontrado que divida os três números ao mesmo tempo.
'''
def divisivel(numeros, atual=1):
    numeros_divisiveis = list(filter(lambda x: atual % x == 0, numeros)) #aqui filtramos o array de números, colocando no novo array APENAS os números que são divisíveis
    return divisivel(numeros, atual+1) if len(numeros_divisiveis) != len(numeros) else atual #caso o número de divisíveis não seja idêntico ao conjunto original, incrementamos o valor do 'atual'; caso contrário, o atual é o valor que desejamos encontrar

print(divisivel([2,3,10]))