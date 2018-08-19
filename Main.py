import requests

URL = 'https://api.telegram.org/' + 'bot651294662:AAGNUBYrNmmBvrq_P_VuK4lBayeC7Rezt3s' + '/'


def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()


def get_messege(current_id):
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    messege = data['result'][-1]['message']['text']
    mess_id = data['result'][-1]['update_id']
    user = data['result'][-1]['message']['from']['username']
    mess = {'chat_id': chat_id,
            'message': messege,
            'upd': mess_id,
            'user': user}
    if current_id != mess['upd']:
        print(mess)
    return mess


def send_messege(id, messege):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(id, messege)
    requests.get(url)


def main():
    current_id = -1
    while True:
        data = get_messege(current_id)
        if current_id == data['upd']:
            continue
        text = check_mess(data['message'])
        send_messege(data['chat_id'], text)
        current_id = data['upd']


def check_mess(message):
                # DIALOG
    if 'hello' in message:
        return 'hello world'
    elif '/start' in message:
        return 'Привет! Я бот версии 1.0.0 \n' \
               'Я пока мало что умею, так что не бейте ногами \n' \
               'Все что я пока умею - это отвечать на 2 сообщения\n' \
               'И это в их числе\n' \
               'Пиши в нижнем регистре, что бы  я не парился'
    elif 'контест' in message:
        return 'https://official.contest.yandex.ru/contest/8630'
    elif 'привет' in message:
        return 'Мы уже здоровались))'
    elif ('умеешь' in message) and ('ты' in message):
        return 'Ничегоооо)))'
    elif ('твой создатель' in message) and ('кто тебя' in message):
        return '@fargoth_Co'
    else:
        return 'im not understand'


if __name__ == '__main__':
    main()

