# semanticchangeHansard

## Contents

semanticchangeHansard.py

Input: list of words of interest, aligned embeddings from two different epochs

Output: For each WOI, 10 most similar words in each epoch 

to run: python semanticchangeHansard.py "text file containing list of words of interest"

### Resources

oed_obsolete_occ.txt -- obsolete word, occurences in Hansard 1909-1918, occurences in Hansard 2009-2018

knownwois.txt -- list of known words of interest -- words that have been shown to have undergone semantic change from prior work

knownwois_pos.txt -- list of known words of interest with POS tags
