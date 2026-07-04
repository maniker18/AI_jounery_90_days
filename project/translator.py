def translator(pharse):
    result = ""
    for letters in pharse:
        if letters.lower() in 'aeiou':
            if letters.islower():
                result = result +'g'
            
            else:
                result = result +'G'

           
            
        else:
            result = result + letters
    return result       




print(translator(input("enter your sentence or a letter to translate vowels to k : ")))