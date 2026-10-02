# TuneShelf

## 1. Nome do Projeto e Descrição

**TuneShelf** é um catálogo pessoal de músicas desenvolvido com Django. O usuário cria uma conta, faz login e pode cadastrar músicas que já ouviu, quer ouvir ou está ouvindo. Cada item pode ter título, artista, álbum, comentário, status, nota e data de adição automática.

## 2. Tecnologias Utilizadas

- Python 3.14
- Django 6.1.1
- SQLite
- CSS próprio

## 3. Pré-requisitos

- Python 3.14 instalado.
- Git instalado.
- Git Bash instalado.
- Visual Studio Code instalado.

Não é necessário instalar banco de dados separado, pois o projeto utiliza SQLite.

## 4. Como Instalar e Rodar

### 4.1 Clonar o projeto

Abra o Git Bash e execute:

```bash
git clone https://github.com/SEU-USUARIO/tuneshelf.git
cd tuneshelf
```

> Se você estiver executando o projeto localmente antes de publicar no GitHub, entre na pasta do projeto com `cd catalogo_musical`.

### 4.2 Criar o ambiente virtual

No Git Bash:

```bash
python -m venv venv
```

Ative o ambiente:

```bash
source venv/Scripts/activate
```

No Git Bash do Windows, o começo da linha deverá mostrar `(venv)`.

### 4.3 Instalar as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4.4 Criar o banco de dados

```bash
python manage.py migrate
```

### 4.5 Criar um usuário administrador (opcional)

```bash
python manage.py createsuperuser
```

Informe usuário, e-mail e senha quando o Django solicitar.

### 4.6 Executar o sistema

```bash
python manage.py runserver
```

Abra no navegador:

```text
http://127.0.0.1:8000/
```

### 4.7 Parar o servidor

No Git Bash:

```text
CTRL + C
```

## 5. Funcionalidades do Sistema

- Cadastro de usuário.
- Login.
- Logout.
- Página principal protegida por autenticação.
- Cadastro de músicas.
- Listagem das músicas do usuário logado.
- Edição de músicas.
- Exclusão de músicas com confirmação.
- Status da música: Ouvida, Quero ouvir ou Estou ouvindo.
- Nota pessoal de 1 a 5.
- Data de adição gerada automaticamente.
- Cada usuário visualiza apenas seus próprios itens.
- CSS próprio separado em `static/css/style.css`.

## 6. Autor

**Mikael Gomes Rodrigues**  
**Tecnico em desenvolvimento de sistemas**

---

## Estrutura principal

```text
tuneshelf/
├── catalogo/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── catalogo_musical/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── catalogo/
│   └── registration/
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Observação

O arquivo `db.sqlite3` é criado localmente depois de executar `python manage.py migrate`. Ele não deve ser enviado ao GitHub, pois está listado no `.gitignore`.
