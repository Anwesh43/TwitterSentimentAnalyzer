import nltk

def pos_tag_words(sentence):
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    return tagged_words
def filter_nouns(sentence):
    tagged_words = pos_tag_words(sentence)
    def noun_checker(word_set):
        a,b = word_set
        return not(b == 'NNP' or b == 'NN')
    return filter(noun_checker,tagged_words)
def get_words_without_nouns(sentence):
    def remove_tags(word_set):
        a,b = word_set
        return a
    tags_without_pn = filter_nouns(sentence)
    return map(remove_tags,tags_without_pn)
def get_sentence_without_nouns(sentence):
    return ' '.join(get_words_without_nouns(sentence))
print get_sentence_without_nouns('Da Vinci Code book is just awesome')
