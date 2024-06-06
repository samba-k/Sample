import subprocess

result = subprocess.run(["python", "sub.py"], capture_output=True, text=True)
re = result.stdout
with open("file.txt", "w")as file:
    file.write(re)
file = open("file.txt", "r")
print(file.read())
