# Sistema de Gestão de Serviços

Este é um sistema de gestão de serviços desenvolvido em Python utilizando Streamlit para a interface de usuário e SQLite para o banco de dados. O sistema permite o cadastro, edição, exclusão e consulta de serviços, além da geração de relatórios em PDF e a gestão de tarefas.

## Funcionalidades

- **Cadastro de Serviços**: Permite cadastrar novos serviços fornecendo informações como empresa, serviço, data, setor e quantidade.
- **Edição de Serviços**: Permite editar os serviços cadastrados.
- **Exclusão de Serviços**: Permite excluir serviços cadastrados.
- **Consulta de Serviços**: Permite consultar os serviços cadastrados.
- **Relatório de Serviços**: Permite gerar relatórios em PDF dos serviços cadastrados.
- **Gestão de Tarefas**: Permite adicionar e visualizar tarefas.

## Requisitos

- Python 3.7 ou superior
- Streamlit
- Pandas
- SQLite3
- ReportLab (para geração de PDFs)

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/sistema-gestao-servicos.git
    cd sistema-gestao-servicos
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Inicialize o banco de dados:
    ```sh
    python db_utils.py
    ```

2. Execute a aplicação:
    ```sh
    streamlit run app.py
    ```

3. Acesse a aplicação no navegador através do endereço:
    ```
    http://localhost:8501
    ```

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Streamlit.
- `db_utils.py`: Funções utilitárias para interação com o banco de dados SQLite.
- `reports.py`: Funções para geração de relatórios em PDF.
- `helpers.py`: Funções auxiliares para a aplicação.
- `dados.json`: Arquivo JSON contendo dados estáticos para a aplicação.
- `requirements.txt`: Arquivo de dependências do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.