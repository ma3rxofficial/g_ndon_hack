# LICHESS TEAM CAPTURING BY USING TOKEN(ORIGINAL)

import berserk
import requests
import ndjson

def start_token():
    token = input('Token Here: ')
    team = input('Write team code(https://lichess.org/team/<code>/): ')

    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    r = requests.get('https://lichess.org/api/team' + team + '/users')
    data = r.json(cls=ndjson.Decoder)

    for i in data:
        user = i['id']
        client.teams.kick_member(team, user)
        print(f'{user} was kicked!')

if __name__ == '__main__':
    start_token()
