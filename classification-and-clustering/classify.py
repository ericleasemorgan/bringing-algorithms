#!/usr/bin/env python3

# classify.py - given a previously saved classification model and a directory of .txt files, classify a set of documents

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# January 11, 2020 - written for a book about machine learning in libraries


# require the libraries/modules that will do the work
import glob, os, pickle, sys

# sanity check; make sure the program has been given input
if len( sys.argv ) != 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <model> <directory>\n" )
	quit()

# get input; get the model to read and the directory containing the .txt files
model     = sys.argv[ 1 ]
directory = sys.argv[ 2 ]

# read the model
with open( model, 'rb' ) as handle : ( vectorizer, classifier ) = pickle.load( handle )

# process each .txt file
for file in glob.glob( directory + "/*.txt" ) :
	
	# open, read, and classify the file
	with open( file, 'r' ) as handle : classification = classifier.predict( vectorizer.transform( [ handle.read() ] ) )
	
	# output the classification and the file's name
	print( "\t".join( ( classification[ 0 ], os.path.basename( file ) ) ) )
	
# done
exit()

