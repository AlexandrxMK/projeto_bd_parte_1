# 🍻 Sistema de Gerenciamento de Bar

## 📖 Descrição

Este projeto é um **sistema simples de gerenciamento de estoque e vendas para um bar**, desenvolvido em **Python** com integração ao **MySQL**.

O sistema permite **cadastrar bebidas, gerenciar estoque, registrar vendas e gerar relatórios**, sendo uma aplicação de console criada para a disciplina de **Banco de Dados**.

---

## 🚀 Funcionalidades

O sistema possui as seguintes operações:

* ➕ **Cadastrar bebidas**
* 📋 **Listar todas as bebidas**
* 🔍 **Pesquisar bebida por nome**
* ✏️ **Alterar preço de uma bebida**
* ❌ **Remover bebida do estoque**
* 🆔 **Exibir bebida por ID**
* 📊 **Gerar relatório de estoque**
* 💰 **Registrar venda (atualizando estoque)**

Cada bebida possui os seguintes atributos:

* Nome
* Marca
* Estoque
* Preço
* Data de validade

---

## 🛠 Tecnologias Utilizadas

* **Python 3**
* **MySQL**
* **mysql-connector-python**

---

## 📦 Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/AlexandrxMK/projeto_bd_parte_1.git
```

---

### 2️⃣ Instalar dependências

```bash
pip install mysql-connector-python
```

---

### 3️⃣ Configurar o banco de dados

1. Abra o **MySQL**.
2. Crie o banco de dados:

```sql
CREATE DATABASE BAR;
```

3. Execute o script localizado em:

```
database/bar.sql
```

Esse script irá criar a tabela necessária para o funcionamento do sistema.

---

### 4️⃣ Configurar conexão

Caso necessário, altere as credenciais em:

```
src/conexao.py
```

Configuração padrão:

```
Host: localhost  
Usuário: root  
Senha: (vazia)
```

---

## ▶️ Como Executar

1. Certifique-se de que o **MySQL está rodando**.
2. Navegue até a pasta `src`.

```bash
cd src
```

3. Execute o sistema:

```bash
python main.py
```

---

## 📂 Estrutura do Projeto

```
projeto_bd_parte_1
│
├── database
│   └── bar.sql
│
├── src
│   ├── conexao.py
│   ├── crud.py
│   ├── main.py
│   ├── menu.py
│   └── produtos.py
│
└── README.md
```

Descrição dos arquivos:

| Arquivo            | Descrição                          |
| ------------------ | ---------------------------------- |
| `database/bar.sql` | Script SQL para criação da tabela  |
| `src/conexao.py`   | Conexão com o banco de dados       |
| `src/crud.py`      | Operações CRUD                     |
| `src/main.py`      | Ponto de entrada do programa       |
| `src/menu.py`      | Interface de interação com usuário |
| `src/produtos.py`  | Classe Produto                     |

---

## 👨‍💻 Autores

* **Alexandre Guedes**
* **Mikael Rocha**

---

## 📚 Disciplina

Projeto desenvolvido para a disciplina de **Banco de Dados**.
