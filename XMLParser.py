# This program parses the input file , filters the senteces removing punctuations
# and stopwords and then clusters the sentences and outputs feature words,
# which are then used by SenseDef.py for generating meaning and examples.
# We maintain a list of yet to be clustered sentences. And the idea behind
# the baseline system is to pick the first yet to be clustered sentence and
# then find feature words around the target word in that sentences and then
# look for those feature words in a larger domain of words around the target
# words in all other sentences and cluster them in the same cluster. Then it
# also add the feature words for all those sentences clustered and again looks
# in all the remaining sentences for all these words and tries to add more
# sentences into this cluster already created. It will keep on doing that
# till it reaches a stage where there are a very few remaining sentences with
# no matching feature words. Then it clusters all those into 1 cluster. This
# is the baseline idea, we have to improve on this in the next stage.

# Import nltk, stopwords from nltk, etree used for parsing
import nltk
from nltk.corpus import stopwords
from lxml import etree

# Class definition
class XMLParser(object):

        # Constructor
        def __init__(self):
                self.data =[]

        #
        def isalfa(self,w):
                return w.replace('_','').isalpha()

        # 
        def parse(self,path,keyword):

                t,data=self.parsegeneral(path)
                # finding target word from file name
                target_word = str(keyword)

                return target_word,t,data
        
        def parseConflate(self,path,keyword1,keyword2):

                t,data=self.parsegeneral(path)

                target_word = keyword1[0:1]+'_'+keyword2[0:1]
                return target_word,t,data
        # 
        def parsegeneral(self,path):
                
                parser = etree.XMLParser(recover=True)
                tree=etree.parse(path,parser=parser)
                root = tree.getroot()
                child = root.findall('.//context')
                data =[]
                for index in range(len(child)):
                                data += etree.tostringlist(child[index],encoding="us-ascii",method="xml")


		# removing context tags form beginning and end
		# and tokenizing the sentences into words from
		# which the stop words and punctuations
		# will be remove later.
                t=[]
                for x in range(len(data)):
                                s=str(data[x])
                                s=s[13:len(s)-16]
                                t.append(nltk.word_tokenize(s))

                # removing stop words and punctuation from the
                # words in the sentences
                stop=set(stopwords.words('english'))
                stop.update(['head','Mr','I','In','Mrs','A','So','To','us','He','And','Yes'])  
                for x in range(len(t)):
                        # removing stop words
                        t[x]=[word for word in t[x] if word not in stop]
                        # removing not alphabet words i.e punctuations etc.
                        t[x]=[word for word in t[x] if self.isalfa(word)]

                return t,data


                
                        
                
    




        
                
        

