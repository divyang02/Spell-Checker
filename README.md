# Spell-Checker
## Pre requisite -
	1. Python 3.6+
	2. Intall tkinter by the command - pip install tkinter
	3. Place the dictionary.txt in the same folder as the program

## Algorithm used -
	1. Firstly, the dictionary.txt is parsed into python dictionary
	2. Edit distance is the distance measure used to calculate the relevance score between two words. 
	3. Edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other. The operations can be Insertion, Deletion or Replacement of a character.
	4. Dynamic Programming approach is used to calculate edit distance.
	5. When a string is present in the dictionary, its meaning is returned
	6. When it is not present, whole dictionary is searched for the most probable closest word that is present in it to make suggestions

## Time Complexity Analysis -
	1. The edit distance is calculated in O(m*n) time where m and n are length of string
	2. If word is present in dictionary the meaning is returned in O(1) time
	3. If it is not present it is returned in O(L*m*n) where L is the number of words present in dictionary 

## Future Ideas - 
We can use the 1 billion word dataset by google and train a character-level sequence-to-sequence model with LSTM layers to convert a text with spelling errors to a correct text. Further we can add attention mechanism to make the model more robust
