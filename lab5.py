import random
import string

letters_used = set()
repl_used = set()
repl_dict = {}

for i in range(5):
    while True:
        letter = input("Enter a lowercase letter: ").strip()
        if len(letter) == 1 and letter.islower() and letter not in letters_used:
            letters_used.add(letter)
            break
        else:
            print("Invalid or duplicate letter.")
    repls = set()
    while len(repls) < 3:
        rep = input(f"Enter a replacement character for '{letter}': ").strip()
        if len(rep) == 1 and rep not in repl_used:
            repls.add(rep)
            repl_used.add(rep)
        else:
            print("Invalid or duplicate character.")
    repl_dict[letter] = list(repls)

print("\nReplacement Dictionary:")
for key, value in repl_dict.items():
    print(f"{key} -> {value}")

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

print("\nOriginal Passwords:")
for pwd in passwords:
    print(pwd)

final_passwords = []
for pwd in passwords:
    new_pwd = ""
    for c in pwd:
        new_pwd += random.choice(repl_dict[c]) if c in repl_dict else c
    final_passwords.append(new_pwd)

strong = []
weak = []
for pwd in final_passwords:
    special = sum(1 for c in pwd if c not in string.ascii_lowercase)
    if special > 4:
        strong.append(pwd)
    else:
        weak.append(pwd)

print("\nStrong Passwords:")
for pwd in strong:
    print(pwd)
print("\nWeak Passwords:")
for pwd in weak:
    print(pwd)
