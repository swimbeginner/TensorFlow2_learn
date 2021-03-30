##%%
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


sentences=[
    'I love my dog',
    'I love my cat',
#    'You love my dog!',
#    'Do you think my dog is amazing?'
]

tokenizer=Tokenizer(num_words=3, oov_token=None)
tokenizer.fit_on_texts(sentences)
print(tokenizer.word_index)

##%
len(sentences)

##%%
test_data=[
    'my dog love my manetee',
    'i love my manetee'
]
index_sequence=tokenizer.texts_to_sequences(test_data)
print(index_sequence)
pad_sequence=pad_sequences(index_sequence, padding='pre', maxlen=8)
print(pad_sequence)