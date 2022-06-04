import hashlib

str = input()
encoded_str = str.encode()
answer = hashlib.sha256(encoded_str).hexdigest()
print(answer)
