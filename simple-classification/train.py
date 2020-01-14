#!/usr/bin/env python3

# train.py - given a file name and a list of directories containing .txt files, create a model for classifying similar items

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# January 11, 2020 - written for a book about machine learning in libraries


# require the libraries/modules that will do the work
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection         import train_test_split
from sklearn.naive_bayes             import MultinomialNB
import glob, os, pickle, sys

# sanity check; make sure the program has been given input
if len( sys.argv ) < 4 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <model> <directory> <another directory> [<another directory> ...]\n" )
	quit()

# get the name of the file where the model will be saved
model = sys.argv[ 1 ]

# get the rest of the input, the names of directories to process
directories = []
for i in range( 2, len( sys.argv ) ) : directories.append( sys.argv[ i ] )

# initialize the data to analyze and its associated labels
data   = []
labels = []

# loop through each given directory
for directory in directories :

	# find all the text files and get the directory's name
	files = glob.glob( directory + "/*.txt" )
	label = os.path.basename( directory )
	
	# process each file
	for file in files :
		
		# open the file
		with open( file, 'r' ) as handle :
		
			# add the contents of the file to the data
			data.append( handle.read() )
			
			# update the list of labels
			labels.append( label )

# divide the data/labels into training sets and testing sets; a best practice
data_train, data_test, labels_train, labels_test = train_test_split( data, labels )

# initialize a vectorizer, and then count/tabulate the training data
vectorizer = CountVectorizer( stop_words='english' )
data_train = vectorizer.fit_transform( data_train )

# initialize a classification model, and then use Naive Bayes to create a model
classifier = MultinomialNB()
classifier.fit( data_train, labels_train )

# count/tabulate the test data, and use the model to classify it
data_test       = vectorizer.transform( data_test )
classifications = classifier.predict( data_test )

# begin to test for accuracy
count = 0

# loop through each test classification
for i in range( len( classifications ) ) :
    
    # increment, if the calculated classification match the given classification
    if classifications[ i ] == labels_test[ i ] : count += 1

# calculate and output the accuracy score; above 75% begins to achieve success
print ( "Accuracy: %s%% \n" % ( int( ( count * 1.0 ) / len( classifications ) * 100 ) ) )

# save the vectorizer and the classifier (the model) for future use, and done
with open( model, 'wb' ) as handle : pickle.dump( ( vectorizer, classifier ), handle )
exit()
