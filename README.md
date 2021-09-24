# Stock Market Prediction using LSTM (Research)
The research cum project revolves around the capability of LSTM to make predictions. The model tries to predict the next opening price of the Stock Market.
The main aim of this project is to increase the accuracy of the prediction model by tweaking several **hyper-parameters**. The number of **LSTM** layers used would be fixed (75 units) but the parameters that are being changed are:- **BATCH_SIZE** for LSTM, **EPOCHS** and previous **DAYS**.   
___
## Abstract
**LSTM** or **Long Short-Term Memory** is an improvement over traditional **RNN** or **Recurrent Neural Network** in the sense that it can effectively “remember” **long sequence of events in the past**. Just like humans can derive information from the previous context and can chart his future actions, **RNN** and **LSTM** tends to imitate the same. The difference between **RNN** and **LSTM** is that **RNN** is used in places where the **retention of memory is short**, whereas **LSTM** is capable of connecting events that happened way earlier and the events that followed them.   
   
Hence, it (LSTM) is one of the **best** choices when it comes to analyzing and predicting **temporal dependent** phenomena which spans over a **long period** of time or multiple instances in the past.   
   
**LSTM** is capable of performing three main operations: **Forget**, **Input** and **Output**. These operations are made possible with the help of trained neural network layers like the **tanh layer** and the **sigmoid layer**. These layers decide whether an information needs to be **forgotten**, **updated** and what values need to be given as **output**. **LSTM** learns which parameter to learn, what to forget and what to be updated during the **training process**. That is the reason why **LSTM** requires a **huge amount of dataset** during its training and validation process for a **better result**. The **sigmoid layer** decides the flow of information. Whether it needs to allow all of the information or some of it or nothing.   
There are multiple gates that performs the role of **Forget**, **Input** and **Output**. These gates perform the respective operation on the **cell state** which carries information from the past. The **forget gate layer** tells the **LSTM** cell whether to keep the past information or completely throw away. The **input gate** determines what new information should be added to the cell state. The **output gate** finally gives the output which is a filtered version of the cell state.

