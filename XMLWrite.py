from lxml import etree

class XMLWrite(object):
    def __init__(self):
        self.data=[]

    def write(self,path,cluster_information,output):
        parser = etree.XMLParser(recover=True)
        tree=etree.parse(path,parser=parser)
        root = tree.getroot()
        value=0
        #Updating the attributes of the xml
        #Updating the sense ids of the xml based on the clusters
        for answer in root.iter('answer'):
            answer.attrib['senseid']=str(cluster_information[value])
            value=value+1
            #Updating the xml and writing it to a new xml
        tree.write(output)
