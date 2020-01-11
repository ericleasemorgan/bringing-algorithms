# Simplistic training and classification scripts

This directory contains two Python scripts and a set of plain text files, and the intent is to use this directory's contents to: 1) train/create a classification model, and 2) apply the model to a set of unclassified documents.

It is assumed you already have Python installed. You will then want to install the necessary Python libraries/modules that will do the actual work:

> `pip3 install -r requirements.txt`
  
The directory has already been set up and configured for use. Thus you ought to be able to run the following command to create a classification model based on the contents of the alcott emerson longfellow and thoreau directories:

> `python3 train.py model.bin alcott emerson longfellow thoreau`

The output is two-fold. First, the program will output an accuracy score, and the score ought to be pretty high, if not 100%. Second, a file named "model.bin" will be created in the current directory. Run the command a few times and notice how the accuracy score may change. This is do to the fact that the sample data is being divided into different training and test sets each time it is run.

Now that a model has been created, you can use it to classify other, unclassified documents. Again the directory has already been set up for doing so. To classify documents in the directory named unclassified, run:

> `python3 classify.py model.bin unclassified`

Thus, the program loads the model, applies it to all the files in the given directory, and outputs a set of label/file name combinations, something like this:

| alcott | alcott-4770.txt |
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

In other words, the program things the file named emerson-6312.txt has the label of "emerson", and the file named alcott-26041.txt has a label of "alcott". This is particular case, the training and classification scripts worked perfectly.

To experiment some more, try this:

   1. return all the files in the unclassified directory into their respective author directories
   2. randomly pick a few files from each author directory and put them into the unclassified directory
   3. as before, run `train.py`
   4. as before, run `classify.py`

The results ought to be very similar.

To experiment even more:

   1. obtain a set of plain text files of another author
   2. put some of the new files into a diretory with the new author's name
   3. put some of the new files into the unclassified directory
   4. re-run `train.py` making sure to include name of the new author's directory
   5. as before, run `classify.py`
   
Again the results ought to be similar.

The next step is to read the contents of `train.py` and `classify.py` more closely. 

