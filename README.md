# Guia de Build do Projeto

Este repositório contém os arquivos necessários para construir a imagem Docker de um aplicativo web baseado no Tomcat.

## Estrutura de Arquivos

- `config/`: Diretório contendo arquivos de configuração XML.
- `context.xml`: Configurações de contexto Tomcat.
- `Dockerfile`: Arquivo de definição para a construção da imagem Docker.
- `entrypoint.sh`: Script utilizado como ponto de entrada do container.
- `wfre.py`: Script Python que pode ser usado pelo aplicativo.

## Pré-requisitos

Antes de iniciar o processo de build, você precisará ter o Docker instalado em sua máquina. Visite [Docker](https://www.docker.com/get-started) para instruções de instalação.

## Construindo a Imagem Docker

Para construir a imagem Docker, siga estes passos:

1. **Preparação dos Arquivos**: Certifique-se de que todos os arquivos necessários estão na estrutura correta conforme mostrado na árvore do diretório acima.

2. **Construção da Imagem**:
   Abra um terminal e navegue até o diretório raiz onde o Dockerfile está localizado.

   Execute o seguinte comando para construir a imagem Docker:

   ```sh
   docker build -t nome_da_imagem .
   ```

   Substitua `nome_da_imagem` pelo nome que deseja dar à sua imagem Docker.

## Configurando Variáveis de Ambiente

O script `wfre.py` utiliza variáveis de ambiente para configurar a conexão com o banco de dados. Você precisará configurar as seguintes variáveis:

- `WEBRUN_HOST_DB`: Endereço do host do banco de dados.
- `WEBRUN_USER_DB`: Nome de usuário para acesso ao banco de dados.
- `WEBRUN_PASS_DB`: Senha para acesso ao banco de dados.
- `WEBRUN_DB`: Nome do banco de dados.
- `WEBRUN_PORT_DB`: Porta de conexão ao banco de dados.

### Usando Docker Run

Para passar essas variáveis ao iniciar o container, use o comando `docker run` com a opção `-e` para cada variável de ambiente:

```sh
docker run -d -p 8080:8080 \
  -e WEBRUN_HOST_DB=hostname \
  -e WEBRUN_USER_DB=username \
  -e WEBRUN_PASS_DB=password \
  -e WEBRUN_DB=database_name \
  -e WEBRUN_PORT_DB=database_port \
  nome_da_imagem
```

### Usando Docker Compose

Se você estiver usando Docker Compose, inclua as variáveis de ambiente no seu arquivo `docker-compose.yml`:

```yaml
version: '3'
services:
  webapp:
    image: nome_da_imagem
    ports:
      - "8080:8080"
    environment:
      WEBRUN_HOST_DB: hostname
      WEBRUN_USER_DB: username
      WEBRUN_PASS_DB: password
      WEBRUN_DB: database_name
      WEBRUN_PORT_DB: database_port
```

## Executando o Container

Após a construção da imagem e configuração das variáveis de ambiente, você pode iniciar o container usando o comando `docker run` mostrado acima ou através do Docker Compose com:

```sh
docker-compose up -d
```

Este comando irá iniciar o container em modo desacoplado (detached) e mapear a porta 8080 do container para a porta 8080 do host, permitindo que você acesse o aplicativo através do navegador em `http://localhost:8080`.

## Observações

- **Arquivos de Configuração**: Certifique-se de revisar e ajustar os arquivos de configuração em `config/` conforme necessário antes do build.
- **Scripts Customizados**: O `entrypoint.sh` e `wfre.py` podem necessitar ajustes para atender às especificidades do seu ambiente ou da lógica do aplicativo.

Para mais informações sobre a configuração do Tomcat ou detalhes específicos do seu aplicativo, consulte a documentação relevante ou os arquivos de configuração incluídos.