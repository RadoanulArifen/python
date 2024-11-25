list=[]
Name="Shikha"
Father_name="Muzam"
Mother_name="Haua"
Phone_number='01971700130'
list.append(Name)
list.append(Father_name)
list.append(Mother_name)
list.append(Phone_number)
print(list)

total_char=sum(len(word) for word in list)
print(total_char)
total_vowels=sum(word.count(char) for word in list for char in 'aeiouAEIOU')
print(total_vowels)