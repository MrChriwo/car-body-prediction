## Car-Body-Prediction

This project is regarding the standford-cars-dataset which is available on kaggle.
Scope of this project is to predict the car body of a given image

### Usage to test the model 

opeen a terminal inside the project folder. While running docker desktop in background enter the following cmd: 

```docker build -t tf_env```

after the image was successfully build, you can run the container with 

```docker run -p 8888:8888 --name car_body_prediction tf_env```

NOTE: the container provides all dependencies to load the final model (you can ignore the warnings and erros). 
      because there are some dependencies which requires an nvidia GPU, you will not be able to run the entire model notebook inside the container (i.e. train the model). 

### Run the project without container: 
running the project outsite the provided container requires an python environment with all dependencies mentioned in **requirements.txt**
again, for running the model.ipynb notebook completly you will need to have an nvidia GPU or adjust the code for CPU usage. 
Because computational benefit, we've used the GPU for the Notebook. 

For using GPU it's highly recommended to use a Anaconda virtual enviornment. With that it's easy and fast to setup all dependencies 
for the GPU usage. 

[click here](https://www.tensorflow.org/install/pip) for more details setting up tensorflow with GPU usage. 
