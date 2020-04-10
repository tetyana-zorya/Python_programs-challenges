#decoder and encoder
#encoder:
    #takes integer and d_phrase
    #adds 'integer' amount of randomly genereated capital
    #or lowercase letters after each character of input phrase

    #then shifts each character by 'intger' number of ascii values:
    # if integer = 1, then a --> b

#decoder:
    #decodes the encoded message by reversing the applied changes



def add_letters(word,num):
    import random
    new_word = []
    letters = ""
    for chars in word:
        letters = ""
        for i in range(num):
            cap_no = random.randint(0,1)
            if cap_no == 0:
                caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                cap_idx = random.randint(0,25)
                add_cap = caps[cap_idx]
                letters += add_cap
            if cap_no == 1:
                down = "abcdefghijklmnopqrstuvwxyz"
                down_idx = random.randint(0,25)
                add_down = down[down_idx]
                letters +=add_down

        new_word.append(chars + letters)
    s = ""
    scrambled = s.join(new_word)
    return scrambled

def remove_letters(scrambled,num):
    step = num+1
    return scrambled[::step]

def shift_characters(word,num):
    i = 0
    shifted_word = ""
    while i < len(word):
       new_let = ord(word[i]) + num
       shifted_word += chr(new_let)
       i +=1
    return shifted_word

#running program:
while True:

    while True:
        e_d_q = input("(e)ncode, (d)ecode, (q)uit: ")
        if e_d_q == "e" or e_d_q == "d" or e_d_q == "q":
            break
        else:
            print("Invalid entry, choose either 'e', 'd' or 'q' ")
    if e_d_q == "q":

        break

    while True:
        num = int(input("Enter a number between 1 and 5: "))
        if num >= 1 and num <= 5:
            break
        else:
            print("Invalid number, try again.")
    if e_d_q == "e":
        e_phrase = input("Enter a phrase to encode: ")

        added = add_letters(e_phrase, num)
        encoded = shift_characters(added, num)
        print("Your encoded word is: ",encoded)
        print()

    if e_d_q == "d":
        d_phrase = input("Enter a phrase to decode: ")
        step = num * -1
        un_shift = shift_characters(d_phrase, step)
        decoded = remove_letters(un_shift,num)
        print("Your decoded word is: ", decoded)
        print()
