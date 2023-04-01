
#letter , key output encrypted letter
def encrypt_letter(letter, key):
    l_code = ord(letter)
    k_code = ord(key)
    enc_code = l_code + k_code
    return(chr(enc_code))


def decrypth_letter(letter, key):
    enc_l_code = ord(letter)
    k_code = ord(key)
    dec_code = enc_l_code - k_code
    return(chr(dec_code))


def process_message(message, key, encrypt):
    print("help")