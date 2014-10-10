def count_consonants(string):
    list_with_consonants = "bcdfghjklmnpqrstvwxz"
    sum = 0
    string.lower()
    for x in range(0, len(string)):
        for y in range(0, len(list_with_consonants)):
            if(string[x] == list_with_consonants[y]):
                sum += 1
    return sum

print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga"))
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))
