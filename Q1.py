import os
import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification
from collections import Counter
import re
import csv

# The following function named extract_text_from_csv is used to extract text from CSV files and save to a single .txt file.
# First we used the open function to create and write into the output file. Then we used for-loop to open each csv file in the folder.
# Next we used os.path.join as was recommended by the teacher and read the csv file using panda library's read_csv() function.
# Next we use dataframe's tolist() function to separate all the text and then run for-loop to loop through each line of text and
# then write it in output file. This part of the code pertains to Task 1.
def extract_text_from_csv(folder_path, output_file, text_column):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                df = pd.read_csv(file_path)
                texts = df[text_column].tolist()
                for text in texts:
                    outfile.write(text + '\n')


# This function is created to count occurrences of words and save top 30 to CSV. It'll take 2 files as input in the argument.
# We will then attempt to read the file and save all the text read. Then using regex we find all the words. We then lowercase them
# to streamline the counting process. Then we call the Counter() function to count all the occurences and the most_common() function
# to save the output of top 30 words only. Then we proceed to create a csv file and using writerow() function, we output the results,
# in a presentable format.
def count_common_words(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    words = re.findall(r'\w+', text.lower())
    counter = Counter(words)
    common_words = counter.most_common(30)
    
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(common_words)

# We have created this function to get top 30 unique tokens using a tokenizer as was mentioned in the task 3. This 
# will take in 2 arguments. Tokenizer is from the Hugging Face's transformation library. The input file will be the one containing the texts.
# We first open and read the contents of the file in the text variable same as before. 
def get_top_tokens_from_text(tokenizer, input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    tokens = tokenizer.tokenize(text) # The tokenize method splits the text into smaller units called token, in this case which will be tokens.
    token_counter = Counter(tokens) # We will attempt to count the tokens here.
    
    return token_counter.most_common(30) # Finally we will return the most common 

# 1. We Extract text from CSVs and save to a text file
folder_path = 'csv'
output_file = 'combined_texts.txt'
extract_text_from_csv(folder_path, output_file, "TEXT")

# 2. Then Load the BioBERT tokenizer and model as required in the tasks.
biobert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
biobert_model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# 3. We count the top 30 common words and save to CSV.
count_common_words(output_file, 'top_30_words.csv')

# 4. Finally we get the top 30 tokens using a BERT tokenizer
bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
top_tokens = get_top_tokens_from_text(bert_tokenizer, output_file)
print(top_tokens)
