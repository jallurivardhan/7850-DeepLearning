## Language Translation using Neural Networks

### Project Overview

Welcome to the Language Translation project! The goal of this project is to implement a Recurrent Neural Network (RNN) sequence-to-sequence model using Keras for language translation, specifically from English to French. The system is designed to be adaptable to other language pairs.

### Sequence-to-Sequence Learning

Sequence-to-sequence learning involves training models to convert sequences from one domain to sequences in another domain. The process includes:

1. **Encoder LSTM:** Transforms input sequences into state vectors.
2. **Decoder LSTM:** Predicts target sequences based on the input, utilizing "teacher forcing" during training.
3. **Inference:** Generates predictions for unknown input sequences during testing.

For additional details, refer to the following papers:
- [Sequence to Sequence Learning with Neural Networks](#)
- [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](#)

### How to Use It

#### Requirements
- Python 3.x
- Keras
- NumPy

#### Clone and Install
```bash
git clone https://github.com/jallurivardhan/7850-DeepLearning.git
cd 7850-DeepLearning
pip install -r fra.txt
```

#### Run Training
```bash
python training.py
```
This script loads the dataset, preprocesses it, builds and trains the Seq2Seq model. Training logs are saved in the log directory.

#### Run Prediction
```bash
python PredictionTranslation.py
```
This script loads the trained model and performs translation for the given input sentence.

### Customization

- Modify `data_path` in `training.py` to point to your dataset.
- Adjust model architecture and training parameters in `util.py` if needed.

### File Descriptions

- **training.py:** Script to train the Seq2Seq model.
- **PredictionTranslation.py:** Script to perform translations using the trained model.
- **util.py:** Utility functions for data processing, model creation, and training.

### LSTM or GRU

The default model uses the LSTM cell, with an option to switch to the GRU cell for faster training.

### Downloading Weights

The model was trained on the complete English/French dataset, requiring several weeks. However, promising results were achieved after 18 hours of training (20 epochs). The weights can be downloaded [here](#).

### Results

While the system is not as accurate as Google Translate, it demonstrates accuracy for short sentences after 20 epochs.

#### Examples:

1. **Input:** "I love you."
   - **Decoded:** "Je t'aime !"
   - Accurate translation.

2. **Input:** "We studied."
   - **Decoded:** "Nous étudions."
   - Accurate translation.

3. **Input:** "I slept well."
   - **Decoded:** "J'ai dormi toute la journée."
   - Translation not fully accurate, but captures the meaning.

4. **Input:** "He worked a lot."
   - **Decoded:** "Il a travaillé pour un homme riche."
   - Translation not correct.

### Conclusion

In conclusion, the network has learned the basic concepts of English/French translation but requires more training time and a deeper architecture, such as incorporating additional LSTM cells, for improved accuracy.

### Citation

- [InterviewBit Blog](https://www.interviewbit.com/blog/deep-learning-projects/)
- [Fireblaze AI School](https://www.fireblazeaischool.in/blogs/language-translation-using-deep-learning/)
