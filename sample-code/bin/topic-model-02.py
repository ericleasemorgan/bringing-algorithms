#!/usr/bin/env python

# lda-list.py - given directory (with files of a particular shape) and two integers, output LDA "topics"

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
#import mglearn
import numpy as np
import os
import sys

# sanity check
if len( sys.argv ) != 4 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <directory> <integer> <integer>\n" )
	quit()

# get input
directory  = sys.argv[ 1 ]
components = int( sys.argv[ 2 ] )
dimensions = int( sys.argv[ 3 ] )

data = []
for file in os.listdir( directory ) :
	if file.endswith( '.txt' ) : 
		data.append( open( directory + '/' + file ).read() )
		
vectorizer = CountVectorizer( stop_words='english', min_df=4 )
X          = vectorizer.fit_transform( data )
lda        = LatentDirichletAllocation( n_components=components, learning_method="batch", max_iter=50, random_state=0 )
topics     = lda.fit_transform( X )
sorting    = np.argsort( lda.components_, axis=1)[ :, ::-1 ]
names      = np.array( vectorizer.get_feature_names() )

for topic in topics : print( topic )
exit()

for name in names : print( name )
exit()

# output and done; kewl
#mglearn.tools.print_topics( topics=range( components ), feature_names=names, sorting=sorting, topics_per_chunk=5, n_words=dimensions )
#exit()
