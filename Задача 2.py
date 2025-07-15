word = "Hello"
repeated_char = None

for char in word:
    if word.count(char) > 1:
        repeated_char = char
        break

print("Повторяющийся символ:", repeated_char)