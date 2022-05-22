# PokeWay: um game Pokémon 

## Descrição do Projeto

<p align="justify">

PokeWay é um jogo de caça aos Pokémons. O objetivo deste projeto é praticar o desenvolvimento e consumo de APIs REST. Frontend realizado em React e Backend realizado em Django utiliazando o banco de dados PostgreSQL (em um container Docker).

## Features realizadas

1. Log In e Sign Up

2. Consumo de <a href = "https://pokeapi.co/">API</a> para obter dados dos Pokemóns (inclusive imagens)

3. Desenvolvimento de API para criação e login de usuário, adição de Pokémon, level up.
  
4. Escolha de mapas para caçar Pokemóns

5. Reaproveitamento de telas, como no caso de consultar os Pokémons e escolher algum para batalha
  
6. Batalha de Pokémons com música, efeito sonoro e animações.
  
7. Uso de música em todas as telas do game.
  
8. Projeto disponibilizado pelo Heroku.



## Instruções de uso 

> ### Rodando Localmente - Windows

1. Realizar o clone do repositório.

2. Instalando dependências:


```bash

pip install -r requirements.txt

```

3. Para rodagem do arquivo local, verificar se a variável DEBUG em `pokegame/settings.py` está com valor True.

4. Criar um container Docker com imagem Postgres. <p> <a href = "https://docs.docker.com/get-docker/"> Baixe o Docker</a> </p>

5. Ative o container no PowerShell ou em um terminal com permissão de administrador. 


```bash

docker run --rm --name pg-docker -e POSTGRES_PASSWORD=[escolhaumasenha] -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

```

6. Por fim, na pasta do projeto clonado rode no terminal o comando abaixo e acesse em um navegador: `http://localhost:8000`

```bash

python manage.py runserver

```

> ### Acessando projeto via web (Aplicação Heroku)

1. Apenas clique <a href = "https://pokeway.herokuapp.com/">aqui</a>.

<p align="center"><img src='https://thumbs.gfycat.com/LivelyBraveAmericanriverotter-size_restricted.gif'></img></p>

@2022, Insper. Quarto Semestre, Engenharia da Computação.
