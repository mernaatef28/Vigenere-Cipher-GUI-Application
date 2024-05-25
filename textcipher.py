# Encrypt Text
def vigenere_encrypt(plain_text, key="CIPHER"):
    size = len(plain_text)
    encrypted_message = [''] * size

    for i in range(size):
        j = i % len(key)
        p = plain_text[i]
        k = key[j]

        p_index = ord(p) - ord('A')
        k_index = ord(k) - ord('A')

        enc_index = (p_index + k_index) % 26

        encrypted_message[i] = chr(enc_index + ord('A'))

    return ''.join(encrypted_message)

# Decrypt text

def vigenere_decrypt(plain_text, key="CIPHER"):
    size = len(plain_text)
    decrypted_message = [''] * size

    for i in range(size):
        j = i % len(key)
        p = plain_text[i]
        k = key[j]

        p_index = ord(p) - ord('A')
        k_index = ord(k) - ord('A')

        dec_index = (p_index - k_index) % 26

        decrypted_message[i] = chr(dec_index + ord('A'))

    return ''.join(decrypted_message)