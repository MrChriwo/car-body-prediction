from os import listdir, path, remove, rename
import pickle

def check_images(formats: list) -> dict:
    c = 0
    # Create an empty dictionary to store useful files
    dictionary = {} 
    # Iterate through directories in the "./photos" directory
    for dir in listdir("./photos"):  
        directory = path.join("./photos", dir) 
        files = listdir(directory)  
        # If there are more than one file in the directory
        if len(files) > 1:
            useful_files = {dir: []} 
            # Iterate through files in the current directory
            for fname in files:
                # Check if the file has an extension
                if "." in fname: 
                    split = fname.split(".") 
                    # Check If the file extension is in the provided formats list
                    if split[-1] in formats:  
                        useful_files[dir].append(fname) 
                        c += 1 
                        print(f"{c} of {len(files)} successfully checked", end="\r") 
                else: 
                    pth = path.join(directory, fname) 
                    remove(pth)  #
            dictionary.update(useful_files) 
        else:
            print(f"{directory} has no files")  

    # safe all to pickle file
    with open("picture_struct.pickle", "wb") as file:  
        pickle.dump(dictionary, file) 
        print("file was created successfully") 

check_images(["jpeg", "png"])

with open("./picture_struct.pickle", 'rb') as file:
    loaded_dict = pickle.load(file)

print(len(loaded_dict))
