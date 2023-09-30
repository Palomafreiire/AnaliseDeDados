arquivo = open('exemplodois.txt', 'r', encoding="utf8")
dados = arquivo.read() # faz uma string do arquivo para poder manipular, abriu como READ por conta do r
palavras = dados.split()

arquivo.close() # posso fechar em qualquer lugar


print(dados)
print('quantidade de caracteres', len(dados))
print ("quantidade de palavras: ", len(palavras))

