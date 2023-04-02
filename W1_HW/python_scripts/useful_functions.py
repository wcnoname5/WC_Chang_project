
#letter , key output encrypted letter
def encrypt_letter(letter, key):
    l_code = ord(letter)
    k_code = ord(key)
    enc_code = l_code + k_code
    return(chr(enc_code))


def decrypt_letter(letter, key):
    enc_l_code = ord(letter)
    k_code = ord(key)
    dec_code = enc_l_code - k_code
    return(chr(dec_code))


def process_message(message, key, encrypt = True):
    #enc_list = [list(message), list(key)]
    list_k = list(key)
    output = str()
    for index, mes_let  in enumerate(message):
        i = index % len(list_k) 
        if encrypt:
            k = encrypt_letter(mes_let, list_k[i])
        else:
            k = decrypt_letter(mes_let, list_k[i])
        output = output + k
    return(output)
