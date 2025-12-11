import nltk
from nltk.stem import PorterStemmer

nltk.data.path.append('/Users/pavanvenugopal/nltk_data')  # classic resources

txt = "I unleashed a V12 monster engine that roars to 9500 RPM and it is called BMW"

# cursed abandoned tokenization
tok = nltk.data.load('tokenizers/punkt/english.pickle')
tokens = [w for s in tok.tokenize(txt) for w in nltk.word_tokenize(s)]

# classic perceptron tagger
tagger = nltk.data.load('taggers/averaged_perceptron_tagger/english.pickle')
tagged = tagger.tag(tokens)

# cursed abandoned dark methods
filt = [w for w,p in tagged if p not in ('IN','DT','CC','TO','UH')]
stems = [PorterStemmer().stem(w) for w in filt]
chunks = nltk.chunk.ne_chunk(tagged)
ner = nltk.chunk.ne_chunk(tagged)

# outputs
print("TOKENS:  ", tokens)
print("FILTERED:", filt)
print("STEMS:   ", stems)
print("POS:     ", tagged)
print("CHUNKS:  ", chunks)
print("NER:     ", ner)
