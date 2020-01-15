# Simplistic classification and visualized topic models

This directory contains a set of files used to demonstrate: 1) a simplistic machine learning classification system and 2) two methods for visualizing topic models.


## Simplistic classification

This section describes the use of two Python scripts and a set of plain text files. The intent is to use these files to: 1) train/create a classification model, and 2) apply the model to a set of unclassified documents.

It is assumed you already have Python installed. You will then want to install the necessary Python libraries/modules that will do the actual work:

`pip3 install -r requirements.txt`

The directory has already been set up and configured for use. Thus you ought to be able to run the following command to create a classification model based on the contents of the alcott emerson longfellow and thoreau directories:

`python3 train.py model.bin alcott emerson longfellow thoreau`

The output is two-fold. First, the program will output an accuracy score, and the score ought to be pretty high, if not 100%. Second, a file named "model.bin" will be created in the current directory. Run the command a few times and notice how the accuracy score may change. This is do to the fact that the sample data is being divided into different training and test sets each time it is run.

Now that a model has been created, you can use it to classify other, unclassified documents. Again the directory has already been set up for doing so. To classify documents in the directory named unclassified, run:

`python3 classify.py model.bin unclassified`

Thus, the program loads the model, applies it to all the files in the given directory, and outputs a set of label/file name combinations, something like this:

	  alcott      alcott-4770.txt
	  thoreau     thoreau-34392.txt
	  alcott      alcott-26041.txt
	  emerson     emerson-12843.txt
	  longfellow  longfellow-5436.txt
	  longfellow  longfellow-2039.txt
	  alcott      alcott-163.txt
	  alcott      alcott-38049.txt
	  alcott      alcott-34920.txt
	  longfellow  longfellow-9080.txt
	  emerson     emerson-6312.txt

In other words, the program thinks the file named emerson-6312.txt has the label of "emerson", and the file named alcott-26041.txt has a label of "alcott". This is particular case, the training and classification scripts worked perfectly.

To experiment some more, try this:

   1. return all the files in the unclassified directory into their respective author directories
   2. randomly pick a few files from each author directory and put them into the unclassified directory
   3. as before, run `train.py`
   4. as before, run `classify.py`

The results ought to be very similar.

To experiment even more:

   1. obtain a set of plain text files of another author
   2. put some of the new files into a diretory with the new author's name
   3. put the balance of the new files into the unclassified directory
   4. re-run `train.py` making sure to include the name of the new author's directory
   5. as before, run `classify.py`
   
Again the results ought to be similar.

The next step is to read the contents of `train.py` and `classify.py` more closely. 


## Visualizing topic models

This section outlines how to: 1) use a program called Topic Modeling Tool to generate a list of latent themes, and 2) use two different methods to visualize the results.

Topic Modeling Tool is a GUI/desktop version of the venerable MALLET suite of tools. To get started, first download and install Topic Modeling Tool. Second, create a directory called "corpus", and copy (not move) all the .txt files from this distribution (except requirements.txt) into the newly created directory. Third create a directory called "model". Then:

   1. open Topic Modeling Tool
   2. specify "Input Dir..." to be the corpus directory
   3. specify "Output Dir..." to be the model directory
   4. specify the "Number of topics" to equal 4
   4. click "Optional Settings" and change "Number of topic words to print" to 3
   
The Optional Settings dialog ought to look something like this:

[INSERT IMAGE-01 HERE.]

To continue:

   5. click "Ok"
   6. click the "Learn Topics" button
   
The Tool will do its good work, and in less than a minute the console will look something like the following, and I have highlighted the resulting topics:

[INSERT IMAGE-02 HERE.]

At this point the topics may seem a bit confusing. While English stop words have been automatically removed, there may be other noise. To continue:

   6. optionally, use your text editor to remove things like digits, additional stop words (like thee, thy, or thou) from the corpus, as well as weird punctation such as the underscore ("_") character
   7. go to Step #5 until tired

I have removed some of the extraneous data, and now my modeling looks like this:

[INSERT IMAGE-02 HERE.]

To create the first visualization, copy &amp; paste the topics into your favorite spreadsheet application, and then use the spreadsheet to create a pie chart of the result, such as this:






Topic modeling is a unsupervised machine learning process. Given a set of documents and an integer (t), a topic modeler will identify t latent themes, where each theme is a list of words which appear relatively close to each to each other. There are many topic modeling algorithms, but LDA (Latent Dirichlet Allocation) is generally considered the best one. 

