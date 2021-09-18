# Stock Market Prediction using Long Short-Term Memory
The main aim of this project is to increase the accuracy of the prediction model by tweaking several hyper-parameters. The number of LSTM layers used would be fixed (75 units) but the parameters that are being changed are:- **BATCH_SIZE** for LSTM, **EPOCHS** and previous **DAYS**.

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


