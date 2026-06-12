import hashlib

file = input("File: ")

with open(file, "rb") as f:
    dados = f.read()
    
hash = hashlib.sha256(dados).hexdigest()

print("SHA256: ")
print(hash)