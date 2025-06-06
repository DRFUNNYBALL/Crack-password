# you need to find hash of password
#just search MD5 Hash Generator in google and enter the site and enter your password and generate your password
#copy your hash password and past it in the (target)

import hashlib
import itertools
import string
from typing import Optional

def load_wordlist(filename: str) -> list:
    """
    Load passwords from a wordlist file.
    Returns a list of passwords.
    """
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Wordlist file '{filename}' not found!")
        return []

def dictionary_attack(hash_to_crack: str, wordlist: list) -> Optional[str]:
    """
    Attempt to crack a password using a dictionary attack.
    Returns the password if found, None otherwise.
    """
    for word in wordlist:
        # Try the word as is
        if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
            return word
        
        # Try with common substitutions
        variations = [
            word.capitalize(),
            word.upper(),
            word + "123",
            word + "!",
            "123" + word,
        ]
        
        for variation in variations:
            if hashlib.md5(variation.encode()).hexdigest() == hash_to_crack:
                return variation
    
    return None

def brute_force_attack(hash_to_crack: str, max_length: int = 4) -> Optional[str]:
    """
    Attempt to crack a password using brute force.
    Returns the password if found, None otherwise.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            if hashlib.md5(password.encode()).hexdigest() == hash_to_crack:
                return password
    
    return None

def main():
    # Example usage
    target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # MD5 hash of "password"
    
    # Load wordlist from file
    wordlist = load_wordlist("wordlist.txt")
    if not wordlist:
        return
    
    # Dictionary attack example
    result = dictionary_attack(target_hash, wordlist)
    
    if result:
        print(f"Password found using dictionary attack: {result}")
    else:
        print("Password not found in wordlist")
        
        # Try brute force if dictionary attack fails
        print("Attempting brute force attack...")
        result = brute_force_attack(target_hash, max_length=4)
        if result:
            print(f"Password found using brute force: {result}")
        else:
            print("Password not found using brute force")

if __name__ == "__main__":
    main() 