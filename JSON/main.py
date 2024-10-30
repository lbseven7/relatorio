import json
import os
from collections import defaultdict

# Especifica o diretório onde estão os arquivos JSON
diretorio_json = "C:/Users/Aux Administrativo/Documents/leob/relatorio/JSON/dados"

# Inicializa a contagem total de vagas de professores e lista de professores com observações
total_vagas_com_observacoes = 0
professores_com_observacoes = []
observacoes_por_tipo = defaultdict(set)

# Função para contar e armazenar as vagas de professores que possuem observações
def contar_professores_com_observacoes(dados, chave, instituicao):
    vagas_com_observacoes = []
    if chave in dados and dados[chave]:
        for item in dados[chave]:
            observacao = item.get("observacoes")
            if observacao and isinstance(observacao, str) and observacao.strip():  # Verifica se a observação não está vazia
                item["instituicao"] = instituicao  # Adiciona o nome da instituição ao item
                vagas_com_observacoes.append(item)
    return vagas_com_observacoes

# Percorre todos os arquivos no diretório JSON
for nome_arquivo in os.listdir(diretorio_json):
    if nome_arquivo.endswith('.json'):
        caminho_json = os.path.join(diretorio_json, nome_arquivo)

        # Carrega o arquivo JSON
        try:
            with open(caminho_json, 'r', encoding='utf-8') as arquivo_json:
                dados = json.load(arquivo_json)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar o arquivo JSON '{nome_arquivo}': {e}")
            continue

        # Verifica se os dados foram carregados corretamente
        if not dados:
            print(f"Arquivo '{nome_arquivo}' está vazio ou não foi carregado corretamente.")
            continue

        instituicao = dados.get("escola")
        if not instituicao:
            instituicao = "Instituição desconhecida"

        # Conta as vagas nas chaves "docentes", "professores_desdobrados" e "professores" que possuem observações
        servidores_efetivos = dados.get("servidores_efetivos", {})
        professores_com_observacoes.extend(contar_professores_com_observacoes(servidores_efetivos, "docentes", instituicao))
        professores_com_observacoes.extend(contar_professores_com_observacoes(servidores_efetivos, "professores_desdobrados", instituicao))

        servidores_contratados = dados.get("servidores_contratados", {})
        professores_com_observacoes.extend(contar_professores_com_observacoes(servidores_contratados, "professores", instituicao))

# Calcula o total de vagas com observações
total_vagas_com_observacoes = len(professores_com_observacoes)

# Classifica as observações por tipo
for professor in professores_com_observacoes:
    nome = professor.get("nome", "Desconhecido")
    observacoes = professor.get("observacoes", "Nenhuma observação")
    instituicao = professor.get("instituicao", "Instituição desconhecida")
    observacoes_por_tipo[observacoes].add((nome, instituicao))

# Exibe o total de vagas de professores com observações
print(f"Total de vagas reais de professores com observações: {total_vagas_com_observacoes}")

# Exibe as informações dos professores que têm observações
for tipo, infos in observacoes_por_tipo.items():
    print(f"Observação: {tipo}")
    for nome, instituicao in infos:
        print(f"  Nome: {nome}, Instituição: {instituicao}")

# Salva as informações dos professores com observações em um arquivo de saída
with open("professores_com_observacoes.txt", 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(f"Total de vagas reais de professores com observações: {total_vagas_com_observacoes}\n\n")
    for tipo, infos in observacoes_por_tipo.items():
        arquivo_saida.write(f"Observação: {tipo}\n")
        for nome, instituicao in infos:
            arquivo_saida.write(f"  Nome: {nome}, Instituição: {instituicao}\n")
