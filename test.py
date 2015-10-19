from mnistparser import MNISTParser, MNISTElement

# To set up a parser, call the constructor with the label filename and the images filename
parser = MNISTParser('../train-labels.idx1-ubyte','../train-images.idx3-ubyte')
# The parser is an iterator. A call to "next()" will return the next MNISTElement
element = parser.next()
# Each element has a label (the digit in the sample) and an array containing each of the
# pixel values (in the range [0,255]). It's an array of length 28*28 or 784 for each image.
print element.label
print element.image

# Since the MNISTParser object is an iterator, you can also use it in a for loop
count = 0
for element in parser:
    # Since there are 60000 samples, we'll just count them instead of trying to print
    # each one.
    count += 1
# This example should print 59999, since we've already called "next()" on this parser once
# in the previous example.
print "The number of samples is: " + str(count)
