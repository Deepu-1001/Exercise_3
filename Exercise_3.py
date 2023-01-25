# it was not specified in the question whether to take count of the spces
# that is " " int the resulting dict but as the sampple test case 
# didnt took count of it i applied one more condition to eradicate that case



input_string=input("Enter a string: ")

string_dict={}
def get_string_dict(strng):
    temp_dict={}
    temp_string= strng.lower()
    for i in temp_string:
        if i !=" ": 
            if i in temp_dict:
                temp_dict.update({i:str(int(temp_dict[i])+1)})
            if i not in temp_dict:
                        temp_dict.update({i:1})

    return temp_dict

string_dict = get_string_dict(input_string)

print(string_dict)