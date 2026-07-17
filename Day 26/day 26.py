#Regexp:
#1.match:startswith
'''import re
pattern=r'[A-Z]'
text='Python vaersion 3.13'
res=re.match(pattern,text)
print("Match found" if res else "Match not found")'''

'''import re
pattern=r'\d'#to check whether it starts with digit 
text='Python vaersion 3.13'
res=re.match(pattern,text)
print("Match found" if res else "Match not found")'''


#2.search:to search something in the string
'''import re
pattern=r'\d'
text='Python version 3.13.13'
res=re.search(pattern,text)
print("Match found" if res.group() else "Match not found")'''



'''import re
pattern=r'[A-Z]'
text='Python version 3.13'
res=re.search(pattern,text)
print(res.group() if res else "Match not found")'''

#findall:used to get a list of elements
'''import re
pattern=r'[0-9]'
text='Python version 3.13'
res=re.findall(pattern,text)
print(res)'''

'''import re
pattern=r'[a-z]{3}'
text='Python version 3.13'
res=re.findall(pattern,text)
print(res)'''

#finditer:
'''import re
pattern=r'[0-9]{2}'
text='Python version 3.13.13'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())'''

#fullmatch:entire string should match with str
'''import re
pattern=r'[0-9]{2}'
text='12'
res=re.fullmatch(pattern,text)
print(res.group() if res else "Match not found")'''


#sub:used to replace the text in the str
'''import re
pattern=r'[0-9]'
text='Python version 3.13'
res=re.sub(pattern,'*',text)
print(res)'''

#vowels with *:
'''import re
pattern=r'[aeiouAEIOU]'
text='Python version 3.13'
res=re.sub(pattern,'*',text)
print(res)'''


#split:used to split the text in the str by a separator
import re
pattern=r'[,;:]'
text='Python,version; 3:13'
res=re.split(pattern,text)
print(res)

