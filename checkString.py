def detectCapitalUse(word):
    for i in range(0, len(word)):
        if word[0].isupper() and word[1].isupper():
            print word[i]
            print "1", word[0].isupper() and word[1].isupper()
            if word[i].islower():
                return False
        if word[0].islower():
            if word[i].isupper():
                return False
        if word[0].isupper and word[1].islower():
            if i >0 and  not word[i].islower():
                return False
    return True

print detectCapitalUse('FlaG')
