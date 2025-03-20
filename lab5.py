import random
import string

def main():
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
    
    passwords = [''.join(random.choice(string.ascii_lowercase) for _ in range(15)) for _ in range(5)]
    print("\nGenerated Passwords:")
    for pwd in passwords:
        print(pwd)
    
    new_passwords = []
    for pwd in passwords:
        new_pwd = ""
        for c in pwd:
            new_pwd += random.choice(repl_dict[c]) if c in repl_dict else c
        new_passwords.append(new_pwd)
    
    strong = []
    weak = []
    for pwd in new_passwords:
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

if __name__ == "__main__":
    main()
