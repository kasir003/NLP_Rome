import getopt, sys
from XMLParser import XMLParser
from XMLWrite import XMLWrite
from KeyWrite import KeyWrite
from SenseDef import SenseDef
import argparse

def main():
        #Reading the arguments from the command line
        parser = argparse.ArgumentParser(description='process some xml file')
        parser.add_argument("-i","--pos", dest="posfile",help="read data from FIlENAME")
        parser.add_argument("-n","--conflate",dest="conflatefile")
        parser.add_argument("-o","--output",dest="outputfile")
        parser.add_argument("-k1","--keyword1",dest="keyword1")
        parser.add_argument("-k2","--keyword2",dest="keyword2")
        args = parser.parse_args()
        if not((args.posfile) or (args.outputfile) or (args.keyword1)) or not((args.conflatefile)or(args.outputfile)or(args.keyword1)or(args.keyword2)):
                parser.error("incorrect number of arguments")
        if args.posfile:
                xmlParse = XMLParser()
                target_word,t,data= xmlParse.parse(args.posfile,args.keyword1)
                cluster,all_features = xmlParse.cluster(target_word,t)
                xmlWrite = XMLWrite()
                xmlWrite.write(args.posfile,cluster,args.outputfile)
                keyWrite = KeyWrite()
                keyWrite.writekey(args.posfile,args.keyword1)
                keyWrite.writeOutputKey(args.outputfile,args.keyword1)
                sensedef = SenseDef()
                words = sensedef.generatemeaning(all_features)
                content = sensedef.generateexample(cluster,data)
                sensedef.writeexampleandmeaning(args.keyword1,content,words)
        if args.conflatefile:
                xmlParse=XMLParser()
                target_word,t,data=xmlParse.parseConflate(args.conflatefile,args.keyword1,args.keyword2)
                cluster,all_features = xmlParse.cluster(target_word,t)
                xmlWrite = XMLWrite()
                xmlWrite.write(args.conflatefile,cluster,args.outputfile)
                keyWrite = KeyWrite()
                keyWrite.writeConflatekey(args.conflatefile,args.keyword1,args.keyword2)
                keyWrite.writeOutputConflateKey(args.outputfile,args.keyword1,args.keyword2)
                sensedef = SenseDef()
                words = sensedef.generatemeaning(all_features)
                content = sensedef.generateexample(cluster,data)
                sensedef.writeconflateExampleandMeaning(args.keyword1,args.keyword2,content,words)

                
        
#The main function is called 
if __name__ == "__main__":
        main()
                
