# python-rsa-test

This Python project demonstrates RSA key generation, encryption, and decryption. It includes a simple menu-driven command-line interface for generating keys, encrypting messages, and decrypting messages.

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://codeberg.org/hecdelatorre/Python-RSA-Test.git
   ```

2. Create a virtual environment:
   
   ```bash
   python3 -m venv env
   ```

3. Activate the virtual environment:
   
   ```bash
   . env/bin/activate
   ```

4. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script using the following command:

```bash
python main.py
```

### Menu Options

1. **Generate Keys:** Generates RSA public and private keys. You will be prompted to choose the key size.

2. **Encrypt Message:** Encrypts a user-entered message using the generated public key.

3. **Decrypt Message:** Decrypts the previously encrypted message using the generated private key.

e. **Exit:** Exits the program.

## GPL 3 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
