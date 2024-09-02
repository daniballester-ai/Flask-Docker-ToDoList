# Usando uma imagem oficial do Python como base
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo de dependências para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando todo o conteúdo da aplicação para o diretório de trabalho
COPY . .

# Criando o diretório onde o SQLite armazenará o banco de dados
RUN mkdir -p /app/instance

# Expondo a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]