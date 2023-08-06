# Given a string, return all possible substrings along with each substring's frequency/count.

"""Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
 
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 10**5
s[i] is a printable ascii character.
"""

#TODO: Fix index out of range
def reverse_a_string(s):
    a = []
    first_index = 0
    last_index = -1
    while first_index != last_index:
        a = s[first_index]
        s[first_index] = s[last_index]
        s[last_index] = a
        first_index += 1
        last_index -= 1

	# # only need to loop through half the string
    return a

reverse_a_string(['p', 'o', 'l', 'a', 'r'])