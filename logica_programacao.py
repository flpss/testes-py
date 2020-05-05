'''
Para essa abordagem, iremos obter os múltiplos de 3 e 5 separadamente, e depois uní-los usando o conceito de um set.
Note que, em um set, nenhum termo pode se repetir. Por isso é uma abordagem interessante para nós, neste caso.
'''

multiplos = lambda numero, final : [n for n in range(1, final) if n % numero == 0] # essa função gera os números múltiplos até o número final, sem incluir este último
multiplos_desejados = set(multiplos(3, 1000) + multiplos(5, 1000)) #aqui, contatenamos os dois arrays em um set. trabalhar com os dados dessa forma garante que multiplos de 3 e 5 (15, por exemplo), se repitam
print("Soma dos múltiplos:", sum(multiplos_desejados)) #agora, basta chamar o método sum para somar todos os itens do set