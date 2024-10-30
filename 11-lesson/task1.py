def find_contrast(string1, string2):
    for i in range(len(string2)):
        if string2[i] not in string1 or string2.count(string2[i]) != string1.count(string2[i]): 
            return string2[i]

s1= "hello"
s2 = "hellor"
print(find_contrast(s1, s2), 'is added')
