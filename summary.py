import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text=''' In 1980, Samsung acquired the Gumi-based Hanguk Jeonja Tongsin and entered telecommunications hardware. Its early products were switchboards. The facility was developed into the telephone and fax manufacturing systems and became the center of Samsung's mobile phone manufacturing. They have produced over 800 million mobile phones to date.[21] The company grouped them together under Samsung Electronics in the 1980s. '''
stopwords=list(STOP_WORDS)

# print(stopwords)
nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
print(doc)

#tokenization
token=[token.text for token in doc]
# print(token)

#count frequency of each word store in a dictonary
word_freq={}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
            word_freq[word.text]=1
        else:
            word_freq[word.text] += 1

print(word_freq )
