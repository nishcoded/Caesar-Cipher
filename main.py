alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, user_direction):
    new_word = ""
    if user_direction == "decode":
        shift_amount *= -1

    for char in plain_text:
        if char in alphabets:
            index = alphabets.index(char)
            new_index = index + shift_amount
            new_word += alphabets[new_index]

    print(f"The {user_direction}d text is {new_word}")

should_continue= True

while should_continue:
    text = input("What is the text? ").lower()
    shift = int(input("What is the shift amount? "))
    direction = input("Do you want to encode or decode? ")

    #if the user enters the shift amount greater than the number of alphabets
    shift = shift % 26

    #calling the function
    caesar(text, shift, direction)

    restart = input("Do you want to go again? Type Y/N: ").upper()
    if restart == "N":
        should_continue = False


