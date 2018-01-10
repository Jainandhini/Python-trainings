"""
Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example """

print("a string that you \"dont\'t\" have to escape");
print("This\nis a ........ multi-line\nheredoc string -------> example");

#the ques actually means to have the sample string as doc i.e desc for a function so rewrite solution as

def jai():
    """a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

print(jai.__doc__)