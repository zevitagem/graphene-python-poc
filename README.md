# Sobre
Uma simples aplicação **Python** usando Docker.

Com o intuito de ajudar quem também está começando em PYTHON, foi construído esse material e repositório sobre *COMO CONSTRUIR UM SERVER WEB EM PYTHON USANDO DOCKER*.

A ideia desse projeto não é englobar todas as coisas possíveis de serem utilizadas e implementadas, a ideia principal é termos um ambiente básico que:
- Aceite e interprete requisições HTTP usando bibliotecas nativas;
- Tenha isolamento e algum controle de dependência como qualquer outro projeto;
- Realize o nosso famoso "Hello World!" sem crise.

# Subir a aplicação com docker-compose
```shell
docker compose up -d --build

[+] Running 1/1
 ⠿ Container cgi-python-web  Started
```

# Subindo a aplicação manualmente
```shell
$ docker build -t cgi-python .

$ docker run -p 8080:8080 \
    --mount type=bind,src=$(pwd)/source,dst=/usr/src/app/source \ 
    -it \
    --name cgi-python-web cgi-python
    
Server started http://0.0.0.0:8080
```

# Como testar
Tenha certeza de que sua aplicação está realmente de pé, então:

Acesse o navegador e digite, por exemplo, a `URL`: http://localhost:8080/zetest

```shell
172.17.0.1 - - [09/Aug/2022 20:16:34] "GET /zetest HTTP/1.1" 200 -
```

---
## Observações
- A pasta `source` está sendo observada, ou seja, todas as alterações que forem realizadas localmente dentro dessa pasta, serão automáticamente refletidas para dentro do `container`.
- Se quiser experimentar a maneira "manual/raw", vá para o ramo "**docker-raw-config**" e execute por lá.
- A única diferença do ramo "**docker-raw-config**" para o "**main**" é a exposição da PORTA 8080: https://github.com/zevitagem/web-python-poc/pull/2/files

## Referências
- https://pythonbasics.org/webserver/
- https://hub.docker.com/_/python
- https://docs.docker.com/compose/compose-file/compose-file-v3/
- https://docs.docker.com/engine/reference/commandline/run/

## Urls
http://localhost:8082/mutation?name=jose&type=Droid&hability=sleep

http://localhost:8082/query?id=1 => Droid
http://localhost:8082/query?id=12 => Developer