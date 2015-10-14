#  Author : Vamsidhar Kasireddy
#  Team: Rome 
# 
# This File Generates definition of different senses of the word, writes the word, its sense and an example to a text file 
# The text file will be of name "word-definition.txt" if the file is POS file  
# The text file will be of name "word1-word2-definition.txt" if the file is name conflate file
#
# Input:
# The input for the functions in this file are Feature set, Cluster information, Data, words of Pos file or Name conflate file
#
# Feature Set : It contains all the feature words of each cluster, example :  {always,asks,emma}
#   
# Cluster Information : This dictionary contains information about clusters which contains its instances,  example : { 1:1,1:2} key is the instance and values is the sense cluster
#
# Data : This list contains the text of instances
#
# Words : words for which definition should be defined, example : believe
#
# Output :
# The output will be of format
#                       The definition and examples of the word is :
#                       Instance which is the example of the word
#                       Defintion of the word 
# Example :
# Definition and Examples for words priest and heaven
# Example is :
# at the valley of Shaveh, which is the king's dale. 14:18 And Melchizedek king of Salem brought forth bread and wine: and he was the <head>p_h</head> of the most high God.  14:19 And he blessed him, and said, Blessed be Abram of the most high God, possessor of heaven and earth: 

# Definition is:['unto', 'God', 'said', 'LORD']

# Example is :
# his seed after him. 29:1 And this is the thing that thou shalt do unto them to hallow them, to minister unto me in the <head>p_h</head> office: Take one young bullock, and two rams without blemish, 29:2 And unleavened bread, and cakes unleavened tempered with oil, and wafers unleavened anointed with

# Definition is:['shall', 'upon', 'LORD', 'offering']
#
#
#
# Importing counter function from collection for counting the frequency of words in feature set 
from collections import Counter

class SenseDef(object):
    #Defining Constructor
    def __init__(self):
        self.data=[]

# This function generates meaning based on frequency of words in feature set
# INput parameter is feature set 
    def generatemeaning(self,feature_all_cluster):
        #defining a list of lists to store the frequency of words
        topfeatures_withcounts=[]
        #defining list to store the words from feature set
        words=[]
        #Loop to store feature set words with frequency
        for x in range(len(feature_all_cluster)):
            topfeatures_withcounts.append(Counter(feature_all_cluster[x]).most_common(4))
#Loop to store most common words 
        for list in topfeatures_withcounts:
            for item in list:
                words.append(item[0])

        
        return words
# This function extracts the instance for each sense in the output
    def generateexample(self,clusterinfo,data):
        #to store the instance 
        content=[]
        # to look for all the senses 
        sense=1
        for a in range(len(clusterinfo)):
            if (clusterinfo[a]==sense):
                content.append(data[a])
                sense=sense+1
        return content
# This function writes example and definition of the POS file
    def writeexampleandmeaning(self,word,content,words):
        filename = "./Output/"+word+"-"+"definition.txt"
        #creating a new file with name "word-definition.txt"
        newfile = open(filename,'w')
        newfile.write('Definition and Examples for %s' % (word))
        self.contentWrite(content,words,newfile)

# This function writes example and defintion of the Name conflate file
    def writeconflateExampleandMeaning(self,word1,word2,content,words):
        filename="./Output"+word1+"-"+word2+"-"+"definition.txt"
        #creating a new file  to store definition for name conflate words
        newfile = open(filename,'w')
        newfile.write('Definition and Examples for words %s and %s'%(word1,word2))
        self.contentWrite(content,words,newfile)
# Writes definition example to the text file         
    def contentWrite(self,content,words,newfile):
        start=0
        end=4
        #Writes in the content to output text file 
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


        
