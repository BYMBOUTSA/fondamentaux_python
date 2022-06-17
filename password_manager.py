from json import load
from cryptography.fernet import Fernet
from os.path import exists


def generate_key() -> bytes:
    '''
        Fonction pour générer et sauvegarder une clef

        Return:
            La clef
    '''
    key = Fernet.generate_key()

    # sauvegarder dans un fichier key.key
    with open('key.key', 'wb') as f:
        f.write(key)
    return key

def load_key() -> bytes:
    with open('key.key', 'rb') as f:
        key = f.read()
    return key

def store_credentials(id: str, password: str, fernet: Fernet) -> None:
    credentials = f'{id} | {password}'
    token = fernet.encrypt(credentials.encode())

    with open('password.txt', 'a') as f:
        f.write(token.decode('utf-8') + '\n')
    print(credentials, 'stocké.')

def views_credentials(fernet: Fernet) -> None:
    print('Identifiants / MDP stockées: ')
    if exists('password.txt'):
        with open('password.txt', 'rb') as f:
            for line in f.readlines():
                credentials = fernet.decrypt(line)

                id, mdp = credentials.decode('utf-8').split(' | ')
                print(f'''
                        Identifiant : {id}
                        MDP: {mdp}
                        ''')
    else:
        print('WARNING ! : aucun mot de passe sauvegardés jusqu\'à présent.')

if __name__ == '__main__':
    # Si on a pas générer de clef
    if not exists('key.key'):
        # Generer et sauvegarder une clef
        key = generate_key()
    else:
        #print('I load the key')
        # Charger la clef préalablement générée
        key = load_key()

    # Passer ma clef à l'algo Fernet.
    fernet = Fernet(key)

    
    while True:
        # Demander à l'utilisateur ce qu'il veut faire
        option = input(
            '''Que veut-tu faire ?
                - Stocker un coup de identifiant / mdp (s).
                - Voir les couples identifiant / mdp (v).
                - Quitter (q)
            '''
        )

        if option == 'q':
            break
        if option == 's':
            id = input('Entrer l\'identifiant a stocker: ')
            mdp = input('Entrer le mot de passe à stocker: ')
            store_credentials(id, mdp, fernet)
        elif option == 'v':
            views_credentials(fernet)