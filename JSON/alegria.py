import json
import os

# Carrega o JSON das escolas
with open("C:/Users/Aux Administrativo/Documents/leob/relatorio/JSON/todas_as_escolas.json", "r", encoding='utf-8') as f:
    todas_as_escolas = json.load(f)

# Função para mapear professores inativos e calcular vagas reais
def mapear_professores_inativos(escolas):
    resultados = []

    for escola in escolas:
        # Verifica se 'escola' é um dicionário
        if isinstance(escola, dict):
            dados = escola  # Aqui você tem a estrutura JSON de cada escola

            professores_inativos = []

            # Servidores efetivos
            for docente in dados.get("servidores_efetivos", {}).get("docentes", []):
                if "Readaptada" in docente["observacoes"] or "Doutorado" in docente["observacoes"]:
                    professores_inativos.append(docente)

            # Servidores contratados
            professores_contratados = dados.get("servidores_contratados", {}).get("professores", [])
            for professor in professores_contratados:
                if professor["observacoes"]:
                    professores_inativos.append(professor)

            # Cálculo das vagas reais
            servidores_efetivos = dados.get("servidores_efetivos", {}).get("docentes", [])
            vagas_reais_efetivos = len(servidores_efetivos) - len([p for p in servidores_efetivos if "Readaptada" in p["observacoes"] or "Doutorado" in p["observacoes"]])
            
            # Verifica se há professores contratados
            if "servidores_contratados" in dados and "professores" in dados["servidores_contratados"]:
                vagas_reais_contratados = len(professores_contratados) - len([p for p in professores_contratados if p["observacoes"]])
            else:
                vagas_reais_contratados = 0  # Se não houver professores contratados, assume 0 vagas

            total_vagas_reais = vagas_reais_efetivos + vagas_reais_contratados

            # Adiciona resultados
            resultados.append({
                "instituicao": dados.get("instituicao", "Desconhecida"),  # Adicione um valor padrão se não houver
                "professores_inativos": professores_inativos,
                "vagas_reais_efetivos": vagas_reais_efetivos,
                "vagas_reais_contratados": vagas_reais_contratados,
                "total_vagas_reais": total_vagas_reais
            })

    return resultados

# Executa a função
resultados = mapear_professores_inativos(todas_as_escolas)

# Exibe resultados
for resultado in resultados:
    print(f"\nEscola: {resultado['instituicao']}")
    print("Professores inativos:")
    for professor in resultado['professores_inativos']:
        print(f"  Nome: {professor['nome']}, Carga Horária: {professor['ch']}, Observações: {professor['observacoes']}")
    print(f"Vagas reais de professores efetivos: {resultado['vagas_reais_efetivos']}")
    print(f"Vagas reais de professores contratados: {resultado['vagas_reais_contratados']}")
    print(f"Total de vagas reais de professores: {resultado['total_vagas_reais']}")
