# Sobre
- Uma simples aplicação **Python**.
- Utilizado a biblioteca Graphene para realizar consultas e escritas no formato GraphQL.
- Aplicado uma leve organização de pastas
- Usado o conceito de `views` para misturar `python code` com linguagem de marcação isoladamente.

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
			"native": true
		}],
		"hability": "sleep"
	}
}
```

- http://localhost:8082/query?id=1 => `Droid`

```json
{
	"hero": {
		"id": "1",
		"name": "Droid: one",
		"type": "Droid",
		"languages": [{
			"description": "droid_language",
			"native": true
		}],
		"hability": "eat"
	}
}
```


- http://localhost:8082/query?id=12 => `Developer` : com parâmetro

```json
{
	"hero": {
		"id": "5",
		"name": "Dev: two",
		"type": "Developer",
		"languages": [{
			"description": "javascript",
			"native": false
		}],
		"company": "apple"
	}
}
```

- http://localhost:8082/list
- http://localhost:8082/query => sem parâmetros

```json
{
	"heroes": [{
		"id": "6",
		"name": "Dev: three",
		"type": "Developer",
		"languages": [{
			"description": "python",
			"native": false
		}],
		"company": "police"
	}, {
		"id": "1",
		"name": "Droid: one",
		"type": "Droid",
		"languages": [{
			"description": "droid_language",
			"native": true
		}],
		"hability": "eat"
	}]
}
```

### Observações
- Todos os dados estão `mocados`, ou seja, NÃO existe persistência alguma dos dados enviados.
- IDS menores ou iguais a 10, serão considerados como `Droids`. Maiores que 10, serão considerados `Devs`.

## Referências
- https://graphene-python.org/
- https://www.python.org/
- https://graphql.org/
