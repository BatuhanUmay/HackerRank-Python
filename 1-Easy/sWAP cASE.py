def swap_case(s):
    string = ""
    for harf in s:
        if (harf.isupper()):
            string = string + harf.lower()
        else:
            string = string + harf.upper()
    return string     
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)    
    
