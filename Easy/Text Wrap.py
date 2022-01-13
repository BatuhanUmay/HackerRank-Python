import textwrap

def wrap(string, max_width):
    # s = ""
    # sayac = 0
    # for i in range(len(string)):
    #     if (sayac == max_width):
    #         s = s + "\n" 
    #         sayac = 0
            
    #     s = s + "" + string[i]

    #     sayac += 1
        
    # return s 

    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
        


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
