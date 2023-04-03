import useful_functions
import argparse

#output msg_file_encrypted.txt/msg_file_decrypted.txt

#if __name__ == "__main__":
praser = argparse.ArgumentParser(__file__)
praser.add_argument("--message", action = "store", dest ="mes", required=True,
                    help="")
praser.add_argument("--key", action="store", dest="key_string", required=True,
                    help="")
praser.add_argument("--mode", action="store", dest="mode", required=True,
                    #choices=["enc","dec"],
                    help="Specify \"enc\" or \"dec\" for encryption or decryption")
arg = praser.parse_args()

if arg.mode == "enc":
    enc=True
    file_name = "msg_file_encrypted.txt"
else:
    enc=False
    file_name = "msg_file_decrypted.txt"

out_content = useful_functions.process_message(arg.mes, arg.key_string, enc)

f = open(file_name, 'w')# write
f.write(out_content)
f.close()
print(out_content)
#write out output file
