import psycopg2 as db
from flask import Flask, jsonify, request

app = Flask(__name__)


def execute_query(query):

    connection = db.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal",
        port="5432",
    )

    cursor = connection.cursor()
    cursor.execute(query)

    column_names = [desc[0] for desc in cursor.description]

    query_result = [dict(zip(column_names, record)) for record in cursor]

    connection.close()
    cursor.close()

    return query_result


@app.route("/")
def index():
    return jsonify({"app": "NBA History Hub"})


@app.route("/leagues/<league>/teams")
def teams(league):

    query = f"""
        SELECT
            team.team_abbr,
            team.team_location,
            team.team_name
        FROM tblTeam team
        INNER JOIN tblLeague league
            ON team.league_id = league.id
        WHERE league.league_abbr = '{league}'
    """

    query_result = execute_query(query)

    return jsonify(query_result)


@app.route("/leagues/<league>/teams/<team>/games")
def games_by_league_and_team(league,team):
    date = request.args.get("date")

    if date is None:
        return "Please pass a date query parameter in the format YYYY-MM-DD."
    query = f"""
        SELECT
            league.league_abbr,
            game.game_season,
            game.game_date,
            team.team_abbr,
            opponent.team_abbr AS opponent_abbr,
            game.team_points,
            game.opponent_points
    FROM tblGameRaw game
    INNER JOIN tblTeam team
        ON game.team_id = team.id
    INNER JOIN tblTeam opponent
        ON game.opponent_id = opponent.id
    INNER JOIN tblLeague league
        ON team.league_id = league.id
    WHERE league.league_abbr = '{league}'
    AND team.team_abbr = '{team}'
    AND game.game_date = '{date}'  
    """
    query_result = execute_query(query)
    return jsonify(query_result)

@app.route("/leagues/<league>/games")
def games_by_league(league):
    date = request.args.get("date")

    if date is None:
        return "Please pass a date query parameter in the format YYYY-MM-DD."
    query =f"""
    SELECT
        league.league_abbr,
        game.game_season,
        game.game_date,
        team.team_abbr,
        opponent.team_abbr AS opponent_abbr,
        game.team_points,
        game.opponent_points
    FROM tblGameRaw game
    INNER JOIN tblTeam team
        ON game.team_id = team.id
    INNER JOIN tblTeam opponent
        ON game.opponent_id = opponent.id
    INNER JOIN tblLeague league
        ON team.league_id = league.id
    WHERE league.league_abbr = '{league}'
    AND game.game_date = '{date}'
    """
    query_result = execute_query(query)
    return jsonify(query_result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

