word_to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

digit_to_word = {v: k for k, v in word_to_digit.items()}


def decode(s):
    number = ""
    for i in range(0, len(s), 3):
        number += word_to_digit[s[i:i+3]]
    return int(number)


def encode(n):
    if n == 0:
        return "ZER"
    result = ""
    for d in str(n):
        result += digit_to_word[d]
    return result


expr = input()

# find operator
for op in "+-*":
    if op in expr:
        left, right = expr.split(op)
        a = decode(left)
        b = decode(right)

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        else:
            res = a * b

        print(encode(res))
        break
