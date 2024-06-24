import yaml

with open("eg.yaml", "r")as file:
    result = yaml.safe_load(file)
# print(type(result))
result['Languages'] = {'python' : '4', 'java' : '3', 'c++' : '2', 'go' : '1'}
# print(result) 

with open("eg.yaml", "w")as file:
    yaml.dump(result, file, sort_keys=True)
print(result)

print ("Modified yaml script for pull request")
