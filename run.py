"""
This program generates Markov chain with cleaned text data saved in data.txt 
and priints the output to screen
"""
from markov_chain.cc_markov import MarkovChain

DATAFILENAME= "data.txt"
mc = MarkovChain()
mc.add_file(DATAFILENAME)
print mc.generate_text()
