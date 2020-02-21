'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #Base Case: has to have more than 2 letters otherwise
    if len(word) < 2:
        return 0

    #Check for th in the first 2 letters
    elif word[0:2] == "th":
        #Recursive call for slicing letters off the word while counting each time of "th" 
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])

print(count_th("abcthxyz"))