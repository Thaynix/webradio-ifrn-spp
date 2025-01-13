# RÁDIO IFRN-SPP

## Sobre
O Sistema da rádio IFRN-SPP é um sistema web desenvolvido em Django, com o objetivo de facilitar o gerenciamento e divulgação das atividades da rádio escolar.

---

## Instalação

### Configurando o ambiente

1. **Clone o repositório**:

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente virtual**:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source .venv/bin/activate
     ```

### Configurando sua máquina

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Realize as migrações**:
   ```bash
   python manage.py migrate
   ```

### Rodando o servidor

1. **Crie um superusuário** (opcional para acessar o painel administrativo):
   ```bash
   python manage.py createsuperuser
   ```

2. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```

3. **Acesse a aplicação localmente**:
   - URL: [localhost:8000](http://localhost:8000)

---

## Funcionalidades
- Gerenciamento de programas da rádio.
- Cadastro alunos bolsistas e orientadores do projeto.
- Painel administrativo para controle geral.

