# Author : Vamsidhar Kasireddy
# Team : Rome 
#
# This script contains the main function which will invoke all other scripts of the project 
# The input would either be a POS file or name conflate , output file name and location, words for which sense and clusters need to be find
# There are multiple options in provided to differentiate the command line arguments
# -i or --pos option specifies the argument is the location of the POS file
# -n or --conflate option specifies the argument is the location of name conflate file
# -o or --output option specifies the argument is the name and location of output file
# -k1 or --keyword1 option specifies that argument is the keyword of POS file or first keyword of name conflate file
# -k2 or --keyword2 option specifies that argument is the second keyword of nameconflate file
# The input options will change based on the input file
#
# If the input is a POS file then command line input would be of below format 
# python3 main.py -i posfile -o outputfile -k1 keyword1
# 
# If the input is name conflate file then command line input would be of below format 
# pythone3 main.py -n conflatefile -o outputfile -k1 keyword1 -k2 keyword2
#
# 
#
#
#
#
#
#
#
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
        # validating the number of command line arguments 
        if not((args.posfile) or (args.outputfile) or (args.keyword1)) or not((args.conflatefile)or(args.outputfile)or(args.keyword1)or(args.keyword2)):
                parser.error("incorrect number of arguments")
        #if the arguments specify pos file then the following functions are executed and output is generated
        if args.posfile:
                #creating XMLParser class object
                xmlParse = XMLParser()
                #retrieving the word which need to be processed list containing the context 
                target_word,t,data= xmlParse.parse(args.posfile,args.keyword1)
                #cluster information and feature set are retrieved
                cluster,all_features = xmlParse.cluster(target_word,t)
                xmlWrite = XMLWrite()
                # generating the output xml file
                xmlWrite.write(args.posfile,cluster,args.outputfile)
                keyWrite = KeyWrite()
                # generating input and output key files
                keyWrite.writekey(args.posfile,args.keyword1)
                keyWrite.writeOutputKey(args.outputfile,args.keyword1)
                sensedef = SenseDef()
                #generating the sense and example text document
                words = sensedef.generatemeaning(all_features)
                content = sensedef.generateexample(cluster,data)
                sensedef.writeexampleandmeaning(args.keyword1,content,words)
        #if the arguments specify name conflate file then the following functions are executed and output is generated       
        if args.conflatefile:
                xmlParse=XMLParser()
                #retrieving the conflated word and list with context
                target_word,t,data=xmlParse.parseConflate(args.conflatefile,args.keyword1,args.keyword2)
                #cluster information and feature set are retrieved
                cluster,all_features = xmlParse.cluster(target_word,t)
                xmlWrite = XMLWrite()
                #generating output xml file
                xmlWrite.write(args.conflatefile,cluster,args.outputfile)
                keyWrite = KeyWrite()
                #generating output and input keys
                keyWrite.writeConflatekey(args.conflatefile,args.keyword1,args.keyword2)
                keyWrite.writeOutputConflateKey(args.outputfile,args.keyword1,args.keyword2)
                sensedef = SenseDef()
                #generating the sense and example text document
                words = sensedef.generatemeaning(all_features)
                content = sensedef.generateexample(cluster,data)
                sensedef.writeconflateExampleandMeaning(args.keyword1,args.keyword2,content,words)

                
        
#The main function is called 
if __name__ == "__main__":
        main()
                
