# ord() #convert a char to ascii value
# chr() #convert a value to ascii char

def encrypt(sentence):

    result = []
    for letter in sentence:
        l = ord(letter) 
        result.append(l)
    
    # print(result)

    print("This is your encrypted message")
    for numbers in result:
        print(numbers,end='')
        print(" ", end='')

    print()
    decrypt(result)


def decrypt(result):
    end_string = ""
    for numbers in result:
        l = int(numbers)
        # l = l + 200
        l = chr(l)
        end_string = end_string + l
    
    print("Your decrypted message is: ")
    print(end_string)
    

def main():
    s = input("Input a sentence that you want encrypted ")
    encrypt(s)
  


if __name__ == '__main__':
    main()