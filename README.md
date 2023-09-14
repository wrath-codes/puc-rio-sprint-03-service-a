# Backend para o Sprint 3
## Descrição
Este projeto é um Backend para Sprint 03, faz parte do ultimo sprint da Pós Graduação em Desenvolvimento Full Stack da PUC-Rio.


## Pré-requisitos
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)



## Instalação
1. Clone o repositório

2. Faca a build do container
```bash
docker build -t sprint-3-backend .
```

3. Acesse o site
```bash
npm run dev
```
4. Acesse o endereço [http://localhost:4200](http://localhost:4200)


## Autores
- [Raphael Vaz](http://github.com/wrath-codes)

5. Comandos uteis:
   - Para rodar o container:
      ```bash
      docker run -it -p 5173:5173 sprint-3-frontend
      ```
   - Para parar o container:
      ```bash
      docker stop $(docker ps -a -q)
      ```
   - Para remover o container:
      ```bash
      docker rm $(docker ps -a -q)
      ```