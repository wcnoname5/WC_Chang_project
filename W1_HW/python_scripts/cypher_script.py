import useful_functions
import argparse

def main(message_text, key, mode):
    if mode == "enc":
        enc=True #encryption
        suffix = "encrypted"
    else:
        enc=False 
        suffix = "decrypted"

    temp = message_text.split('.')[0] #w/o file format
    file_name = temp + "_" + suffix + ".txt"
    message = open(message_text, 'r') #open the message file
    word_list = list(message)

    f = open(file_name, 'w')# write
    for i in word_list:
        out_content = useful_functions.process_message(i, key, enc)
        f.write(out_content)
        f.write('\n')
        #print(out_content)
    f.close()
    print("Message is successfully " + suffix +"!")

def argparse_func():
    praser = argparse.ArgumentParser(__file__)
    praser.add_argument("-m", "--message", action = "store", dest ="mes", required=True,
                        help="Add a text file or a path of it")
    praser.add_argument("-k", "--key", action="store", dest="key", required=True,
                        help="Type your encryption/decryption key")
    praser.add_argument("--mode", action="store", dest="mode", required=True,
                        choices=["enc","dec"],
                        help="Specify \"enc\" or \"dec\" for encryption or decryption")
    args = praser.parse_args()
    return(args)
arg = argparse_func()

if __name__ == "__main__":
    main(arg.mes, arg.key, arg.mode)
