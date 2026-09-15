import hashlib
def hash_file(filename):
    sha = hashlib.sha256()

    with open(filename, "rb") as f:
        for data in iter(lambda: f.read(4096), b""):
            sha.update(data)

    return sha.hexdigest()

def verify_file(filename, old_hash):
    return hash_file(filename) == old_hash

def hash_string(data):
    return hashlib.sha256(data.encode()).hexdigest()

def compare_hash(old_hash, new_hash):
    if old_hash == new_hash:
        return "No change"
    return "File changed"

filename = input("Enter file name: ")
original_text = input("Enter original text: ")
modified_text = input("Enter modified text: ")
text = input("Enter a string to hash: ")

with open(filename, "w") as f:
    f.write(original_text)

old_hash = hash_file(filename)

print("\nOriginal Hash:", old_hash)
print("Before Change:", verify_file(filename, old_hash))

with open(filename, "w") as f:
    f.write(modified_text)

new_hash = hash_file(filename)

print("Modified Hash:", new_hash)
print("After Change:", verify_file(filename, old_hash))
print("Result:", compare_hash(old_hash, new_hash))

print("String Hash:", hash_string(text))
