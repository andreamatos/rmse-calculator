import json
import math

# Função para calcular o RMSE
def calcular_rmse(previsoes, valores_reais):
    # Calcula o erro para cada previsão
    erros = [p - r for p, r in zip(previsoes, valores_reais)]
    # Calcula o quadrado de cada erro
    erros_quadrados = [erro ** 2 for erro in erros]
    # Calcula a média dos erros quadrados
    media_erros_quadrados = sum(erros_quadrados) / len(erros_quadrados)
    # Calcula a raiz quadrada da média dos erros quadrados
    rmse = math.sqrt(media_erros_quadrados)
    return rmse

# Carrega os dados do JSON de entrada
with open('dados_entrada.json', 'r') as f:
    dados_entrada = json.load(f)

previsoes = dados_entrada['P']
valores_reais = dados_entrada['R']

# Calcula o RMSE
rmse = calcular_rmse(previsoes, valores_reais)

# Cria um dicionário com o RMSE
resultado = {'RMSE': rmse}

# Grava o resultado em um JSON de saída
with open('resultado.json', 'w') as f:
    json.dump(resultado, f)

print("RMSE calculado e gravado com sucesso no arquivo 'resultado.json'.")
