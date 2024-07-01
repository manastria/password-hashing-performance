import bcrypt
import hashlib
import time

# Configuration des paramètres
password = b"mon_mot_de_passe_tres_securise"
iterations = 100
bcrypt_cost = 12  # Ajuster ce coût pour observer les différences de performance
display_hash_count = 5  # Nombre de hash à afficher pour chaque algorithme

# bcrypt
print("Starting bcrypt hashing...")
bcrypt_hashes = []  # Liste pour stocker les premiers hash bcrypt
start_time = time.time()  # Démarrer le chronomètre
for i in range(iterations):
    if i % 20 == 0:  # Afficher la progression toutes les 100 itérations
        print(f"bcrypt iteration: {i}")
    salt = bcrypt.gensalt(rounds=bcrypt_cost)  # Générer un sel avec le coût spécifié
    hashed = bcrypt.hashpw(password, salt)  # Hacher le mot de passe avec bcrypt
    if i < display_hash_count:  # Stocker les premiers hash générés
        bcrypt_hashes.append(hashed)
end_time = time.time()  # Arrêter le chronomètre
print(f"bcrypt: Time taken for {iterations} hashes with cost {bcrypt_cost}: {end_time - start_time:.4f} seconds")
if display_hash_count > 0:
    print(f"First {display_hash_count} bcrypt hashes:")
    for h in bcrypt_hashes:  # Afficher les premiers hash bcrypt
        print(h)

# MD5
print("\nStarting MD5 hashing...")
md5_hashes = []  # Liste pour stocker les premiers hash MD5
start_time = time.time()  # Démarrer le chronomètre
for i in range(iterations):
    if i % 100 == 0:  # Afficher la progression toutes les 100 itérations
        print(f"MD5 iteration: {i}")
    hashed = hashlib.md5(password).hexdigest()  # Hacher le mot de passe avec MD5
    if i < display_hash_count:  # Stocker les premiers hash générés
        md5_hashes.append(hashed)
end_time = time.time()  # Arrêter le chronomètre
print(f"MD5: Time taken for {iterations} hashes: {end_time - start_time:.4f} seconds")
if display_hash_count > 0:
    print(f"First {display_hash_count} MD5 hashes:")
    for h in md5_hashes:  # Afficher les premiers hash MD5
        print(h)

# SHA-256
print("\nStarting SHA-256 hashing...")
sha256_hashes = []  # Liste pour stocker les premiers hash SHA-256
start_time = time.time()  # Démarrer le chronomètre
for i in range(iterations):
    if i % 100 == 0:  # Afficher la progression toutes les 100 itérations
        print(f"SHA-256 iteration: {i}")
    hashed = hashlib.sha256(password).hexdigest()  # Hacher le mot de passe avec SHA-256
    if i < display_hash_count:  # Stocker les premiers hash générés
        sha256_hashes.append(hashed)
end_time = time.time()  # Arrêter le chronomètre
print(f"SHA-256: Time taken for {iterations} hashes: {end_time - start_time:.4f} seconds")
if display_hash_count > 0:
    print(f"First {display_hash_count} SHA-256 hashes:")
    for h in sha256_hashes:  # Afficher les premiers hash SHA-256
        print(h)

# SHA-3-256
print("\nStarting SHA-3-256 hashing...")
sha3_256_hashes = []  # Liste pour stocker les premiers hash SHA-3-256
start_time = time.time()  # Démarrer le chronomètre
for i in range(iterations):
    if i % 100 == 0:  # Afficher la progression toutes les 100 itérations
        print(f"SHA-3-256 iteration: {i}")
    hashed = hashlib.sha3_256(password).hexdigest()  # Hacher le mot de passe avec SHA-3-256
    if i < display_hash_count:  # Stocker les premiers hash générés
        sha3_256_hashes.append(hashed)
end_time = time.time()  # Arrêter le chronomètre
print(f"SHA-3-256: Time taken for {iterations} hashes: {end_time - start_time:.4f} seconds")
if display_hash_count > 0:
    print(f"First {display_hash_count} SHA-3-256 hashes:")
    for h in sha3_256_hashes:  # Afficher les premiers hash SHA-3-256
        print(h)
