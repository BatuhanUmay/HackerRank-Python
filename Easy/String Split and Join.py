def split_and_join(line):
    liste = line.split(" ")
    
    liste = "-".join(liste)

    return liste


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)