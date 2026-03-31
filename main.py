import hashlib

def compute_MD5_hash(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()

captured_chars = []

with open("log.txt") as f_log, open("hashes.txt") as f_hashes:
    for line, h in zip(f_log, f_hashes):
        if line.startswith("SERVER") or line.startswith("-"):
            continue
        h = h.strip()
        if h and h[-1].isdigit():
           captured_chars.append(line[4])
        
print((captured_chars[:-1]))