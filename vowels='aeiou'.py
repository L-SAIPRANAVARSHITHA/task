vowels='aeiou'
consonants_count=0
vowels_count=0
string=str(input("enter the string"))
for i in string:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
    
print(vowels_count) 
print(consonants_count)
