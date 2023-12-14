# 7850-DeepLearning
Language Translation using Neural Networks

Project Purpose:
The objective of this project is to implement a Recurrent Neural Network (RNN) sequence-to-sequence model using Keras for language translation, specifically from English to French. While the default language pair is English to French, the system is designed to be adaptable to other language pairs. The ANKI dataset is utilized for training, and it can be easily obtained here.

What is Sequence-to-Sequence Learning?
Sequence-to-sequence learning involves training models to convert sequences from one domain to sequences in another domain. The process can be summarized as follows:

Input sequences from a domain (e.g., English sentences) and corresponding target sequences from another domain (e.g., French sentences) are provided.

An encoder LSTM transforms input sequences into two state vectors, retaining the last LSTM state and discarding the outputs.

A decoder LSTM is trained to predict the target sequences, given the input sequences. During training, a technique called "teacher forcing" is employed, where the model is forced to predict the next timestep's output based on the ground truth. The decoder uses the initial state vectors from the encoder.

During inference, the model generates predictions for unknown input sequences by encoding the input, initializing the target sequence, and iteratively predicting the next character until the end-of-sequence character is generated or a character limit is reached.

For additional details, refer to the following papers:

Sequence to Sequence Learning with Neural Networks
Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation
How to Use It
This repository contains Python scripts for training and using a Neural Machine Translation (NMT) model using a Seq2Seq architecture. The model is designed for translation between different languages and utilizes Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) layers.

Requirements
Python 3.x
Keras
NumPy

Clone the repository:
git clone https://github.com/jallurivardhan/7850-DeepLearning.git
cd your-repository

Install the required dependencies:
pip install -r fra.txt

Run the training script:
python training.py
This script loads the dataset, preprocesses it, builds and trains the Seq2Seq model. Training logs are saved in the log directory.

Run the prediction script:
python PredictionTranslation.py
This script loads the trained model and performs a translation for the given input sentence.

Customization
You can modify the data_path variable in training.py to point to your own dataset.
Adjust the model architecture and training parameters in util.py if needed.

File Descriptions
training.py: Script to train the Seq2Seq model.
PredictionTranslation.py: Script to perform translations using the trained model.
util.py: Utility functions for data processing, model creation, and training.

LSTM or GRU
The default model utilizes the LSTM (Long Short-Term Memory) cell, but the option is provided to use the GRU (Gated Recurrent Unit) cell instead. The GRU cell, having only one gate, tends to speed up the training process.

Downloading Weights
The model was trained on the complete English/French dataset, requiring several weeks. However, promising results were achieved after 18 hours of training (20 epochs). The weights can be downloaded here.

Results
While the system is not as accurate as Google Translate, it demonstrates accuracy for short sentences after 20 epochs.

Examples:

Input: "I love you."
Decoded: "Je t'aime !"
Accurate translation.

Input: "We studied."
Decoded: "Nous étudions."
Accurate translation.

Input: "I slept well."
Decoded: "J'ai dormi toute la journée."
Translation not fully accurate, but captures the meaning.

Input: "He worked a lot."
Decoded: "Il a travaillé pour un homme riche."
Translation not correct.

Conclusion
In conclusion, the network has learned the basic concepts of English/French translation but requires more training time and a deeper architecture, such as incorporating additional LSTM cells, for improved accuracy.
