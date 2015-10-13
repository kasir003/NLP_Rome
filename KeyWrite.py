#Author: Preethi Chimerla
#Team : Rome
# This Program generates keyfiles for input.xml( Initial File which is given as input for xml Parser)
# and
# output.xml( which is the output file generated from our program)files.

# imports etree component from lxml to parse the input data
from lxml import etree


class KeyWrite(object):
    def __init__(self):
        self.data=[]
    
    # Generates key file for input POS file
    def writekey(self,path,word):
        #creating an object for further parsing
        parser = etree.XMLParser(recover=True)
        #reads in the parsed xml
        tree=etree.parse(path,parser=parser)
        #identifies root which is main node
        root = tree.getroot()
        #instatiating a new empty string
        newWord=""
        #creates a new input.key file with the parseddata
        keyfile = open('inputkey.key','w')
        # Gives output in the format of word word.instancenumber word.senseid
        # for example if the word is God it gives the output as God God.1 God.1
        for answer in root.iter('answer'):
            newWord=word+" "+word+"."+answer.attrib['instance']+" "+word+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)
        #closing the gernerated keyfile
        keyfile.close()

    # Generates key file for input nameconflate pair file
    # takes two words as arguements
    def writeConflatekey(self,path,word1,word2):
        #creating an object for further parsing
        parser = etree.XMLParser(recover=True
        #reads in the parsed xml)
        tree=etree.parse(path,parser=parser)
        #identifies root which is main node
        root=tree.getroot()
        #instatiating a new empty string
        newWord=""
        #creates a new input.key file with the parseddata
        keyfile = open('inputkey.key','w')
        # Gives output in the format of word word.instancenumber word.senseid
        # for example if the words are women and friend it gives ouput as w_f w_f.1 w_f.2
        for answer in root.iter('answer'):
            newWord = word1[0:1]+"_"+word2[0:1]+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['instance']+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)
        #closing the gernerated keyfile
        keyfile.close()

    # Generates Key file for output POS file
    def writeOutputKey(self,path,word):
        #creating an object for further parsing
        parser = etree.XMLParser(recover = True)
        #reads in the parsed xml
        tree = etree.parse(path,parser=parser)
        #identifies root which is main node
        root = tree.getroot()
        #instatiating a new empty string
        newWord=""
        #creates a new input.key file with the parseddata
        keyfile = open('outputkey.key','w')
        # Gives output in the format of word word.instancenumber word.senseid
        # for example if the word is God it gives the output as manner manner.1 manner.2
        for answer in root.iter('answer'):
            newWord = word+" "+word+"."+answer.attrib['instance']+" "+word+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)
        #closing the gernerated keyfile
        keyfile.close()

    # Generates Key file for output nameconflate pair file
    # takes two words as arguements
    def writeOutputConflateKey(self,path,word1,word2):
        #creating an object for further parsing
        parser = etree.XMLParser(recover = True)
        #reads in the parsed xml
        tree = etree.parse(path,parser = parser)
        #identifies root which is main node
        root = tree.getroot()
        #instatiating a new empty string
        newWord=""
        #creates a new input.key file with the parseddata
        keyfile = open('outputkey.key','w')
        # Gives output in the format of word word.instancenumber word.senseid
        # for example if the words are whale and night it gives ouput as w_n w_n.1 w_n.2
        for answer in root.iter('answer'):
            newWord = word1[0:1]+"_"+word2[0:1]+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['instance']+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)

        keyfile.close()
                
        
        
