from Crypto.PublicKey import RSA

keys = RSA.generate(2048)

private_key = keys.export_key()
public_key = keys.public_key().export_key()

with open('private.pem', 'wb') as f:
    f.write(private_key)

with open('public.pem', 'wb') as f:
    f.write(public_key)
