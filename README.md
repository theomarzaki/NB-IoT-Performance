# Configuration Advocator for NB-IoT Devices

Command and Control Centre that queries NB-IoT Device for specific configurations, and replies to device with optimal set of configurations to improve the energy consumption, delay or both.

The interface utilises a number of machine and deep learning algorithm for environment prediction and configuration suggestions, the command and control centre utilises Deep Neural Network for prediction and Reinforcement Learning with Gradient Descent for suggestion.

## Configuring Configuration Advocator

The configuration directory, contains all the changeable parameters, to configure the CA.

* config.ini contains the variables that is used for the device connected, edge cloud address. the USB serial port can be changed to reflect where the connection to the device is.

* logstash.conf contains the port and the way the logs will be sent to the elk stack. Should be left alone unless the ports cannot be used, in which the ports can be changed **need to make sure the port is also changed in the docker-compose.yml file and ppp_options**.

* ppp_chat_isp and ppp_options are general configurations used to create a p2p connection and should be left as is.

## Dataset

* Dataset directory, contains the csv files used for training and testing the models. data_no_tx.csv and data_tx.csv are the processed datasets combining the rest of the files to reflect the features and attributes that will be used in the model training.

* data_no_tx.csv and data_tx.csv correspond to No Power Tx measurements and Power Tx measurements respectively.

## Models

* Directory contains all the final and best models for each approach from machine/deep learning models. These models are used in the Command and Control Centre.

* Contains the parameters for the preprocessing variables (MinMaxScaler).

* Only the Models for RL Gradient Descent for No Power Tx is used in the command control centre for all metrics (delay, energy consumption and combination) as best performing model.

## Running Machine/Deep Learning Models

### Dependencies

* Jupyter notebook
* Pandas
* Numpy
* Torch
* Matplotlib

### Dataset_Explore.ipynb

* This is a notebook, self contained, with the visualisations of the datasets.

* Data is preprocessed in this file.

* Split of the data_tx and data_no_tx subsets.

### Machine_Learning.ipynb

Contains the machine learning models used to predict single output and multiple output models for each of the metrics and data subsets.

### DNN_Regression.ipynb

Contains the Deep Neural Network models that predict the multi-output metrics for both data subsets.

### Reinforcement_Learning.ipynb

Contains the Reinforcement Learning Model (Deuling-DQN) that implements the Gradient Descent method for both subsets for each type of metric.

### NeuroEvolution.ipynb

Contains the Reinforcement Learning Model (DQN) that implements the Genetic Algorithm approach for all the metrics for the data subsets.

## Running Command and Control Centre

### Dependencies

* Docker-compose
* Docker
* `sudo sysctl -w vm.max_map_count=262144` -- increases the virtual machine map count, to allow for easier logging in the elk stack. default value is too little.

### Running docker containers

* To run the command and control centre, a swarm of docker containers are used managed by docker-compose. `docker-compose up --build`

* ELK stack and command and control centre will run in background

* `docker exec -it <container_id> bash` to enter the command and control centre container

* `python3 main.py --<flag>` for the different functionality of the command and control centre. `-h` lists all available functionality for the CA.
