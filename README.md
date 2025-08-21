# Sistema de Gestão de Serviços

Este é um sistema de gestão de serviços desenvolvido com Streamlit para controle e relatórios de serviços prestados.

## Requisitos

- Python 3.9 ou superior
- Dependências listadas em `requirements.txt`

## Instalação Local

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd relatorio
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```
   streamlit run app.py
   ```

4. Acesse a aplicação em seu navegador:
   ```
   http://localhost:8501
   ```

## Deploy com Docker

### Construir e Executar Localmente

1. Construa a imagem Docker:
   ```
   docker build -t relatorio-smed:latest .
   ```

2. Execute o contêiner:
   ```
   docker run -p 8501:8501 relatorio-smed:latest
   ```

3. Acesse a aplicação em seu navegador:
   ```
   http://localhost:8501
   ```

### Deploy Automático com GitHub Actions

Este projeto está configurado para deploy automático usando GitHub Actions. Quando você faz push para a branch `main`, o workflow `.github/workflows/docker-deploy.yml` é acionado para:

1. Construir a imagem Docker
2. Fazer login no Docker Hub usando as credenciais armazenadas nos secrets do GitHub
3. Enviar a imagem para o Docker Hub

#### Configuração dos Secrets

Para que o deploy automático funcione, você precisa configurar os seguintes secrets no seu repositório GitHub:

- `DOCKER_USERNAME`: Seu nome de usuário do Docker Hub
- `DOCKER_PASSWORD`: Sua senha ou token de acesso do Docker Hub

#### Como configurar os secrets:

1. Vá para seu repositório no GitHub
2. Clique em "Settings" > "Secrets and variables" > "Actions"
3. Clique em "New repository secret"
4. Adicione os secrets mencionados acima

## Estrutura do Projeto

- `app.py`: Aplicação principal Streamlit
- `db_utils.py`: Funções para interação com o banco de dados
- `reports.py`: Funções para geração de relatórios
- `helpers.py`: Funções auxiliares
- `dados.json`: Dados de configuração da aplicação
- `requirements.txt`: Dependências do projeto
- `dockerfile`: Configuração para construção da imagem Docker
- `.github/workflows/docker-deploy.yml`: Configuração do workflow de CI/CD

## Uso da Aplicação

A aplicação possui as seguintes funcionalidades:

1. **Cadastro**: Adicionar novos serviços
2. **Edição**: Modificar serviços existentes
3. **Exclusão**: Remover serviços do sistema
4. **Consulta**: Visualizar e filtrar serviços
5. **Relatório**: Gerar relatórios em PDF, Excel ou CSV