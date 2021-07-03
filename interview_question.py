


def  question(my_string):
    count = {}
    for char in my_string:
        if char in count:
                return char
        count[char]  = 1
    return None



print(question("ABC"))
