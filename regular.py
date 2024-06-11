import re

pattern = '[^a-e]'
string = 'aaby has a car'
result = re.findall(pattern, string)
result1 = re.search(pattern, string)
result2 = re.split(pattern, string)
print(result)
print(result1)
print(result2)

pattern = 'o{2,3}'
string = 'a afoot is a foot for a foootbal'
result = re.findall(pattern, string)
result1 = re.search(pattern, string)
result2 = re.split(pattern, string)
print(result)
print(result1)
print(result2)

string = 'manas will get a job'
pattern = '(a|b|j)'
match = re.findall(pattern, string)
result1 = re.search(pattern, string)
result2 = re.split(pattern, string)
print(match)
print(result1)
print(result2)
