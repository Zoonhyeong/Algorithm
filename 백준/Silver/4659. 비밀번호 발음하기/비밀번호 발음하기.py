
def check_mo(input_str):
    str_ja = 'bcdfghjklmnpqrstvwxyz'
    str_mo = 'aeiou'
    count_mo = 0

    for i in range(len(input_str)):
        if(input_str[i] in str_mo):
            count_mo += 1
    
    if(count_mo == 0):
        return False
    
    if(len(input_str) > 2):
        for i in range(len(input_str) - 2):
            temp_str = input_str[i] + input_str[i+1] + input_str[i+2]
            count = 0
            if(input_str[i] in str_mo):
                for char in temp_str:
                    if(char in str_mo):
                        count += 1
            else:
                for char in temp_str:
                    if(char in str_ja):
                        count += 1
            

            if(count == 3):
                return False

    
    if(len(input_str) > 1):
        for i in range(len(input_str) - 1):
            temp_str2 = input_str[i] + input_str[i+1]
            isSame = input_str[i] == input_str[i+1]

            if(isSame and temp_str2 != 'ee' and temp_str2 != 'oo'):
                return False
    
    return True

while True:
    my_str = input()
    boolxo = True

    if(my_str == 'end'):    
        break

    boolxo = check_mo(my_str)


    if(boolxo):
        print("<" + my_str + "> is acceptable.")
    else:
        print("<" + my_str + "> is not acceptable.")