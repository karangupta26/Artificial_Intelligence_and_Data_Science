# Practical 8 Rivest Shamir Adleman RSA Algorithm
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
# Subject   -   Information Security
#########################################################

from random import randrange, getrandbits

class RSA:

    def __init__(self, prime_length=1024):
        self.prime_length = prime_length
        self.p = self.generate_prime_number()
        self.q = self.generate_prime_number()
        self.e = 65537
        self.generate_keys()

    def is_prime(self, n, k=128):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if (x != 1 and x != n - 1):
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def generate_prime_candidate(self, length):

        p = getrandbits(length)
        p |= (1 << length - 1) | 1
        return p

    def generate_prime_number(self):
        p = 4
        length = self.prime_length
        while not self.is_prime(p, 128):
            p = self.generate_prime_candidate(length)
        self.generate_prime_candidate(1) # Clears variables
        return p

    def check_encryption(self):
        test_message = "abcdefghijklmnopqrstuvqxyz"
        encrypted = self.encrypt(test_message)
        decrypted = self.decrypt(encrypted)
        if test_message == decrypted:
            return True
        return False

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def string_to_ascii(self, message):
        return [ord(c) for c in message]

    def ascii_to_string(self, c):
        return chr(c)

    def mod_power(self, power, base, mod):
        return pow(base, power, mod)

    def phi_primes(self):
        return ((self.p-1) * (self.q-1))

    def hcf(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.hcf(b % a, a)
            return (g, x - (b // a) * y, y)

    def modular_inverse(self):
        g, x, y = self.hcf(self.e, self.phi_pq)
        return x % self.phi_pq

    def generate_keys(self):
        self.pq = self.p*self.q
        self.phi_pq = self.phi_primes()
        self.public_key = [self.pq, self.e]
        self.private_key = self.modular_inverse()
        return [self.public_key, self.private_key]

    def encrypt(self, message):
        return [self.mod_power(self.public_key[1], c, self.public_key[0]) for c in self.string_to_ascii(message)]

    def decrypt(self, ciphertext):
        return ''.join([self.ascii_to_string(self.mod_power(self.private_key, c, self.public_key[0])) for c in ciphertext])

if __name__ == '__main__':
    rsa = RSA()
    message = input("Enter Text For a Encryption : ")
    encrypted = rsa.encrypt(message)
    print("\n\t Encrypted Text: \n")
    print(encrypted,"\n")
    decrypted = rsa.decrypt(encrypted)
    print("Decrypted Message : ",decrypted)
