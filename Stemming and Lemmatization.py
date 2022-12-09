print('Stemming and Lemmatization:')
print('--------------------------------------------------------------')
print('1- Stemming: we start with Stemming:')
print('the Stemming is only available in nltk, because spacy-library doesn\'t support it.')
print('--------------------------------------------------------------')
print('''Comparison between the variants of Stemming's tool in nltk-library:
PorterStemmer(p_stemmer), SnowballStemmer(s_stemmer) and LancasterStemmer(l_stemmer: ''')
words = ['run','runner','running','ran','runs','easily','fairly',"is","was","be","been","are","were"]
import nltk
p_stemmer=nltk.stem.porter.PorterStemmer()
s_stemmer= nltk.stem.snowball.SnowballStemmer(language='english')
l_stemmer = nltk.stem.LancasterStemmer()
print('_________________________________________________________________________')
print('-------------------------------------------------------------------------')
print('|| Word         || PorterStemmer    || SnowballStemmer|| LancasterStemmer|| ')
print('--------------------------------------------------------------------------------')
for word in words:
    print('|| %-12s || %-16s || %-15s|| %-16s||'%(word,p_stemmer.stem(word),s_stemmer.stem(word),l_stemmer.stem(word)))
print('_________________________________________________________________________')
print('-------------------------------------------------------------------------')
print(' ')
print('---------------------------------------------------------------')
print('2-Lemmatization:')
print('a- we start with spacy-library: ')
import spacy
nlp = spacy.load('en_core_web_sm')
def show_lemmas(text):
    print('________________________________________________________________________________')
    print('--------------------------------------------------------------------------------')
    print('|| Word         || POS              || POS-ID              || Lemmatization   || ')
    print('--------------------------------------------------------------------------------')
    for token in text:
        print('|| %-12s || %-16s || %-20s|| %-16s||' % (token.text, token.pos_, token.lemma, token.lemma_))
    print('________________________________________________________________________________')
    print('--------------------------------------------------------------------------------')

doc2 = nlp(u"I saw eighteen mice today!")
show_lemmas(doc2)

print('b-Limmatization with nltk-library with the tool WordNetLemmatizer()')
lemmatizer = nltk.stem.WordNetLemmatizer()
words = ["cats","cacti","radii","feet","speech",'runner']
def lemmatization(words):
    print('______________________________________')
    print('--------------------------------------')
    print('|| Word         || POS              ||')
    print('--------------------------------------')
    for word in words :
        print('|| %-12s || %-16s ||' %(word,lemmatizer.lemmatize(word)))
    print('______________________________________')
    print('--------------------------------------')
lemmatization(words)
print('lemmatization has better performance when it given if the word noun or verb (pos= \'n\' or \'v\'):')
print('the noun meeting has the lemmatization: ',lemmatizer.lemmatize("meeting", pos="n"))
print('the verb meeting has the lemmatization: ',lemmatizer.lemmatize("meeting",'v'))