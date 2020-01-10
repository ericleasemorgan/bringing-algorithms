#!/usr/bin/env python

# lda-visualize.py - given a directory (with files of a particular shape) and two integers, visualize LDA "topics"

# require
from sklearn.decomposition           import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import pandas as pd

# sanity check
if len( sys.argv ) != 4 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <directory> <integer> <integer>\n" )
	quit()

# get input
directory  = sys.argv[ 1 ]
components = int( sys.argv[ 2 ] )
dimensions = int( sys.argv[ 3 ] )

data    = []
keys    = []
authors = []
books   = []
for file in os.listdir( directory ) :
	if file.endswith( '.txt' ) : 
		keys.append( file )
		authors.append( file.split( '-' )[ 0 ] )
		books.append( file.split( '-' )[ 1 ] )
		data.append( open( directory + '/' + file ).read() )
		
# initialize and instantiate a vectorizer
vectorizer = CountVectorizer( stop_words='english', min_df=4 )
X = vectorizer.fit_transform( data )

# initialize and instantiate an LDA estimater
lda = LatentDirichletAllocation( n_components=components, learning_method="batch", max_iter=50, random_state=0 )
lda.fit_transform( X )

# get a list of all the words (features) in the vectorizer
features = np.array( vectorizer.get_feature_names() )

# get a list of the pointers to the features
indices = np.argsort( lda.components_, axis=1 )[ :, ::-1 ]

# create the list of topics by enumerating the features pointed to by the indices
topics = [ ' '.join( words ) for i, words in enumerate( features[ indices[ :, :dimensions ] ] ) ]

# get the scores for each sample
scores = lda.fit_transform( X )

# initialize a dataframe and fill it with content
df = pd.DataFrame()
df[ 'keys' ]    = keys
df[ 'authors' ] = authors
df[ 'books' ]   = books

# add the topics and associated scores
for i, topic in enumerate( topics ) : df[ str( i ) + ' ' + topic ] = scores[ :, i ]

# clean & organize the data frame, just for fun
df.set_index( 'keys', inplace=True )
df.sort_index( inplace=True )

table = df.pivot_table( index='authors' )
print( table )
table.plot( kind='barh', stacked=True )
plt.show()

table = df.pivot_table( index='books' )
print( table )
table.plot( kind='barh', stacked=True )
plt.show()

