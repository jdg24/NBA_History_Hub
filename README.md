# NBA_History_Hub

Scraped NBA Game Data + An API

```bash
spin up sportSnapshot crawler, processor and postgres DB containers

docker build -t nbahistoryhub .
docker kill $(docker ps -q --filter ancestor=nbahistoryhub);  docker run --rm -p 5000:5000 nbahistoryhub
```

Endpoints:
`http://localhost:5000/`
`http://localhost:5000/leagues/NBA/teams`
`http://localhost:5000/leagues/NHL/teams/BOS/games?date=2010-03-07`

When making changes, rebuild and re-run the above.
