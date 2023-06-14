def alternate_case(sentence):
    result = ""
    upper = True
    for char in sentence:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char
    return result

while True:
    line = input()
    if not line:
        break
    print(alternate_case(line))
