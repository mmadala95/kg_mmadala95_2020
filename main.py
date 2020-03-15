import sys


def isValidMapping(str1,str2):

    if(len(str1)!=len(str2)):
        return False
    # dictionary to map string one
    mapping=dict()
    for str1_char,str2_char in zip(str1,str2):
        #validate if entry is there in mapping
        if str1_char in mapping:
            #validate if existing mapping value and new value for the string are same
            if mapping[str1_char]==str2_char:
                continue
            else:
                return False
        #if not include string one character in mapping
        else:
            mapping[str1_char]=str2_char

    #incase of checking one on one mapping from both sides use this in else part
            # if str2_char not in mapping.values():
            #   mapping[str1_char] = str2_char
            # else:
            #     return False
    return True

if __name__=="__main__":
    if(len(sys.argv)<3):
        print ("Not enough arguments provided")
        sys.exit(1)
    stringOne=sys.argv[1]
    stringTwo=sys.argv[2]
    result=isValidMapping(stringOne,stringTwo)

    print(result)