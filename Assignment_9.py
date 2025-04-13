I really enjoy playing esports games like Valorant. They are super competitive and exciting, and I usually play them after classes or on weekends. I also like watching professional tournaments online because it’s fun to see how good the pros are. Sometimes I even learn new tricks or strategies by watching them. My friends and I usually play as a team, and it’s a great way to bond while having fun. I think esports are becoming more popular because people take gaming seriously now, not just for fun but even as a career.

#Question 1:
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# downloading stuff
nltk.download('punkt')
nltk.download('stopwords')

# original text
para = "I really enjoy playing esports games like Valorant, League of Legends, and CS:GO. They are super competitive and exciting, and I usually play them after classes or on weekends. I also like watching professional tournaments online because it’s fun to see how good the pros are. Sometimes I even learn new tricks or strategies by watching them. My friends and I usually play as a team, and it’s a great way to bond while having fun. I think esports are becoming more popular because people take gaming seriously now, not just for fun but even as a career."

# lowercase + remove punctuation
lower_para = para.lower().translate(str.maketrans('', '', string.punctuation))

# tokenize
words = word_tokenize(lower_para)
sentences = sent_tokenize(lower_para)

# remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]

# frequency
fdist = FreqDist(filtered_words)

print("Tokenized Sentences:", sentences)
print("Filtered Words:", filtered_words)
fdist.plot()

#Question 2:
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

# stemming
porter_stem = [porter.stem(word) for word in filtered_words]
lancaster_stem = [lancaster.stem(word) for word in filtered_words]

# lemmatization
lemmas = [lemmatizer.lemmatize(word) for word in filtered_words]

print("Original Words:", filtered_words)
print("Porter Stemmer:", porter_stem)
print("Lancaster Stemmer:", lancaster_stem)
print("Lemmatized Words:", lemmas)


#Quesiton 3:
import re

# a. Words with more than 5 letters
big_words = re.findall(r'\b\w{6,}\b', para)

# b. Numbers
numbers = re.findall(r'\b\d+\b', para)

# c. Capitalized words
cap_words = re.findall(r'\b[A-Z][a-z]*\b', para)

# splitting
only_alpha = re.findall(r'\b[a-zA-Z]+\b', para)

# words starting with vowel
vowel_words = [w for w in only_alpha if w[0].lower() in 'aeiou']

print("Words >5 letters:", big_words)
print("Numbers in text:", numbers)
print("Capitalized words:", cap_words)
print("Only alphabetic words:", only_alpha)
print("Words starting with vowel:", vowel_words)


#Question 4:
# custom tokenizer
def custom_tokenize(text):
    # keep hyphens and apostrophes
    text = re.sub(r'[^\w\s\'\-\.]', '', text)
    tokens = re.findall(r"\d+\.\d+|\w+(?:-\w+)*|'\w+", text)
    return tokens

tokens = custom_tokenize(para)

# regex cleaning
def clean_text(text):
    text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', '<EMAIL>', text)
    text = re.sub(r'https?://\S+|www\.\S+', '<URL>', text)
    text = re.sub(r'\+?\d[\d\s\-]{8,}\d', '<PHONE>', text)
    return text

cleaned = clean_text(para)

print("Custom Tokens:", tokens)
print("Cleaned Text:", cleaned)

