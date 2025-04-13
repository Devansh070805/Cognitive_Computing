same paragraph as previous
I really enjoy playing esports games like Valorant, League of Legends, and CS:GO. They are super competitive and exciting, and I usually play them after classes or on weekends. I also like watching professional tournaments online because it’s fun to see how good the pros are. Sometimes I even learn new tricks or strategies by watching them. My friends and I usually play as a team, and it’s a great way to bond while having fun. I think esports are becoming more popular because people take gaming seriously now, not just for fun but even as a career.

#Question 1:
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

# original text
text = """I really enjoy playing esports games like Valorant, League of Legends, and CS:GO. They are super competitive and exciting, and I usually play them after classes or on weekends. I also like watching professional tournaments online because it’s fun to see how good the pros are. Sometimes I even learn new tricks or strategies by watching them. My friends and I usually play as a team, and it’s a great way to bond while having fun. I think esports are becoming more popular because people take gaming seriously now, not just for fun but even as a career."""

# 1. Lowercase + remove punctuation using re
clean_text = re.sub(r'[^\w\s]', '', text.lower())

# 2. Tokenize into words and sentences
words = word_tokenize(clean_text)
sentences = sent_tokenize(text)

# 3. Compare split() vs word_tokenize()
split_words = clean_text.split()
word_tokenized = word_tokenize(clean_text)

print("Using split():", split_words[:10])
print("Using word_tokenize():", word_tokenized[:10])

# 4. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [word for word in words if word not in stop_words]

# 5. Word frequency distribution
fdist = FreqDist(filtered)
fdist.plot()

#Question 2:
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

# 1. Extract words with only alphabets
alpha_words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# 2. Remove stopwords
filtered_alpha = [w for w in alpha_words if w not in stop_words]

# 3. Stemming
porter = PorterStemmer()
stems = [porter.stem(w) for w in filtered_alpha]

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(w) for w in filtered_alpha]

# 5. Compare outputs
print("Stemmed:", stems[:20])
print("Lemmatized:", lemmas[:20])

# Stemming is faster but can distort words ("playing" → "play", "strategies" → "strategi")
# Lemmatization keeps proper words and grammar ("strategies" → "strategy"), better for readable output

#Question 3:
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

texts = [
    "This phone has a great battery life.",
    "The camera quality is not that good.",
    "Amazing design and excellent performance."
]

# 1. CountVectorizer (BoW)
cv = CountVectorizer()
bow = cv.fit_transform(texts)
print("BoW Features:", cv.get_feature_names_out())
print(bow.toarray())

# 2. TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

# 3. Top 3 keywords per text
import numpy as np

feature_names = tfidf.get_feature_names_out()
for i, row in enumerate(tfidf_matrix.toarray()):
    top_indices = row.argsort()[-3:][::-1]
    top_keywords = [(feature_names[j], row[j]) for j in top_indices]
    print(f"Text {i+1} Top Keywords:", top_keywords)

#Question 4:
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

text1 = """Artificial Intelligence is used in many areas like healthcare, robotics, and data analysis. It helps machines make decisions and learn from experience."""
text2 = """Blockchain is a secure technology that records transactions in blocks. It is mostly used in cryptocurrencies and digital records."""

# Tokenization & preprocessing
tokens1 = set(re.findall(r'\b\w+\b', text1.lower()))
tokens2 = set(re.findall(r'\b\w+\b', text2.lower()))

# a. Jaccard Similarity
jaccard = len(tokens1 & tokens2) / len(tokens1 | tokens2)
print("Jaccard Similarity:", jaccard)

# b. Cosine Similarity using TF-IDF
vec = TfidfVectorizer()
tfidf_matrix = vec.fit_transform([text1, text2])
cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
print("Cosine Similarity:", cos_sim[0][0])

# c. Insight
# Cosine is better for longer texts because it considers word importance (TF-IDF)
# Jaccard is simpler and works better for short, distinct texts

#Question 5:
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reviews = [
    "The app is really useful and works smoothly.",
    "Worst update ever, full of bugs!",
    "It's okay, nothing special but not bad.",
    "I love how fast and simple the UI is!",
    "Terrible experience. Would not recommend."
]

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f"Review: {review}\nPolarity: {polarity:.2f} → {sentiment}\n")

# Word Cloud for positive reviews
positive_text = " ".join([r for r in reviews if TextBlob(r).sentiment.polarity > 0.1])
wordcloud = WordCloud(width=600, height=400, background_color='white').generate(positive_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Positive Review Word Cloud")
plt.show()


#Question 6:
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

# Training text
data = """Esports is growing rapidly around the world. Players train hard to compete at high levels. Tournaments are watched by millions online. Careers in esports include players, coaches, and streamers. Teams often have sponsors and big fanbases."""

# 1. Tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
total_words = len(tokenizer.word_index) + 1

# 2. Create sequences
input_sequences = []
tokens = tokenizer.texts_to_sequences([data])[0]
for i in range(2, len(tokens)):
    input_sequences.append(tokens[:i])

# Pad sequences
input_sequences = pad_sequences(input_sequences)

# Split input and labels
X = input_sequences[:, :-1]
y = input_sequences[:, -1]
y = np.array(y)

# 3. Build model
model = Sequential()
model.add(Embedding(total_words, 10, input_length=X.shape[1]))
model.add(LSTM(50))
model.add(Dense(total_words, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=200, verbose=0)

# Generate text
seed_text = "Esports is"
next_words = 5
for _ in range(next_words):
    token_seq = tokenizer.texts_to_sequences([seed_text])[0]
    token_seq = pad_sequences([token_seq], maxlen=X.shape[1])
    predicted = model.predict(token_seq, verbose=0).argmax()
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            seed_text += " " + word
            break

print("Generated Text:", seed_text)

