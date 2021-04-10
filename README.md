# Rodando o projeto

Para rodar o projeto, o jeito mais fácil é usando `docker-compose`

## Rodando

```
docker-compose up -d
```

Em seguida abra 

http://0.0.0.0:8004

Para ver a documentação da API

http://0.0.0.0:8004/docs/

## Encerrando

```
docker-compose down
```

# Deploy no Heroku


Criando aplicativo

```
heroku apps:create nome-do-meu-app
```

Para facilitar um pouco, criaremos a variável `APP` com o mesmo nome dado anteriormente

```bash
APP=nome-do-meu-app
```

Inicializando o repositório no diretório

```bash
git init
heroku git:remote -a $APP
```

Commits

```bash
git add .
git commit -m "Primeiro commit incrível"
```

Para produção de app não podemos deixar variáveis de ambiente visíveis. Neste passo, você precisará abrir uma conta no MongoDB (veja a primeira referência). Um exemplo

```bash
heroku config:set MONGODB_URI='mongodb+srv://<user>:<password>@cluster0.tgicj.mongodb.net/<database>?retryWrites=true&w=majority' -a $APP
```

Empurrando as mudanças para o repositório remoto

```bash
git push heroku master
```

OBS: Caso queira escolher a versão do Python, modifique o arquivo `runtime.txt`

## Deploy com Dockerfile

Os passos anteriores usam a stack Heroku para subir nosso app. Há também a possibilidade de trocar a stack para Container.

Caso opte por container

```
heroku stack:set container
```

A imagem será construida de acordo com o arquivo `heroku.yml`

Considerando os passos anteriores, para empurrar as mudanças 

```bash
git push heroku master
```


# Referências

- https://testdriven.io/blog/fastapi-mongo/
- https://testdriven.io/courses/tdd-fastapi/getting-started/
- https://devcenter.heroku.com/articles/build-docker-images-heroku-yml