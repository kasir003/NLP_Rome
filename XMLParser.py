# Author : Vamsidhar Kasireddy
# Team : Rome 
#
# This program parses the input file , filters the senteces removing punctuations
# and stopwords and sends the information to Cluster sentences.py
# Import nltk, stopwords from nltk, etree used for parsing
#
import nltk
from nltk.corpus import stopwords
from lxml import etree

# Class definition
class XMLParser(object):

        # Constructor
        def __init__(self):
                self.data =[]

        # this function looks out if the word is alphabetic or not , returns true if the word is alphabetic and
        # false if numeric
        def isalfa(self,w):
                return w.replace('_','').isalpha()

        # This function is used to parse the POS xml file
        def parse(self,path,keyword):

                t,data=self.parsegeneral(path)
                # finding target word from file name
                target_word = str(keyword)

                return target_word,t,data
        # This function is used to parse name conflate xml file
        def parseConflate(self,path,keyword1,keyword2):

                t,data=self.parsegeneral(path)

                target_word = keyword1[0:1]+'_'+keyword2[0:1]
                return target_word,t,data
        # this function is used to parse the xml and retrieve the contents in context tag and save it to a list
        def parsegeneral(self,path):
                #creating an object parser which helps in retrieving the xml parsing when it encounters an error
                parser = etree.XMLParser(recover=True)
                tree=etree.parse(path,parser=parser)
                #saving the root node in root variable
                root = tree.getroot()
                #saving the content of context node in child list
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


                
                        
                
    




        
                
        

