import hashlib

def compute_MD5_hash(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()

with open("log.txt") as f, open("hashes.txt", "w") as out:
    for line in f:
        out.write(compute_MD5_hash(line) + "\n")