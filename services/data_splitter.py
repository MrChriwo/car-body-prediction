import pandas as pd
from sklearn.model_selection import train_test_split

#def split1(images, labels, train, val, test):
#    train_ratio = train
#    validation_ratio = val
#    test_ratio = test

    # train is now  of the entire data set
#    images_train, images_test, labels_train, labels_test = train_test_split(images, labels, test_size=1 - train_ratio)

    # test is now 10% of the initial data set
    # validation is now 15% of the initial data set
#    images_val, images_test, labels_val, labels_test = train_test_split(images_test, labels_test, test_size= test_ratio/(test_ratio + validation_ratio)) 

#   return images_train, images_val, images_test, labels_train, labels_val, labels_test


#=================================================================================================================================

data = pd.read_csv("final_dataset_labeled.csv")

def split2(data, val, test):
    df = pd.read_csv("final_dataset_labeled.csv")

    images= df["images"]
    labels= df["labels"]

    validation_ratio = val
    test_ratio = test

    training_images, other_images, training_labels, other_labels = train_test_split(images, labels, test_size= (test_ratio+validation_ratio) , random_state= 1)

    validation_images, testing_images, validation_labels, testing_labels = train_test_split(other_images, other_labels, test_size= (test_ratio / (test_ratio + validation_ratio)), random_state= 1)

    return training_images, validation_images, testing_images, training_labels, validation_labels, testing_labels

    
