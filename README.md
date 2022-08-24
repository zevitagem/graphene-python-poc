# Sobre
Uma simples aplicação **Python** usando a biblioteca Graphene para realizar consultas e escritas no formato GraphQL.

# Subir a aplicação com docker-compose
```shell
docker compose up -d --build

[+] Running 1/1
 ⠿ Container python-server  Started
```

# Subindo a aplicação manualmente
```shell
$ docker build -t python-server-image .

$ docker run -p 8080:8082 \
    --mount type=bind,src=$(pwd)/source,dst=/usr/src/app/source \ 
    -it \
    --name python-server python-server-image
```

# Subindo a aplicação sem docker
```shell
$ python3 source/main.py
```

```
Server started http://0.0.0.0:8082
```

-----

# Como testar
- http://localhost:8082/mutation?name=jose&type=Droid&hability=sleep

```json
{
	"CreateHero": {
		"id": "4",
		"name": "Jose",
		"type": "Droid",
		"languages": [{
			"description": "droid_language",
			"native": True
		}],
		"hability": "sleep"
	}
}
```

- http://localhost:8082/query?id=1 => Droid

```json
{
	"hero": {
		"id": "1",
		"name": "Droid: one",
		"type": "Droid",
		"languages": [{
			"description": "droid_language",
			"native": True
		}],
		"hability": "eat"
	}
}
```


- http://localhost:8082/query?id=12 => Developer

```json
{
	"hero": {
		"id": "5",
		"name": "Dev: two",
		"type": "Developer",
		"languages": [{
			"description": "javascript",
			"native": False
		}],
		"company": "apple"
	}
}
```

## Referências
- https://graphene-python.org/
- https://www.python.org/
- https://graphql.org/