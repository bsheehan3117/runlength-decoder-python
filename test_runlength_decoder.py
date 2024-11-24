'''
    CS5001
    Spring 2023
    HW4

    Brendan Sheehan

    This program tests the decode function
'''

from runlength_decoder import decode

def test_decode(list, expected):

    '''Function test_decode

    Parameters:
    list with strings to be decoded in even positions and their
    occurrence in the run as a digit in odd positions.
    expected output
    return: nothing, print inputs & actual vs expected.

    Examples:
    Input: ['T', 5, 'P' 3, 'R' 5] Output: [T,T,T,T,T,P,P,P,R,R,R,R,R]
    Input: ['@', 2, '*', 5] Output: [@,@,*,*,*,*,*]
    Input: ['&', 7, 'y', 3, 'E', 2] Output: [&,&,&,&,&,&,&,y,y,y,E,E]
    Input: ['X', 3, 'y', 4, 'e', 0] Output: ['X', 'X', 'X', 'y', 'y', 'y', 'y']
    Input: [w, 3, 'r', 4] Output: ['w', 'w', 'w', 'r', 'r', 'r', 'r']
    '''
    actual = decode(list)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)
    
def main():

    # test 1
    test_decode(['T', 5, 'P', 3, 'R', 5], ['T', 'T', 'T', 'T', 'T',
                                           'P', 'P', 'P', 'R', 'R', 'R', 'R', 'R'])

    # test 2
    test_decode(['@', 2, '*', 5], ['@', '@', '*', '*', '*', '*', '*'])

    # test 3
    test_decode(['&', 7, 'y', 3, 'E', 2], ['&', '&', '&', '&', '&',
                                           '&', '&', 'y', 'y', 'y', 'E', 'E'])

    # test 4
    test_decode(['X', 3, 'y', 4, 'e', 0], ['X', 'X', 'X', 'y', 'y', 'y', 'y'])

    # test 5
    test_decode(['w', 3, 'r', 4], ['w', 'w', 'w', 'r', 'r', 'r', 'r'])


if __name__ == "__main__":
    main()    
