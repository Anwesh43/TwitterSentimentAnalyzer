from data_extractor import *
from nlp_util import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
class SentimentAnalyzer:
    def __init__(self):
        dataExtractor = DataExtractor('data.txt')
        msgs,self.Y = dataExtractor.parseTextFile()
        self.Y = map(int,self.Y)
        self.X_str = map(get_sentence_without_nouns,msgs)
        self.__split()
        self.__convertToVectors()

    def __convertToVectors(self):
        self.cf = CountVectorizer()
        Xdtm = self.cf.fit_transform(self.x_str_train)
        self.x_train = Xdtm.toarray()
        self.x_test = self.cf.transform(self.x_str_test)
    def __split(self):
        self.x_str_train,self.x_str_test,self.y_train,self.y_test = train_test_split(self.X_str,self.Y)
    def train(self):
        print "going to train part"
        self.nb = MultinomialNB()
        self.nb.fit(self.x_train,self.y_train)
    def test(self):
        print "test"
        correct = 0
        y_pred = self.nb.predict(self.x_test)
        for i in range(0,len(y_pred)):
            y_pr = y_pred[i]
            y_t = self.y_test[i]
            if y_pr == y_t:
                correct = correct+1
        accuracy = (correct*1.0)/len(y_pred)
        print 'accuracy is {0}'.format(accuracy)
    def predict(self,message):
        message_without_nouns = get_sentence_without_nouns(message)
        Xdtm = self.cf.transform([message])
        x_pred = Xdtm.toarray()
        y_pred = self.nb.predict(x_pred)
        print y_pred
sentimentAnalyzer = SentimentAnalyzer()
sentimentAnalyzer.train()
sentimentAnalyzer.test()
