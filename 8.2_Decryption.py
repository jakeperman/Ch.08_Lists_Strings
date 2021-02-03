'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''
import random
import

# message = input("Input a message to decrypt")
# encrypted_message = ""
# for c in message:
#     x = ord(c)
#     x += random.randint(0,20)
#     c2 = chr(x)
#     encrypted_message += c2
#
# print(encrypted_message)

message = 'Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*'

for i in range(-20, 21):
    decrypted = ""
    for each in message:
        x = ord(each)
        x += i
        ch = chr(x)
        decrypted += ch
    print(decrypted)

# The secret message is: Congratulations! You cracked the code. The force is STRONG with you!

