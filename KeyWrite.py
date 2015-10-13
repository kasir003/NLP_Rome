from lxml import etree

class KeyWrite(object):
    def __init__(self):
        self.data=[]

    def writekey(self,path,word):
        parser = etree.XMLParser(recover=True)
        tree=etree.parse(path,parser=parser)
        root = tree.getroot()
        newWord=""
        keyfile = open('inputkey.key','w')
        for answer in root.iter('answer'):
            newWord=word+" "+word+"."+answer.attrib['instance']+" "+word+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)

        keyfile.close()

    def writeConflatekey(self,path,word1,word2):
        parser = etree.XMLParser(recover=True)
        tree=etree.parse(path,parser=parser)
        root=tree.getroot()
        newWord=""
        keyfile = open('inputkey.key','w')
        for answer in root.iter('answer'):
            newWord = word1[0:1]+"_"+word2[0:1]+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['instance']+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)

        keyfile.close()

    def writeOutputKey(self,path,word):
        parser = etree.XMLParser(recover = True)
        tree = etree.parse(path,parser=parser)
        root = tree.getroot()
        newWord=""
        keyfile = open('outputkey.key','w')
        for answer in root.iter('answer'):
            newWord = word+" "+word+"."+answer.attrib['instance']+" "+word+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)

        keyfile.close()

    def writeOutputConflateKey(self,path,word1,word2):
        parser = etree.XMLParser(recover = True)
        tree = etree.parse(path,parser = parser)
        root = tree.getroot()
        newWord=""
        keyfile = open('outputkey.key','w')
        for answer in root.iter('answer'):
            newWord = word1[0:1]+"_"+word2[0:1]+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['instance']+" "+word1[0:1]+"_"+word2[0:1]+"."+answer.attrib['senseid']+"\n"
            keyfile.write(newWord)

        keyfile.close()
                
        
        
