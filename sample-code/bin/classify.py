#!/usr/bin/env python

# classify.py - given a previously saved classification model, classify a set of documents


# require
import glob, os, pickle, sys

# sanity check
if len( sys.argv ) != 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <model> <directory>\n" )
	quit()

# get input
model     = sys.argv[ 1 ]
directory = sys.argv[ 2 ]

# load the model
with open( model, 'rb' ) as handle : ( vectorizer, classifier ) = pickle.load( handle )

# process each unclassified (.txt) file
for file in glob.glob( directory + "/*.txt" ) :
	
	# open, read, and classify a document
	with open( file, 'r' ) as handle : classification = classifier.predict( vectorizer.transform( [ handle.read() ] ) )
	
	# output
	print( "\t".join( ( classification[ 0 ], os.path.basename( file ) ) ) )
	
# done
exit()






