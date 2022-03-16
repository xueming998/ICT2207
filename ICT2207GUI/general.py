from secrets import choice
import string
import glob, os
import fileinput
import random
import untangle

methodNames = []
newNames = []

returnFunctionType = ""
methodKey = ""
startReadingMethods = False
datatype = ['V','Z']
method = {}
methodLines = []

obj = untangle.parse("C:\\Users\\Jason\\Desktop\\original\\AndroidManifest.xml")
extract = obj.manifest.application.activity[0]['android:name']
mainName = extract.split(".")[-1]
path = extract.split(mainName)[0]
fullPath = path.replace(".", "/")

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

os.chdir("C:\\Users\\Jason\\Desktop\\original\\smali\\edu\\singaporetech\\travelapp")
for file in glob.glob("*.smali"):
    if (file == mainName + ".smali"):
        continue
    with open(file, 'r') as file_open:
        for line in file_open:
                # encode characters
                line = line.rstrip()
                if (".method" in line and "constructor" not in line) and (".method" in line and "onCreate" not in line) and (".method" in line and "displayResult" not in line):
                    removeBracket = line.split('(')[0]
                    methodNames.append(removeBracket.split()[len(removeBracket.split())-1])

                    returnFunctionType = line[len(line)-1]

                    if (returnFunctionType) != ";":
                        newFunctionType = random.choice(datatype)
                        if newFunctionType != returnFunctionType:
                            line = line[:-1] + line[len(line)-1].replace(line[len(line)-1], newFunctionType)
                            method[line] = methodLines.append(file)

                        startReadingMethods = True
                    else:
                        continue

                if (".end method" in line):
                    if methodLines:
                        for key in method.keys():
                            if key == methodLines[1]:
                                del methodLines[1]
                                if (newFunctionType == 'Z'):
                                    methodLines[len(methodLines)-1] = "    const/4 v1, 0x1"
                                    methodLines.append("    return v1")
                                if (newFunctionType == 'V'):
                                    methodLines[len(methodLines)-1] = "    return-void"
                                method[key] = methodLines
                    startReadingMethods = False
                    methodLines = []

                if (startReadingMethods == True):
                    if (".locals" in line) and (newFunctionType == 'Z'):
                        line = line[:-1] + str(int(line[len(line)-1]) + 1)
                    methodLines.append(line)

for i in range(0, len(methodNames)):
    randomName = ''.join([choice(string.ascii_uppercase + string.digits) for _ in range(10)])
    newNames.append(methodNames[i])
    newNames.append(randomName)


d = {}
d = Convert(newNames)
replace = False

for file in glob.glob("*.smali"):
    if (file == mainName + ".smali"):
        continue
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

        for m_key in method.keys():
            data = method[m_key]
            if (file == data[0]):
                del data[0]
                for content in data:
                    for f_key, f_value in d.items():
                        if f_key in m_key:
                            m_key = m_key.replace(str(f_key), f_value)
                            file_write.write("\n" + m_key + "\n")

                    else:
                        file_write.write(content + "\n")
                file_write.write("\n" + ".end method")





