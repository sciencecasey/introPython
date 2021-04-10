'''
Created on Mar 9, 2021

@author: CaseyJayne
'''


def decode(decrypt_frequencies, observed_count):
    for k, v in observed_count.items():
        for pair in decrypt_frequencies:
            if v in pair:
                #if type(observed_count[k]) == int:
                    # replace the value in dictionary with ciper letter
                observed_count[k] = pair[0]
                #else:
                    # add alternate
                    #observed_count[k] = [observed_count[k], pair[0]]
                #remove the item from the list
                decrypt_frequencies.remove(pair)
                break
    return observed_count


def get_freq_count(stringy):
    output = {}
    for letter in stringy:
        if output.get(letter):
            output[letter] += 1 
        else:
            output[letter] = 1 
    return output
    
    
def decrypt(message, code):
    outmsg = ""
    for letter in message:
        if code.get(letter):
            replacement = code[letter]
            outmsg += replacement
    return outmsg 

def main():
    file = open("ciphertext.txt", "r")
    out = open("decipheredText.txt", "w")
    # read in all at once
    message = file.read().strip() 
    # read in starting counts
    # close the files
    file.close()
    decrypt_count = []
    with open("freq.txt", "r") as in_count:
        # read in line by line
        line = in_count.readline()
        while line != "":
            # separate into a tuple
            x,y = line.split(":")
            # change the umeric to number
            y = int(y)
            decrypt_count.append((x, y))
            line = in_count.readline()
            
    msg_counts = get_freq_count(message)
    # Print output so it's easy for me to finish
    out.write("Good luck finishing!\nOriginal Message Counts: \n")
    out.write(f"{msg_counts}")
    out.write(f"\n\n")
    # Decode
    decoder = decode(decrypt_count, msg_counts)
    outmsg = decrypt(message, decoder)
    # Print output to console and file
    print("Input message: ")
    print(message)
    print()
    print("Decoded message: ")
    print(outmsg)
    out.write("Input message: \n")
    out.write(message)
    out.write(f"\n\n")
    out.write("Decoded message: \n")
    out.write(outmsg)
    #close the file
    out.close()
    
if __name__ == "__main__":
    main()
    
    

    