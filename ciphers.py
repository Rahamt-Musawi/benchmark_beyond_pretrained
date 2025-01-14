import unicodedata
import pandas as pd
from itertools import cycle
from abc import ABC, abstractmethod

class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text: str, key: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, encrypted_text: str, key: str) -> str:
        pass

class CaesarCipher(Cipher):
    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def _shift_char(self, char: str, shift: int) -> str:
        if char not in self.alphabet:
            return char
        index = self.alphabet.index(char)
        shifted_index = (index + shift) % len(self.alphabet)
        return self.alphabet[shifted_index]

    def encrypt(self, text: str, key: str) -> str:
        shift = int(key) % len(self.alphabet)
        return ''.join(self._shift_char(char, shift) for char in text)

    def decrypt(self, encrypted_text: str, key: str) -> str:
        shift = (-int(key)) % len(self.alphabet)
        return ''.join(self._shift_char(char, shift) for char in encrypted_text)

class VigenereCipher(Cipher):
    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def _shift_char(self, char: str, key_char: str) -> str:
        if char not in self.alphabet:
            return char
        char_index = self.alphabet.index(char)
        key_index = self.alphabet.index(key_char)
        shifted_index = (char_index + key_index) % len(self.alphabet)
        return self.alphabet[shifted_index]

    def encrypt(self, text: str, key: str) -> str:
        key = ''.join(c for c in key if c in self.alphabet)
        if not key:
            raise ValueError("Key must contain at least one character from the alphabet")
        key_cycle = cycle(key)
        return ''.join(self._shift_char(char, next(key_cycle)) if char in self.alphabet else char for char in text)

    def decrypt(self, encrypted_text: str, key: str) -> str:
        key = ''.join(c for c in key if c in self.alphabet)
        if not key:
            raise ValueError("Key must contain at least one character from the alphabet")
        key_cycle = cycle(self.alphabet[-self.alphabet.index(k)] for k in key)
        return ''.join(self._shift_char(char, next(key_cycle)) if char in self.alphabet else char for char in encrypted_text)

def create_cipher(method: str, alphabet: str) -> Cipher:
    if method == "caesar_cipher":
        return CaesarCipher(alphabet)
    elif method == "vigenere_cipher":
        return VigenereCipher(alphabet)
    else:
        raise ValueError("Unsupported cipher method")

def encrypt_decrypt(method: str, task: str, input_text: str, key: str, alphabet: str) -> str:
    cipher = create_cipher(method, alphabet)

    if task == "encrypt":
        return cipher.encrypt(input_text, key)
    elif task == "decrypt":
        return cipher.decrypt(input_text, key)
    else:
        raise ValueError("Unsupported task")

def normalize_greek(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')