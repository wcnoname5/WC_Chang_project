import useful_functions
import argparse

#output msg_file_encrypted.txt/msg_file_decrypted.txt

if __name__ == "__main__":
    praser = argparse.ArgumentParser(__file__)
    praser.add_argument("-m", "--message", action = "store", dest ="mes", required=True,
                        help="Add a text file or a path of it")
    praser.add_argument("-k", "--key", action="store", dest="key_string", required=True,
                        help="")
    praser.add_argument("--mode", action="store", dest="mode", required=True,
                        #choices=["enc","dec"],
                        help="Specify \"enc\" or \"dec\" for encryption or decryption")
    arg = praser.parse_args()
    
    
    if arg.mode == "enc":
        enc=True #encryption
        suffix = "_encrypted.txt"
    else:
        enc=False 
        suffix = "_decrypted.txt"
    temp = arg.mes.split('.')[0] #w/o file format
    file_name = temp + suffix
    message = open(arg.mes, 'r') #open the message file
    
    word_list = list(message)
    
    f = open(file_name, 'w')# write
    for i in word_list:
        out_content = useful_functions.process_message(i, arg.key_string, enc)
        f.write(out_content)
        f.write('\n')
        #print(out_content)
    f.close()

#write out output file
