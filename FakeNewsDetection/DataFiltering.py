import pandas as pd
import re

found_links = []

def remove_non_ascii_words(text):
    ascii_word_pattern = re.compile(r'[^\x00-\x7F]+')
    ascii_words = ascii_word_pattern.sub('', text)
    return ascii_words

def remove_urls(text):
    url_pattern = re.compile(r'http[s]?://\S+')
    urls = url_pattern.findall(text)
    found_links.extend(found_links)
    return url_pattern.sub('', text)

def clean_text(text):
    text = remove_non_ascii_words(text)
    text = remove_urls(text)
    return text

def clean_dataset(dataset):
    cleaned_dataset = dataset.map(lambda x: clean_text(str(x)))
    cleaned_dataset = cleaned_dataset.replace('', pd.NA).dropna(how='all')
    return cleaned_dataset


fake_dataset = pd.read_csv('Fake.csv')
true_dataset = pd.read_csv('True.csv')

fake_dataset = clean_dataset(fake_dataset)
true_dataset = clean_dataset(true_dataset)

fake_dataset['label'] = '0'
true_dataset['label'] = '1'

# Merge the two CSV files
full_dataset = pd.concat([fake_dataset, true_dataset], ignore_index=True)

# Save the merged CSV to a new file
full_dataset.to_csv('FakeReal.csv', index=False)

with open('removed_urls.txt', 'a') as f:
    for url in found_links:
        f.write(url + '\n')