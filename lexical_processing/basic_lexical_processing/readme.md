# overview

## order to read it in
- tokenisation
- stemming and lematisation
- word count
- tf-idf

## tokenisation
Basically splitting your data into words, or into sentences and so on

- to tokenise by word
```code
import nltk
from nltk.tokenize import word_tokenize
print(word_tokenize(text))
```
- to tokenise by sentence
```code
import nltk
from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))
```
- for tweets (cause tweets are made differently)
```code
from nltk.tokenize import TweetTokenizer
tknrsr = TweetTokenizer()
tknrsr.tokenize(sentence)
```
- to find ones that match a certain regex expression
```code
from nltk.tokenize import regexp_tokenize
pattern = "#[\w]+" 
regexp_tokenize(message,pattern)
```

## lematisation and stemming

This is basically just converting words to their root, so that words like apple and apples are treated the same. There are two ways to do this.

Stemming - This is when we use certain rule to convert words to their roots, mostly by removing/replacing the suffixes and prefixes in a word

```code
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# using function 1
porter = PorterStemmer()
porter_stemmed = [porter.stem(word) for word in words]
print(porter_stemmed)

# using function 2
snowball = SnowballStemmer("english")
snowball_stemmed = [snowball.stem(word) for word in words]
print(snowball_stemmed)

# porter does only for eng, snowball can do for other languages
```

Lematisation is basically like a lookup, where each word is mapped to it's root
```code 
lemma = WordNetLemmatizer()
lemmatized = [lemma.lemmatize(word) for word in words]
print(lemmatized)
```

## tf-idf and word count
These are ways to measure how important a word is in a certain sample, read the jupyter notebook for more.

## stop words
These are words like a,and that don't really carry any meaning. We must remove these before doing any analysis

```code
import nltk
from nltk.corpus import stopwords
print(stopwords.words('english'))
final_list = [word for word in string_list if word not in stopwords.words('english')]
```