import requests, random, threading, time, string

with open('proxies.txt', 'r') as proxies:
    proxies = proxies.read().splitlines()


def create_account():
    try:
        with requests.session() as session:
            username = ""
            for i in range(13):
                username = username + random.choice(string.ascii_uppercase)
            password = random.randint(10000000,100000000)
            create = session.post('https://www.nitrotype.com/api/register', data={'username':username, 'password':password, 'email':'', 'acceptPolicy':'on', 'receiveContact':'', 'adb':0, 'tz':'America/Los_Angeles'}, proxies={'http':random.choice(proxies), 'https':random.choice(proxies)})
            if create.status_code == 200 and create.json():
                with open('nitro_type_accs.txt', 'a') as tokens:
                    tokens.write(f'{username}:{password} \n')
            print(f'=-> Bot account created with username: [{username}]')
    except:
        pass

while True:
    threading.Thread(target=create_account,).start()
