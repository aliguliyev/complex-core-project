from zipfile import ZipFile
import os


def generate_zip(file):
    zipObj = ZipFile(file["name"] + '.zip', 'w')
    print("hgqjhbjhefjhwef",file["name"])
    print(zipObj)
    for name in file["res"]:
        zipObj.write(name, name.split("/")[-1])
        os.remove(name)
    zipObj.close()
    


