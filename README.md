# biblioteca

Projeto desenvolvido para gerenciamento de empréstimo de livro

## Tecnologias

- python
- django
- sqlite3
- html
- css
- bootstrap.js

## Pré-requisitos

- Python (version 3.6 or higher)
- pip (Python package installer)

## Instalação

1. Clone o repositório:

   ```bash
   git@github.com:deamelo/biblioteca.git
   ```

2. No diretório do projeto:

   ```bash
   cd biblioteca
   ```

3. Crie o ambiente virtual:

   - Windows:

     ```bash
     python -m venv .venv
     ```

   - Linux:

     ```bash
     python3 -m venv .venv
     ```

4. Ativação do ambiente virtual:

   - macOS e Linux:

     ```bash
     source venv/bin/activate
     ```

   - Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

5. Instalação das dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Rode o projeto

```bash
python3 manage.py runserver
```

**Website**: `localhost:8000`

**Rotas de acesso**:

- Cadastro: `/auth/cadastro/`
- Login: `/auth/login`
