from hw4data import DATA0
from hw4data import DATA1
from hw4data import DATA2
from hw4data import DATA3
from hw4data import DATA4
from hw4data import DATA5

'''
    CS5001
    Spring 2023
    HW4
    
    Brendan Sheehan

    This is a function to decode a Run-Length Encoding
    list.
'''

'''
    Examples:
    Input: ['T', 5, 'P' 3, 'R' 5] Output: [T,T,T,T,T,P,P,P,R,R,R,R,R]
    Input: ['@', 2, '*', 5] Output: [@,@,*,*,*,*,*]
    Input: ['&', 7, 'y', 3, 'E', 2] Output: [&,&,&,&,&,&,&,y,y,y,E,E]
'''


def decode(list):

    '''Function: decode
    Decodes a run-length encoding list.
    Parameters:
    list with strings to be decoded in even positions and their
    occurrence in the run as a digit in odd positions.
    Returns: a decoded list of strings
    '''
    # assigns decoded data to an empty string
    decoded_data = " "

    # if list is not empty, loop retrieves a character at i &
    # digit at i + 1, multiplies them and assigns them to
    # the decoded_data variable
    
    if list != " ":

        for i in range(0, len(list), 2):
            letter = list[i]
            digit = int(list[i + 1])
            decoded_data = decoded_data + letter * digit
            
    # converts decoded_data returned as a string into a list
    # by filling in each letter/character
    
    list_fill = [ ]
    for letter in decoded_data:
        list_fill.append(letter)

    # removes empty string at index position 0
    list_fill.pop(0)

    return list_fill
