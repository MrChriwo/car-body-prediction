from os import listdir, path, remove, rename 
import pickle

def check_images(formats: list) -> dict: 
    c = 0
    dictonary = {}
    for dir in listdir("./photos"):
        directory = path.join("./photos", dir)
        files = listdir(directory)
        if len(files) > 1: 
            usefull_files = {dir: []}
            for fname in files: 
                if "." in fname: 
                    split = fname.split(".")
                    if split[-1] in formats: 
                        usefull_files[dir].append(fname)
                        c+= 1 
                        print(f"{c} of {len(files)} successfully checked", end="\r")
                else:
                    pth = path.join(directory, fname)
                    remove(pth)
            dictonary.update(usefull_files)
        else: 
            print(f"{directory} has no files")

    with open("picture_struct.pickle", "wb") as file: 
        pickle.dump(dictonary, file)
        print("file was created successfully")

check_images(["jpeg", "png"])

with open("./picture_struct.pickle", 'rb') as file:
    loaded_dict = pickle.load(file)

print(len(loaded_dict))