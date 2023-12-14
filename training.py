from utils import *

data_path = 'fra.txt'
encoder_input_data, decoder_input_data, decoder_target_data, input_token_index, target_token_index, _, _, _, _, _, _ = prepare_data(data_path)

model, decoder_outputs, encoder_inputs, encoder_states, decoder_inputs, decoder_lstm, decoder_dense = create_translation_model(len(input_token_index), len(target_token_index))

train_seq2seq(model, encoder_input_data, decoder_input_data, decoder_target_data)

encoder_model, decoder_model, reverse_target_char_index = generate_inference_model(encoder_inputs, encoder_states, input_token_index, target_token_index, decoder_lstm, decoder_inputs, decoder_dense)

save_char2encoding("/output/char2encoding.pkl", input_token_index, max_encoder_seq_length, len(input_token_index), reverse_target_char_index, len(target_token_index), target_token_index)
