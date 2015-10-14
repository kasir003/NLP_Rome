#Author : Nirav Sharda
#Team : Rome
# This program recieves the list_of_words in all sentences
# and then clusters the sentences and outputs feature words,which
# are then used by SenseDef.py for generating meaning and examples.
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

class ClusterSentences(object):
        # The cluster function takes in the target_word and list of lists containing words
        # of all sentences and the clusters the sentences based on the baseline idea.
        # The idea is written in the beginning of this file.
        def cluster(self,target_word,words_in_all_sentences):

                # A new empty list
                remainingsentences=[]

                # A new list for storing cluster information
                sentences=[]

                # A number for storing cluster id
                cluster_number=1

                # A new list for storing features of all clusters
                features_of_all_clusters=[]
                
                # Initialize a dictionary to store cluster information :
                cluster_information = dict()

                # Add indexes of all sentences into remaining sentences
                # Initially all sentences are remaining to be clustered
                for number in range(len(words_in_all_sentences)):
                        remainingsentences.append(number)

        
                # The sentences store the instance id of the sentence that are
		# part of the same cluster. The idea is to extract feature words i.e
		# meaningful neighbouring words in the first sentence that is yet to be 
		# clustered and find feature words in it and then look in all the remaining sentences
		# to be clustered for these words and classify them in the same cluster.
		# The loop stops when the length of sentences become 1 i.e we don't 
		# find any sentences matching that cluster. Then we classify all the remaining 
		# sentences into 1 final cluster. This is an overview of the baseline idea.
                while (len(sentences)!=1):

                        # An empty list for storing feature words for each cluster
                        # which can be used to give meaning to target-word in
                        # same cluster
                        feature=[]
                        
                        # Adding first sentence to group of sentences
                        # Sentences stores the sentences that are part of the same cluster
                        sentences=[remainingsentences[0]]

                        # Iterate two times
                        for i in range(0,2):

                                feature=self.findfeaturewords(sentences,words_in_all_sentences,target_word)

                                # The look in all remaining sentences for these feature words
                                # We are looking in the range of +- 10 words
                                # near the target word and if any words match
                                # any of the feature word then they are in the
                                # same cluster.
                                for x in range(1,len(remainingsentences)):
                                        index_of_target_word=[index for index, word in enumerate(words_in_all_sentences[remainingsentences[x]]) if word.startswith(target_word)]

                                        #Convert list to int
                                        index_of_target_word=index_of_target_word[0]

                                        # Look for feature words in +- 10 words around the target word in all remaining
                                        # sentences yet to be clustered.
                                        w=words_in_all_sentences[remainingsentences[x]][index_of_target_word-10:index_of_target_word+10]

                                        # if some matching words are found add the sentence to the current cluster
                                        if len([words for words in w if words in feature]) !=0:
                                             sentences.append(remainingsentences[x])

                        # Convert to set to remove duplicates
                        sentences=set(sentences)
                        # Convert back to list
                        sentences=list(sentences)

                        # If the number of sentences in the cluster is 1 break from the loop
                        # and cluster all the remaining sentences into 1 cluster
                        if len(sentences)==1:
                                break;

                        # When the number of sentences in the cluster is not 1 update the
                        # result in a dictionary cluster_information
                        if len(sentences)!=1:
                                for c in range(len(sentences)):
                                        # Adding to dictionary 
                                        cluster_information.update({sentences[c]:cluster_number})
                                        
                                # Adding feature of this cluster to the list features_of_all_clusters
                                features_of_all_clusters.append(feature)

                        # Update cluster number
                        cluster_number = cluster_number+1
                        
                        # Remove the sentences already clustered from these.
                        remainingsentences=[a for a in remainingsentences if a not in sentences]

                # Cluster the remaining sentences into 1 cluster, this is a baseline idea
                for x in range(len(remainingsentences)):
                        cluster_information.update({remainingsentences[x]: cluster_number})
                        
                # Adding feature words of the final cluster to the list features_of_all_clusters
                features_of_all_clusters.append(self.findfeaturewords(remainingsentences,words_in_all_sentences,target_word))

                # return cluster_information : dictionary containing clusters sentences
                # and features_of_all_clusters : a list of lists containing feature words
                # of all cluster
                return cluster_information,features_of_all_clusters

        # This function finds the feature words around the target word i.e words in the range +-
        # 4 words around the target word.
        def findfeaturewords(self,list_of_sentences,words_of_all_sentences,target_word):
                
                # A list for storing feature words
                feature=[]
                for x in range(len(list_of_sentences)):
                                        # find the index of target_word
                                        index_of_target_word=[index for index, word in enumerate(words_of_all_sentences[list_of_sentences[x]]) if word.startswith(target_word)]
                                        
                                        #convert list to int
                                        index_of_target_word = index_of_target_word[0]

                                        # Add words to the left of target word to the list feature.
                                        for y in range(index_of_target_word-4,index_of_target_word):
                                                feature.append(words_of_all_sentences[list_of_sentences[x]][y])

                                        # Add words to the right of target word to the list feature.
                                        for z in range(index_of_target_word+1,index_of_target_word+5):
                                                feature.append(words_of_all_sentences[list_of_sentences[x]][z])
                                                
                # return feature : A list containing feature words of all clusters
                return feature
