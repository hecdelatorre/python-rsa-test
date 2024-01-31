import os
import sqlite3
import shutil
from pathlib import Path
from rsa import newkeys
from rsa.key import PublicKey, PrivateKey

def create_keychain():
    home_dir = str(Path.home())
    keychain_dir = os.path.join(home_dir, ".keychain")

    if os.path.exists(keychain_dir):
        choice = input(".keychain folder already exists. Do you want to generate new keys? (y/n): ")
        if choice.lower() == 'y':
            shutil.rmtree(keychain_dir)
        else:
            return False

    os.makedirs(keychain_dir)

    db_path = os.path.join(keychain_dir, "keys.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE keys (
                        id INTEGER PRIMARY KEY,
                        keypart TEXT
                      )''')

    conn.commit()
    conn.close()

    print("Keys database created successfully.")
    return True

def generate_keys():
    if create_keychain():
        print("Generating keys...")
        publicKey, privateKey = newkeys(1024)

        db_path = os.path.join(str(Path.home()), ".keychain", "keys.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # PublicKey n - 1, e - 2
        # PrivateKey n - 1, e - 2, d - 3, p - 4, q - 5 
        cursor.execute("INSERT INTO keys (id, keypart) VALUES (?, ?)", (1, str(publicKey.n)))
        cursor.execute("INSERT INTO keys (id, keypart) VALUES (?, ?)", (2, str(publicKey.e)))
        cursor.execute("INSERT INTO keys (id, keypart) VALUES (?, ?)", (3, str(privateKey.d)))
        cursor.execute("INSERT INTO keys (id, keypart) VALUES (?, ?)", (4, str(privateKey.p)))
        cursor.execute("INSERT INTO keys (id, keypart) VALUES (?, ?)", (5, str(privateKey.q)))

        conn.commit()
        conn.close()

        print("Keys generated and stored successfully.")
    else:
        print("No keys were generated.")

if __name__ == "__main__":
    generate_keys()
