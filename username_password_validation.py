#validating username and password:
  #username parameters:
  #length 8-15 char done
  #only alpha and numeric done
  #no spaces no special char done
  #At least one upper
  #A least one lower
  #A least one numeric

#password parameters:
    #at least 8 chars
    #cannot contain username
    ##mix of upper lower and (#,$,% and &) (at least one each)

def valid_username(username):
    x = "Username is invalid,please try again."
    y = "Username is valid!"
    upper = 0
    lower = 0
    numeric = 0
    f_l = True
    alpha_num = True
    print("* Length of username : ", len(username))
    i=0
    while i < len(username):

        if username[i].isnumeric():
            numeric +=1
        if username[i].isalpha():
            if username[i] == username[i].upper():
                upper +=1
            if username[i] == username[i].lower():
                lower +=1
        i +=1

    alpha_num = username.isalnum()
    print("* All characters are alpha-numeric:", alpha_num)

    if username[0].isnumeric() or username[-1].isnumeric():
        print("* First & last characters are not digits:", f_l)
        f_l = False
    else:
        print("* First & last characters are not digits:", f_l)

    print("* # of uppercase characters in the username: ", upper)
    print("* # of lowercase characters in the username: ", lower)
    print("* # of digits in the username: ", numeric)

    if upper < 1 or lower < 1 or numeric < 1:
        return x
    if len(username) < 8 or len(username) > 15:
        return x
    if alpha_num == False:
        return x
    if f_l == False:
        return x

    return y

while True:
    username = input("Enter a username: ")
    validity = valid_username(username)
    print(validity)
    print()
    if validity == "Username is valid!":
        break

sub = username

def valid_password(password):
    x = "Password is invalid, please try again."
    y = "Password is valid!"
    upper = 0
    lower = 0
    numeric = 0
    special = 0
    i=0
    while i < len(password):

        if password[i].isnumeric():
            numeric +=1
        if password[i] in ("%,$,&"):
            special +=1
        if ord(password[i]) == 35:
            special +=1
        if password[i].isalpha():
            if password[i] == password[i].upper():
                upper +=1
            if password[i] == password[i].lower():
                lower +=1
        i +=1

    user_in_pass = False
    if (username in password):
        user_in_pass = True


    print("* Length of username : ", len(password))
    print("* Username is part of password:", user_in_pass)
    print("* # of uppercase characters in the password: ", upper)
    print("* # of lowercase characters in the password: ", lower)
    print("* # of digits in the password: ", numeric)
    print("* # of special charactes in the password: ", special)

    if upper < 1 or lower < 1 or numeric < 1 or special < 1:
        return x
    if len(password) < 8:
        return x


    return y


while True:
    password = input("Enter a password: ")
    validity = valid_password(password)
    print(validity)
    print()
    if validity == "Password is valid!":
        break
