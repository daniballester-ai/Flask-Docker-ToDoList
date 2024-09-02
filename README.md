```markdown
# 🚀 Aplicação To-Do List - Flask & Docker

## 📑 Visão Geral

Esta aplicação é um serviço de lista de tarefas (To-Do List) desenvolvido em Python usando o framework Flask. Ela permite que os usuários adicionem, visualizem e removam tarefas. A aplicação foi containerizada utilizando Docker para facilitar a implantação, escalabilidade e persistência de dados.

## 🎯 Objetivos

- **Containerizar a aplicação Flask**: Utilizar Docker para criar um ambiente consistente para execução da aplicação.
- **Definir serviços com Docker Compose**: Facilitar a gestão dos serviços necessários, incluindo o banco de dados.
- **Persistir os dados do banco de dados**: Garantir que os dados armazenados no banco de dados SQLite sejam preservados, mesmo quando os contêineres forem destruídos.
- **Expor a aplicação na porta 5000**: Tornar a aplicação acessível através da porta 5000.

## 📂 Estrutura do Projeto

```plaintext
Flask-Docker-ToDoList/
│
├── main.py                 # Arquivo principal da aplicação Flask
├── models.py               # Definição dos modelos de dados com SQLAlchemy
├── forms.py                # Definição dos formulários com Flask-WTF
├── Dockerfile              # Dockerfile para construção da imagem
├── docker-compose.yml      # Arquivo Docker Compose para orquestrar os serviços
├── requirements.txt        # Dependências da aplicação
├── templates/              # Templates HTML para renderização
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── register.html
└── static/                 # Arquivos estáticos como CSS
    └── style.css
```

## ⚙️ Configuração e Execução

### 1. 💻 Pré-requisitos

É necessário ter o Docker instalado no seu ambiente de desenvolvimento. Para instalar:

- [Instalação do Docker](https://docs.docker.com/get-docker/)

### 2. 📥 Clonagem do Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/daniballester-ai/Flask-Docker-ToDoList.git
cd seu-repositorio
```

### 3. 🏗️ Criação e Configuração da Aplicação Flask

O código da aplicação Flask é definido em `main.py`, `models.py` e `forms.py`. A aplicação usa SQLAlchemy para a manipulação do banco de dados e Flask-WTF para os formulários.

### 4. 🐳 Configuração do Docker

#### 4.1. 🐳 Dockerfile

O `Dockerfile` define o ambiente necessário para rodar a aplicação Flask, incluindo a instalação das dependências e a configuração do servidor web:

#### 4.2. 🐳 Docker Compose

O arquivo `docker-compose.yaml` orquestra os serviços necessários para a aplicação, incluindo o serviço web e o volume persistente para o banco de dados SQLite.

### 5. 🔨 Construção e Execução dos Contêineres

Para construir a imagem Docker e executar os contêineres, siga os passos abaixo:

1. **Construir e iniciar os contêineres**:

Na pasta da aplicação, execute conforme abaixo:

   ```bash
   docker-compose up -d
   ```

   Isso irá:
   - Construir a imagem Docker da aplicação Flask.
   - Iniciar o contêiner da aplicação.
   - Mapear a porta 5000 do contêiner para a porta 5000 do host, tornando a aplicação acessível em `http://localhost:5000`.

2. **Acessar a aplicação**:

   Abra um navegador e acesse `http://localhost:5000`. Você deverá ver a interface da aplicação To-Do List.

### 6. 💾 Persistência de Dados

A aplicação usa um volume Docker (`sqlite_data`) para garantir que os dados do banco de dados SQLite sejam persistentes, mesmo após a destruição dos contêineres.

#### **Demonstração de Persistência**:

1. **Adicionar Tarefas**: Acesse a aplicação e adicione algumas tarefas.
2. **Destruir os Contêineres**:

   ```bash
   docker-compose down
   ```

3. **Reiniciar os Contêineres**:

   ```bash
   docker-compose up -d
   ```

4. **Verificar Persistência**: Ao acessar `http://localhost:5000` novamente, as tarefas adicionadas anteriormente ainda estarão presentes.

### 🏁 Conclusão

Este projeto demonstra a construção e containerização de uma aplicação web simples com Flask, Docker e Docker Compose. O uso de volumes Docker garante que os dados do banco de dados SQLite sejam persistentes, proporcionando uma aplicação robusta e fácil de gerenciar.

Se você tiver alguma dúvida ou quiser contribuir com o projeto, fique à vontade para abrir uma issue ou um pull request no GitHub.

### ⏭️ Próximos Passos

- **Escalabilidade**: Considerar a migração para um banco de dados mais robusto para ambientes de produção.

```
