vowels = ['a','e','i','o','u']
consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
letter = input()
if(letter in vowels):
    print("Vowel")
elif(letter in consonents):
    print("Consonant")
else:
    print("invalid")
