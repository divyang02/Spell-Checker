from Trie import *
import heapq as hq

def search( word, maxCost, trie ):

    currentRow = range( len(word) + 1 )

    results = []

    for letter in trie.children:
        searchRecursive( trie.children[letter], letter, word, currentRow, 
            results, maxCost )
    hq.heapify(results)
    return results

def searchRecursive( node, letter, word, previousRow, results, maxCost ):

    columns = len( word ) + 1
    currentRow = [ previousRow[0] + 1 ]
    
    for column in range( 1, columns ):

        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != letter:
            replaceCost = previousRow[ column - 1 ] + 1
        else:                
            replaceCost = previousRow[ column - 1 ]

        currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    if currentRow[-1] <= maxCost and node.word != None:
        results.append( ( currentRow[-1] ,node.word) )

    if min( currentRow ) <= maxCost:
        for letter in node.children:
            searchRecursive( node.children[letter], letter, word, currentRow, 
                results, maxCost )

