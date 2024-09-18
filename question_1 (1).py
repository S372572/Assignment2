# -*- coding: utf-8 -*-


#question 1  task  1
import os
from glob import glob
import cv2
import numpy as np
from skimage import measure
import matplotlib.pyplot as plt


csv_directory = 'C:/Users/ali40/Desktop/Assignment2/extracted.txt'

text_data = []

csv_directory = 'C:/Users/ali40/Desktop/Assignment2' 

text_data = []

for file_name in os.listdir(csv_directory):
    if file_name == 'extracted.txt': 
        file_path = os.path.join(csv_directory, file_name)
        df = pd.read_csv(file_path)
        if 'text' in df.columns:
            text_data.extend(df['text'].dropna().tolist())

# Write all text data to a single '.txt' file
with open('extracted_texts.txt', 'w', encoding='utf-8') as text_file:
    text_file.write('\n'.join(text_data))

#question 1  task  2
# Install Spacy and Scispacy
!pip install spacy scispacy

# Install the Transformers library
!pip install transformers

# Install Biopython
!pip install biopython

# Install PyTorch
!pip install torch

# Download the en_core_sci_sm model for Spacy
!python -m spacy download en_core_sci_sm

# Download the en_ner_bc5cdr_md model for Scispacy
!python -m scispacy download en_ner_bc5cdr_md

!pip install biobert-embed

#question 1  task  3 -->  3.1
from collections import Counter
import re

# Read the extracted text file
with open('extracted_texts.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Remove punctuation and lowercase all words
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Save the top 30 words to a CSV file
df_top_words = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
df_top_words.to_csv('top_30_words.txt', index=False)



#question 1  task  3 -->  3.2
from transformers import AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def count_unique_tokens(text):
    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    unique_tokens = set(tokens)
    return len(unique_tokens), unique_tokens

# Count unique tokens in the text
unique_token_count, unique_tokens = count_unique_tokens(text)
print(f"Unique Token Count: {unique_token_count}")



#question 4
import spacy
import scispacy

# Load the SciSpacy NER models
nlp_sci = spacy.load("en_core_sci_sm")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

def extract_entities(text, model):
    doc = model(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

# Extract entities using SciSpacy models
entities_sci = extract_entities(text, nlp_sci)
entities_bc5cdr = extract_entities(text, nlp_bc5cdr)

# Compare the differences between two models
def compare_entities(entities1, entities2):
    entities1_set = set(entities1)
    entities2_set = set(entities2)
    common_entities = entities1_set.intersection(entities2_set)
    unique_entities1 = entities1_set - entities2_set
    unique_entities2 = entities2_set - entities1_set
    return common_entities, unique_entities1, unique_entities2

common_entities, unique_entities_sci, unique_entities_bc5cdr = compare_entities(entities_sci, entities_bc5cdr)
print(f"Common Entities: {len(common_entities)}")
print(f"Unique Entities in SciSpacy: {len(unique_entities_sci)}")
print(f"Unique Entities in BC5CDR: {len(unique_entities_bc5cdr)}")

from biobert_embedding.embedding import BiobertEmbedding

biobert = BiobertEmbedding()

# Extract entities using BioBERT
biobert_entities = biobert.sentence_vector(text)