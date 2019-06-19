#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:46:51 2019

@author: Vsevolod
"""
with open('data.txt', 'r') as file:
        text = file.read()
        lines = text.lower().split('\n')
from keras.preprocessing.text import text_to_word_sequence, Tokenizer
words= text_to_word_sequence(text)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(words)
vocabulary_size = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(lines)
subsequences = []
for sequence in sequences:
    for i in range(1, len(sequence)):
        subsequence = sequence[:i+1]
        subsequences.append(subsequence)
from keras.preprocessing.sequence import pad_sequences
sequence_length = max([len(sequence) for sequence in sequences])
sequences = pad_sequences(subsequences, maxlen=sequence_length, padding='pre')
from keras.utils import to_categorical
x, y = sequences[:,:-1],sequences[:,-1]
y = to_categorical(y, num_classes=vocabulary_size)
from keras.models import Sequential 
model = Sequential()
from keras.layers import Embedding
model.add(Embedding(input_dim = vocabulary_size, # 582
                    output_dim = 100,
                    input_length = sequence_length - 1)) # input_dim
from keras.layers import LSTM 
model.add(LSTM(units = 100))
from keras.layers import Dropout, Dense 
model.add(Dropout(0.1))
model.add(Dense(units=vocabulary_size, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=500)