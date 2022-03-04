from secrets import choice
import string
import glob, os
import fileinput

methodNames = []
newNames = []

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

os.chdir("C:\\Users\\Jason\\Desktop\\original\\smali\\edu\\singaporetech\\travelapp")
for file in glob.glob("*.smali"):
    with open(file, 'r') as file_open:
        for line in file_open:
                # encode characters
                line = line.rstrip()
                if (".method" in line and "constructor" not in line) and (".method" in line and "onCreate" not in line):
                    if line.split()[1] == "protected":
                        removeBracket = line.split('(')[0]
                        methodNames.append(removeBracket.split()[2])
                    else:
                        removeBracket = line.split('(')[0]
                        methodNames.append(removeBracket.split()[3])



for i in range(0, len(methodNames)):
    random = ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(10)])
    newNames.append(methodNames[i])
    newNames.append(random)



d = {}
d = Convert(newNames)
print(d)
replace = False

for file in glob.glob("*.smali"):
    with open(file, 'r') as file_read:
        content = file_read.readlines()
    with open(file, 'w') as file_write:
        for line in content:
            for f_key, f_value in d.items():
                if f_key in line:
                    line = line.replace(str(f_key), f_value)
                    file_write.write(line)
                    replace = True

            if (replace == True):
                replace = False
                continue
            else:
                file_write.write(line)