## Background Information
### What is Machine Learning?
Machine learning is a branch of **artificial intelligence (AI)** and **computer science** which focuses on the use of data and algorithms to imitate the way that humans learn, gradually **improving its accuracy**.
### How is it Different from Deep Learning?
- **Machine Learning** is the superset. **Deep Learning** is the subset.
- ML is the ability of computers to learn and act with less human intervention.
- DL is all about mimicking the thinking capability of the human brain and arriving at a conclusion just like a human does after analyzing and thinking about it for a while.
### Artificial Intelligence vs Machine Learning vs Deep Learning   
![image](https://user-images.githubusercontent.com/55954313/133870891-0423a591-7518-45e7-8bfc-a125b82fa160.png)
### Neural Networks
**Neural networks**, also known as **Artificial Neural Networks (ANNs)** are a subset of **Machine Learning** and are at the **heart of Deep Learning algorithms**. Their name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.   
   
It comprises of several **nodes** which represent **neurons**. A collection of nodes creates a **node layer**. These node layers play specific roles. Some acts as **input layer**, some **hidden layers** and some acts as **output layer**. Each **node**, or **artificial neuron**, connects to another and has an **associated weight and threshold**. It is by tweaking these weights and thresholds, that the network is able to learn progressively.   
   
There are different types of neural nets : **Convoluted Neural Networks**, **Recurrent Neural Networks**, etc.
### Simplest Neural Network
![image](https://user-images.githubusercontent.com/55954313/133871109-a721309a-9d14-435f-8d32-167c6b15c0d8.png)   
This is called a **perceptron**. It has only one **input layer**, one **hidden layer** comprising of only one **node** and one **output layer**.   
#### Source: https://www.ibm.com/in-en/cloud/learn/neural-networks
### Deep Neural Network
![image](https://user-images.githubusercontent.com/55954313/133872209-40ad4e68-71de-47d4-984d-499599da59f1.png)   
- Contains multiple hidden layers
- Since the depth of hidden layers is deep, hence the name.
#### Source: https://www.ibm.com/in-en/cloud/learn/neural-networks
### Recurrent Nueral Network
![image](https://user-images.githubusercontent.com/55954313/133872292-e603b584-8ad2-43d1-8bdf-863d66e4c823.png)   
#### Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs
- Uses sequential data or time series
- Used in solving temporal dependent problems: Natural language processing, image captioning, speech recognition, voice search, translation, etc.
- Inefficient when it comes to prediction where the outcome is long term temporal dependent.
- The reason being Exploding and Vanishing gradient.
- LSTM overcomes the drawback
### Long Short Term Memory
![image](https://user-images.githubusercontent.com/55954313/134108241-e04cf3cb-e1ef-4aa0-b594-e147ea11d5cb.png)
#### Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs
- Contains a cell state that carries information from one state to another
- Gates manipulate the info in the cell state. Three main gates used to do this are: **Forget gate**, **Input gate**, **Output gate**.   
   
![image](https://user-images.githubusercontent.com/55954313/134108503-8be7d9d1-ddd3-4dc9-863b-09d48d60162f.png)
- **Forget Gate**: Responsible for removing useless information. 
- **Input Gate**: Responsible for adding new information.
- **Output Gate**: Responsible for filtering out the information.
___
# Project Disposition
## Description
- An attempt to predict the **Stock Market Price** using **LSTM** and analyze it's accuracy by tweaking its **hyper-parameters**.
- For this purpose, **two Stocks** have been used for training the model: **Bitcoin Market** and **USD/CAD Forex**.
- A total of **48 models** will be trained for each **Stock**. Each model will be different from other in the sense they will be trained on **different hyperparameters**.
- The **line charts** of all the models will be plotted, its accuracy will be observed.
## Plan Of Attack
- Data Acquisition
- Data Preprocessing
- Structuring Data
- Creating the model
- Training the model
- Prediction
- Plotting chart and accuracy analysis
## Data Acquisition
![image](https://user-images.githubusercontent.com/55954313/134459659-0c12c930-7e72-4e26-b182-bd6adc7e1ff5.png)
- [Yahoo finance](https://finance.yahoo.com/) maintains past data of hundreds of Stock Markets. One can easily download the data in the form of CSV files and use it for training.
- Past 5 years data is downloaded for both Bitcoin and USD/CAD Forex.  
  
![image](https://user-images.githubusercontent.com/55954313/134459760-ddfe7096-024f-459b-a000-6ee536302559.png)
## Data Preprocessing
### 1. Data Cleaning
One of the many important stages in creating an efficient model. Data contains **discrepancies**. If not removed, they might cause hinderance in producing accurate results. **Null** values are the most common.   
   

![image](https://user-images.githubusercontent.com/55954313/134460077-078bc697-5b8d-427c-a8c4-000f2d326117.png)   
   
### 2. Data Extraction
Not all the data that we downloaded are necessary for training purpose. Fields like **Date** are unnecessary, hence we don't need them. In this project, I have chosen **Open** (which stores the **opening price of the market**) as the deciding variable that predicts the outcome. Remember that one can choose **multiple** deciding factors as well. The reason I have chosen **Open** field is because, certainly, the **Stock Market price** depends on the previous days' opening prices. If I were to buy a Stock, I will definitely look at opening price among other factors. Hence training the model on opening price seems feasible. But one can always opt for multiple deciding factors like considering both **opening** and **closing** price together.   

Now the extracted data is stored in a 2D array for futher processing.   
   
![image](https://user-images.githubusercontent.com/55954313/134460621-b617c046-71da-4b30-8042-2bdb753fcd6a.png)   

### 3. Feature Scaling
Feature scaling is the most important part of Data preprocessing. It helps in standardizing / normalizing the given dataset so that one entity is not given more importance than the other solely based on their quantity. Consider this as bringing all the scattered data within the same level for easier analysis. I have used MinMaxScaler() to scale all the values between 0 and 1.   
   
![image](https://user-images.githubusercontent.com/55954313/134461232-deb53e49-5c4b-4979-9d0c-8ebb393dfab0.png)
## Structuring Data
- The LSTM takes a series as an input. The length of the series is equivalent to the number of previous days. 
- X_train will be the inputs for training set
- y_train is the output for training set   
Similar data structure is created for preparing prediction dataset.   
   
![image](https://user-images.githubusercontent.com/55954313/134461506-cec484ab-00e7-4b54-b89e-439b9e48ae13.png)   
Structuring the data for training purpose. The model will use the previous 30 days as the deciding factor and will predict the opening price for 31st day.
## Creating the model
   

![image](https://user-images.githubusercontent.com/55954313/134461881-7823e6ea-e5b4-450b-a530-57c0c42e0214.png)   
## Training the model
This is the stage where we play with the hyper-parameters to bring about changes in the how the machine learns. The parameters which will be tweaked are: **BATCH_SIZE** for LSTM, **EPOCHS** and previous **DAYS**   
   
![image](https://user-images.githubusercontent.com/55954313/134462547-4bc9d677-8ce6-4cac-bbb9-f97cdc57a5e8.png)
![image](https://user-images.githubusercontent.com/55954313/134461977-4489555a-3303-4096-9349-06bfd65c504c.png)

## Prediction
The model has been trained. Now its time to predict the next day's price. For this purpose, a test dataset is created which contains past days' opening prices. This dataset is structured the same way as done in the Data Structuring step. Then these values are fed one by one to the LSTM input layer and the output is collected and stored in a 2D array for chart plotting and accuracy analysis.   
   
![image](https://user-images.githubusercontent.com/55954313/134629026-79575fa9-fb67-4b24-9003-59fd2bc1a621.png)

## Plotting the Chart
Based on the output we gathered, a line chart is plotted. The chart contains both the predicted and original price for accuracy analysis. From these charts we can clearly identify which model performed well.   
   
![image](https://user-images.githubusercontent.com/55954313/134462808-d9766f4a-888e-46bc-8275-782247adbba7.png)

# Tweaking the Hyper-parameters
Tweaking hyper parameters brings about a change in how the model learns and analyzes the given data. Hyper parameters considered in this research project are: Batch Size, Number of Epochs, Number of Days. A total of 48 different models are created. Each containing different hyperparameters.   
   
![image](https://user-images.githubusercontent.com/55954313/134464758-0d48126d-8aa4-4f96-8428-2ba16ba73afd.png)  
   

![image](https://user-images.githubusercontent.com/55954313/134462983-1dd451bf-b02d-4c68-b21c-d422725bd559.png)
# Bitcoin Market Models   
All the 48 models of Bitcoin Market have been prepared and stored in this project. They can be accessed by using the GUI created. Some snapshots of the model are given below:   
   
### MODEL 1
![BTC_B5_E1_D30](/images/BTC_B5_E1_D30.jpg)   
### MODEL 48
![BTC_B32_E100_D120](/images/BTC_B32_E100_D120.jpg)
# USD/CAD Forex Market Models   
All the 48 models have been prepared and stored in this project. They can be accessed by using the GUI created. Some snapshots of the models are given below (red border means higher accuracy):   
   
### MODEL 1
![USDCAD_B5_E1_D30](/images/USDCAD_B5_E1_D30.jpg)   
### MODEL 48
![BTC_B32_E100_D120](/images/USDCAD_B32_E100_D120.jpg)   
   
***
# Graphical User Interface to view the charts
![image](https://user-images.githubusercontent.com/55954313/134464944-a989e128-8dca-4a8b-9eb6-7cca404e2dd8.png)
