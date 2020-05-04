#dados iniciais
array_ufs = ["ES", "MG", "RJ", "SP", "MT"]
arrays_estados = ["Mato Grosso", "São Paulo", "Rio de Janeiro", "Minas Gerais", "Espirito Santo"]

arrays_estados_invertido = arrays_estados[::-1] #array em ordem invertida

estados_agrupados = {uf : arrays_estados_invertido[i] for i, uf in enumerate(array_ufs)} #aqui, juntamos os arrays em um dicionário, em que a chave é o uf e o valor é o nome do estado

for uf, estado in estados_agrupados.items():
    print("{} - {}".format(uf, estado)) #percorremos o novo dicionário, imprimindo o uf e o estado da forma desejada