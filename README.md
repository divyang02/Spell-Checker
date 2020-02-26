# Spell-Checker
## Pre requisite -
	1. Python 3.6+
	2. Intall tkinter by the command - pip install tkinter
	3. Place the dictionary.txt in the same folder as the other files

## Algorithm used -
	1. Firstly, the dictionary.txt is parsed into python dictionary
	2. A trie is created for the words present in dictionary to facilitate fast look-up
	3. Edit distance is the distance measure used to calculate the relevance score between two words. 
	4. Edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other. The operations can be Insertion, Deletion or Replacement of a character.
	5. When a string is present in the dictionary, its meaning is returned
	6. Whenever a word is not present in dictionary, we need to calculate edit distance of word entered with all the words present in dictionary which is time consuming.
	7. To solve this problem, we see that whenever we calculate edit distance (by dynamic programming) we create a matrix. For eg. if we want to create edit distance matrix for "cat" and "kate" it will be of size 3*4, and now if we want to create a edit distance matrix for "cats" and "kate" it will be of size 4*4 but we only need to calculate the last row of this matrix as the submatrix of size 3*4 will be common and we must have calculated it before when we encounter it in trie.
	8. The Next suggestion feature is also added, that is, when we press Search it will give 3 most probable prediction and when we hit Next suggestion, the next 3 most probable suggestion will come and so on. 


## Future Ideas - 
We can use the 1 billion word dataset by google and train a character-level sequence-to-sequence model with LSTM layers to convert a text with spelling errors to a correct text. Further we can add attention mechanism to make the model more robust
