from keras.models import load_model
from utils import *

filename = "char2encoding.pkl"
sentence = "Stay cool"

input_token_index, _, _, reverse_target_char_index, _, target_token_index = get_char2encoding(filename)

encoder_input_data = encode_sentence_to_predict(sentence, input_token_index, 16, len(input_token_index))
encoder_model = load_model('encoder_modelPredTranslation.h5')
decoder_model = load_model('decoder_modelPredTranslation.h5')

input_seq = encoder_input_data

decoded_sentence = decode_sequence(input_seq, encoder_model, decoder_model, len(target_token_index), target_token_index, reverse_target_char_index)
print('-')
print('Input sentence:', sentence)
print('Decoded sentence:', decoded_sentence)
