import hashlib
import random
import string

#Generated hash by random string
def genHash():
    randomString = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    hash = hashlib.sha1(randomString.encode("utf-8")).hexdigest()[:20]
    return hash