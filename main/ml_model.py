from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import h5py
import numpy as np
import pickle
import sheet_parser as ken
import colorcode2 as nico


# file_name = "reptilia_tab.txt"
# with open(file_name, "rb") as tabb :
#     lines = tabb.readlines()
#
# test_sheet = tab_measure(lines)
#
# print(measures)

# Guitar hero note chart splits
mississippi_file = "./data/00mississippi_notes.png"
reptilia_file = "./data/00reptilia_notes.png"
talk_file = "./data/00talkdirty_notes.png"
mississippi_measures = nico.split_measures(mississippi_file)
reptilia_measures = nico.split_measures(reptilia_file)
talk_measures = nico.split_measures(talk_file)

all_measures = [tuple(mississippi_measures), tuple(reptilia_measures), tuple(talk_measures)]
#vocab = list(set(all_measures))
vocab = tuple(all_measures)
vocab_size = len(mississippi_measures) + len(reptilia_measures) + len(talk_measures)
print(vocab_size)
training_size_x = len(all_measures)


# Tab splits
miss_tab_file = "./tabs/mississippi_tabs.txt"
reptilia_tab_file = "./tabs/reptilia_tab.txt"
talk_tab_file = "./tabs/talkdirtytome_tab.txt"
miss_tab_split = ken.split_tab(miss_tab_file)
reptilia_tab_split = ken.split_tab(reptilia_tab_file)
talk_tab_split = ken.split_tab(talk_tab_file)

all_tabsplits = tuple(ken.measures)
training_size_y = len(all_tabsplits)

print(type(vocab[0]))
# Creates the mapping between the characters and orders the characters by least to most frequent
# only need to run once. later, just load it from pickle file

ix_to_notes = {ix:char for ix, char in enumerate(vocab)}
notes_to_ix = {char:ix for ix, char in enumerate(vocab)}

# Used to save a mapping to keep it consistent between runs
HIDDEN_DIM = 200
LAYER_NUM  = 2
BATCH_SIZE = 10
GENERATE_LENGTH = 30
SEQ_LENGTH = 100

length = int(vocab_size/SEQ_LENGTH)


pickle_file = "note_mappings.p"
combined_dict = [ix_to_notes, notes_to_ix]
with open(pickle_file, "wb") as picked :
    pickle.dump(combined_dict, picked)

def generate_song(model, length):
    ix = [np.random.randint(vocab_size)]
    # y_char = [ix_to_notes[ix[-1]]]
    X = np.zeros((1, length, vocab_size))
    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        try:
            nico.print_measure(ix_to_notes[ix[-1]][0])
        except:
            print("caught")
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        # y_char.append(ix_to_notes[ix[-1]])
    #return ('').join(y_char)
print(length)
X = np.zeros((length, SEQ_LENGTH, vocab_size))
y = np.zeros((length, SEQ_LENGTH, vocab_size))



# Create a training array for *length* number of sequences

for i in range(0, length):
    X_sequence = all_measures[i*SEQ_LENGTH:(i+1)*SEQ_LENGTH]
    X_sequence_ix = [notes_to_ix[value] for value in X_sequence]
    input_sequence = np.zeros((SEQ_LENGTH, vocab_size))
    for j in range(SEQ_LENGTH):
        try:
            input_sequence[j][X_sequence_ix[j]] = 1.
        except:
            print("lol")
    X[i] = input_sequence

    y_sequence = all_measures[i*SEQ_LENGTH+1:(i+1)*SEQ_LENGTH+1]
    y_sequence_ix = [notes_to_ix[value] for value in y_sequence]
    target_sequence = np.zeros((SEQ_LENGTH, vocab_size))
    for j in range(SEQ_LENGTH):
        try:
            target_sequence[j][y_sequence_ix[j]] = 1.
        except:
            print("rekt")
    y[i] = target_sequence



# Sequential is just a stack of layers
# each layer added with model.add(...)
#
# First layer:
# model.add(LSTM(HIDDEN_DIM, input_shape=(None, vocab_size), return_sequences=True))
# LSTM(...) - Says we're using a Long Short Term Memory Layer
# HIDDEN_DIM - not sure yet, right now using random number
# input_shape - The dimensions of the input to the layer, in this situation, it's the number of unique characters
# return_sequences - also not sure what this does
#
#
# Second to third to last Layer:
# model.add(LSTM(HIDDEN_DIM, return_sequences=True))
# Same as first layer, but doesn't have to define the input shape
#
# Second to last layer:
# model.add(TimeDistributed(Dense(vocab_size)))
# TimeDistributed - "This wrapper applies a layer of temporal slice of an input"




model = Sequential()

model.add(LSTM(HIDDEN_DIM, input_shape=(None, vocab_size), return_sequences=True))
#model.add(Dense(units=64, input_shape=(None, vocab_size), activation='relu', input_dim=100))
for i in range(LAYER_NUM - 1):
    model.add(LSTM(HIDDEN_DIM, return_sequences=True))
    #model.add(Dense(units=10, activation='softmax'))
model.add(TimeDistributed(Dense(vocab_size)))
model.add(Activation('softmax'))
#adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False) # Adam optimizer Jared told us to use
model.compile(loss="categorical_crossentropy", optimizer="adam")

nb_epoch = 0
#load weights in future runs
#model.load_weights("checkpoint_200_epoch_40.hdf5")
#generate_song(model, GENERATE_LENGTH)
print(type(X))
print(type(y))
print(len(X))
print(len(y))
while True:
    print('\n\n')
    model.fit(X, y, batch_size=BATCH_SIZE, verbose=1, epochs=1)
    nb_epoch += 1
    generate_song(model, GENERATE_LENGTH)
    if nb_epoch % 10 == 0:
        model.save_weights('checkpoint_{}_epoch_+1{}.hdf5'.format(HIDDEN_DIM, nb_epoch))
