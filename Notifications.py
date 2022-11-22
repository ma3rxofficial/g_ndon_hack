if __name__ == '__main__':
    import lichess
    from config import lts
    import os
    import json

    myclient = lichess.Client()

    if not os.path.exists('./autonotify.txxt'):

        users = input('Enter users(ex.: sergeyvoron baba_niga): ').split()

        data = {}
        data['autonotify'] = users

        with open('autonotify.txt', 'w') as outfile:
            json.dump(data, outfile)

    else:

        with open('autonotify.txt') as json_file:
            notify_data = json.load(json_file)

            users = notify_data['autonotify']

            data = myclient.get_status(users)

            offline = [i['name'] for i in data if 'online' not in i.keys()]
            online = [i['name'] for i in data if 'online' in i.keys()]
            playing = [i['name'] for i in data if 'playing' in i.keys()]

            print('Offline: ' + str(lts(offline)))
            print('Online: ' + str(lts(online)))
