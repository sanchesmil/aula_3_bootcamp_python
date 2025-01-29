"""
Exercício 1: Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir que todos 
os registros tenham valores positivos para quantidade e preço.
Escreva um programa que verifique esses campos e imprima "Dados válidos" 
se ambos forem positivos ou "Dados inválidos" caso contrário.
"""

# quantidade = 10
# preco = 20

# if (quantidade > 0 and preco > 0):
#     print('Dados válidos')
# else:
#     print('Dados inválidos')

"""
Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar 
cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'
"""

# leitura_atual = int(input('Informe a temperatura: '))

# if leitura_atual < 18:
#     print('Temperatura  BAIXA')
# elif leitura_atual >= 18 and leitura_atual <= 26:
#     print('Temperatura NORMAL')
# else:
#     print('Temperatura ALTA')

"""
Exercício 3: Filtragem de Logs por Severidade
Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
"""

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print('Error: ', log['message'])

"""
Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e 
tenha fornecido um email válido. Escreva um programa que valide essas 
condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""

# usuario = {'idade':20,'email':'sanchesmil@yahoo.com.br'}

# idade = usuario['idade']
# email = usuario['email']

# if not 18 <= idade <= 65:
#     print('Idade inválida.')
# elif '@' not in email or '.' not in email:
#     print('Email inválido.')
# else:
#     print('Dados do usuário são válidos')
   

"""
Exercício 5: Detecção de Anomalias em Dados de Transações
Você está trabalhando em um sistema de detecção de fraude e precisa
identificar transações suspeitas. Uma transação é considerada suspeita 
se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial 
(antes das 9h ou depois das 18h). 
Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

"""

# LIMITE_VALOR = 10000
# LIMITE_HORA_MENOR = 9
# LIMITE_HORA_MAIOR = 18

# transacao = {'valor': 9000,'hora':19}

# if transacao['valor'] > LIMITE_VALOR:
#     print('Esta transação é suspeita por exceder o valor de referência.')
# elif transacao['hora'] < LIMITE_HORA_MENOR or transacao['hora'] > LIMITE_HORA_MAIOR:
#     print('Esta transação é suspeita por ter sido realizada fora do horário comercial.')
# else:
#     print('Transação normal')

"""
6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""
# texto = "a raposa marrom salta sobre o cachorro marrom preguiçoso"
# print(texto)

# palavras = texto.split()

# contador_palavras = {}

# for palavra in palavras:
#     if palavra in contador_palavras:
#         contador_palavras[palavra] = +1
#     else:
#         contador_palavras[palavra] = 1

# print('Quantidade de palavras não repetidas: ' , len(contador_palavras))

"""
7. Normalização de Dados
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
"""
# numeros = [10, 20, 30, 40, 50]

# minimo = min(numeros)
# maximo = max(numeros)

# numeros_normalizados =[(num-minimo)  / (maximo-minimo) for num in numeros]

# print(numeros_normalizados)

"""
8. Filtragem de Dados Faltantes
Objetivo: Dada uma lista de dicionários representando dados de usuários, 
filtrar aqueles que têm um campo específico faltando.

"""

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": ""}
# ]

# usuarios_sem_email = [usuario['nome'] for usuario in usuarios if not usuario['email']]

# print(usuarios_sem_email)

"""
9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
"""
# numeros = range(1, 30)

# numeros_pares = [numero for numero in numeros if numero % 2 == 0]

# print(numeros_pares)

"""
10. Agregação de Dados por Categoria
Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

"""
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800},
#     {"categoria": "livros", "valor": 400},
# ]

# total_por_categoria = {}

# for venda in vendas:
#     categoria = venda['categoria']
#     valor = venda['valor']

#     if categoria not in total_por_categoria:
#         total_por_categoria[categoria] = valor
#     else:
#         total_por_categoria[categoria] += valor

# print(total_por_categoria)
  

"""
Exemplo Prático: while True com Pausa
Um exemplo direto do uso de while True em Python é criar um loop infinito 
que executa uma ação a cada intervalo definido, como imprimir uma mensagem a cada 10 segundos. 
Isso pode ser útil para monitorar processos ou dados em tempo real com uma verificação periódica.
"""
    
# import time

# while True:
#     print('Verificando novos dados ...')

#     time.sleep(3) # pausa a execução do loop por X segundos antes da próxima iteração


"""
11. Leitura de Dados até Flag
Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
"""

# dados = []
# entrada = ''
# while entrada != 'sair':
#     entrada = input("Digite um valor (ou 'sair' para terminar): ").lower()
#     if entrada != 'sair':
#         dados.append(entrada)
# print(dados)

"""
12. Validação de Entrada
Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
"""
# min = 1
# max = 10
# numero = int(input(f'Escolha um número no intervalo de {min} até {max}:'))

# while numero < min or numero > max:
#     print(f'Número {numero} está fora do intervalo [{min} - {max}]')
#     numero = int(input(f'Escolha um número no intervalo de {min} até {max}:'))

# print(f'Número {numero} é válido. Está dentro do intervalo [{min} - {max}]')

"""
13. Consumo de API Simulado
Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

"""
# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Processando página {pagina_atual} de {paginas_totais}")

#     pagina_atual += 1

# print('Todas as páginas foram processadas')

"""
14. Tentativas de Conexão
Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
"""
# tentativa_atual = 1
# limite_tentativas = 5

# while tentativa_atual <= limite_tentativas:
#     print(f"Processando tentativa {tentativa_atual} de {limite_tentativas}")

#     if True:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break

#     tentativa_atual += 1

# else:
#     print('Falha ao conectar após várias tentativas.')

"""
15. Processamento de Dados com Condição de Parada
Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.
"""

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while itens[i] != 'parar':
    print(f"Processando item: {itens[i]}")
    i+=1
else:
    print("Parada encontrada, encerrando o processamento.")