def count_vowels(string):
    list_with_vowels = "aeiouy"
    sum = 0
    string = string.lower()
    for x in range(0, len(string)):
        for y in range(0, len(list_with_vowels)):
            if(string[x] == list_with_vowels[y]):
                sum += 1
    return sum

print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("A nice day to code!"))
