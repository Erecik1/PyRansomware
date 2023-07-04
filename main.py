from cryptography.fernet import Fernet

# Generowanie klucza
key = Fernet.generate_key()

# Tworzenie obiektu Fernet na podstawie klucza
fernet = Fernet(key)

# Nazwa pliku do zaszyfrowania
file_name = 'file.txt'

# Odczytanie zawartości pliku
with open(file_name, 'rb') as file:
    file_data = file.read()

# Szyfrowanie danych
encrypted_data = fernet.encrypt(file_data)

# Zapisanie zaszyfrowanych danych do pliku
encrypted_file_name = 'zaszyfrowany_plik.txt'
with open(encrypted_file_name, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Wyświetlanie klucza
print("Wygenerowany klucz:", key.decode('utf-8'))



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Cripter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')