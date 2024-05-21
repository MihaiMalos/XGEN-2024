import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.utils import shuffle

# Read the CSV file
data = pd.read_csv("FakeReal.csv")

# Shuffle the data
data = shuffle(data)

# Extract features and labels
x, y = data['text'], data['label']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Display the number of training samples
print(f"The number of train samples is {len(x_train)}")

# Vectorize the text data
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

# Train the classifier
clf = LinearSVC()
clf.fit(x_train_vectorized, y_train)

# Print the accuracy of the model
print(clf.score(x_test_vectorized, y_test))

# Display the number of test samples
print(f"The number of test samples is {len(y_test)}")

# Test the model with a sample text
# text = "LeBron Raymone James Sr. lə-BRON; born December 30, 1984) is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association (NBA). Nicknamed King James, he is widely recognized as one of the greatest players in the history of the sport and is often compared to Michael Jordan in debates over the greatest basketball player of all time.[a] He has competed in 10 NBA Finals (with eight consecutive appearances from 2011 to 2018), winning four NBA championships.[1] He also won the inaugural NBA Cup in 2023 with the Lakers, and two Olympic gold medals as a member of the U.S. men's national team."
# text = "World War I[j] or the First World War (28 July 1914 – 11 November 1918) was a global conflict between two coalitions: the Allies and the Central Powers. Fighting took place throughout Europe, the Middle East, Africa, the Pacific, and parts of Asia. One of the deadliest wars in history, it resulted in an estimated 9 million soldiers dead and 23 million wounded, plus up to 8 million civilian deaths from numerous causes including genocide. The movement of large numbers of troops and civilians during the war was a major factor in spreading the 1918 Spanish flu pandemic."

text = "Rudy Giuliani and 10 others pleaded not guilty in an Arizona court Tuesday to charges of allegedly conspiring to overturn the 2020 presidential election results. The former New York mayor was also ordered to post a $10,000 bond after he ducked efforts by the state to serve him with a summons over the past week. Giuliani was served Friday in Palm Beach, Florida, at his 80th birthday bash held by a GOP operative. Arizona prosecutors spent weeks trying to track down Giuliani and eventually found him based on some of his podcasts. A grand jury in Arizona handed up indictments last month charging over a dozen Donald Trump allies for their efforts to overturn his 2020 election loss, including the fake electors and several individuals connected to his campaign. Giuliani was joined by 10 other defendants entering their not-guilty pleas Tuesday. Four of those appeared virtually and six in person. The list includes: Christina Bobb, a Trump ally who now serves as the Republican National Committee’s top lawyer for “election integrity”; former Trump campaign aide Mike Roman; and former Arizona Republican Party Chair Kelli Ward."
vectorized_text = vectorizer.transform([text])
print(clf.predict(vectorized_text))