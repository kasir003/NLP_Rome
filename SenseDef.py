from lxml import etree
from collections import Counter
import nltk

class SenseDef(object):
    def __init__(self):
        self.data=[]


    def generatemeaning(self,feature_all_cluster):
        topfeatures_withcounts=[]
        words=[]
        taggedwords=[]
        out=[]
        value = 1
        for x in range(len(feature_all_cluster)):
            topfeatures_withcounts.append(Counter(feature_all_cluster[x]).most_common(4))
        print (topfeatures_withcounts)

        for list in topfeatures_withcounts:
            for item in list:
                words.append(item[0])

        
        return words

    def generateexample(self,clusterinfo,data):
        content=[]
        sense=1
        for a in range(len(clusterinfo)):
            if (clusterinfo[a]==sense):
                content.append(data[a])
                sense=sense+1
        return content

    def writeexampleandmeaning(self,word,content,words):
        filename = word+"-"+"definition.txt"
        
        newfile = open(filename,'w')
        newfile.write('Definition and Examples for %s' % (word))

        start=0
        end=4
        for x in range(len(content)):
            newfile.write('\n')
            newfile.write('Example is :')
            newfile.write('\n')
            newfile.write(content[x].decode('utf-8')[10:-11])
            newfile.write('\n')
            newfile.write('Definition is:')
            newfile.write(str(words[start:end]))
            newfile.write('\n')
            start+=4
            end+=4


    def writeconflateExampleandMeaning(self,word1,word2,content,words):
        filename=word1+"-"+word2+"-"+"definition.txt"

        newfile = open(filename,'w')
        newfile.write('Definition and Examples for words %s and %s'%(word1,word2))
        
        start=0
        end=4
        for x in range(len(content)):
            newfile.write('\n')
            newfile.write('Example is :')
            newfile.write('\n')
            newfile.write(content[x].decode('utf-8')[10:-11])
            newfile.write('\n')
            newfile.write('Definition is:')
            newfile.write(str(words[start:end]))
            newfile.write('\n')
            start+=4
            end+=4        
        
