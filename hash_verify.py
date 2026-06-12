import hashlib

file = input("File: ")

with open(file, "rb") as f:
    data = f.read()
    
hash = hashlib.sha256(data).hexdigest()

print("SHA256: ")
print(hash)
