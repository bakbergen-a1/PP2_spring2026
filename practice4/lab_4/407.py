class Reverse:
    def __init__(self, text):
        self.text = text
    
    def __iter__(self):
        for i in range(len(self.text) - 1, -1, -1):
            yield self.text[i]

s = input()
for char in Reverse(s):
    print(char, end='')
print()