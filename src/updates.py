import pickle
import re
import pandas as pd
from base import Base
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from pathlib import Path
import spacy

# Set folder directory to store the data
folder_dir = f'{Path(__file__).parents[0]}\\data'

# Fix lowercase C:// in path.
folder_dir = folder_dir[0].upper() + folder_dir[1:]

# Create a .csv file:
Base().df.to_csv(f'{folder_dir}\\oracle_data.csv', index=False)

# Read in the data to a dataframe object
df = pd.read_csv(f'{folder_dir}\\oracle_data.csv', low_memory=False)
print('Created DataFrame')
# Create the lemmatizations of the dataframe object:
# Drop all null values from oracle text column
df.dropna(subset=['oracle_text'], axis = 0, inplace=True)

# Drop all values from oracle text that are empty strings"
df.drop(df.index[df['oracle_text'] == ''],inplace=True)
print("Dropped all values that are null/empty")
# Using regex, remove all non alpha-numeric values from our column
df['oracle_text'] = [re.sub('[^0-9a-zA-Z]+', " ", i) for i in df.oracle_text]

# Load in spacy dictionary
nlp = spacy.load('en_core_web_md')
lemmas = []
for doc in df['oracle_text']:
    lemmas.append([token.lemma_.lower().strip() for token in nlp(str(doc)) if (token.is_stop != True) and (token.is_punct != True) and (token.is_space != True)])

df['lemmas'] = lemmas
print("Successfully created lemma column in dataframe object")

# Save back over the csv file with the newly updated information:
df.to_csv(f'{folder_dir}\\oracle_data.csv', index=False)
print('Saved DataFrame object to CSV after Lemma Update')
# Create our vectorizer:
def dummy_func(doc):
    return doc

# Create the vect and save the vocab
vect = TfidfVectorizer(preprocessor=dummy_func,
                       token_pattern=None,
                       tokenizer=dummy_func)

vect.fit(df['lemmas'])
vect_vocab = vect.vocabulary_

# Save the entire vectorizer and the vocab:
pickle.dump(vect, open(f'{folder_dir}\\vect', 'wb'))
pickle.dump(vect_vocab, open(f'{folder_dir}\\vect_vocab', 'wb'))
print('Successfully saved vect and vocab objects')

# Create the model and save that to a file as well.
model = NearestNeighbors(n_neighbors=12)
model.fit(vect.transform(df.lemmas))
pickle.dump(model, open(f'{folder_dir}\\model', 'wb'))
print('Model has been created and saved')
print("All required updates have been completed")