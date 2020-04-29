"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        output = []
        gap = (numRows - 1) * 2

        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                tmp = i
                while True:
                    output.append(s[tmp])
                    tmp += gap
                    if tmp >= len(s):
                        break
            else:
                tmp = i
                sub_gap = 2 * (numRows - i - 1)
                while True:
                    output.append(s[tmp])
                    sub_tmp = tmp
                    sub_tmp += sub_gap
                    if sub_tmp < len(s):
                        output.append(s[sub_tmp])
                    tmp += gap
                    if tmp >= len(s):
                        break

        return ''.join(output)

def main():
    s = Solution()
    # print(s.convert("PAYPALISHIRING",3))
    print(s.convert("AB",1))
    print(s.convert("AB", 2))
    for i in range(1, len('PAYPALISHIRING')+1):
        print(s.convert("PAYPALISHIRING",i))

class SolutionOther(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
    main()

# a better solution
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        # This is a vague sentence for python beginers
        L = [''] * numRows
        # it can be replaced by the following:
        # L = []
        # for i in range(0, numRows):
        #     L.append('')
        # so if numRows = 3, L = ['', '', '']
        index, step = 0, 1

        for x in s:
            L[index] += x
            #@1 start #
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            #@1 end  #
            # I like to explain the part above
            # take the str "PAYPALISHIRING" for example:
            # We start with variable index with the value 0, step with the value 1
            # Each row added with the next char
            # If we reach the bottommost row, we need to turn to the next above row, so we change the step value to -1
            # we keep the step value until we reach topmost row. DON'T CHANGE IT!
            # Again, if we reach the topmost row, we need to reset the step value to 1
            # What we need to remember is:
            # the zigzag pattern is just a pictorial image for us to have a better understanding
            # What the trick of algorithm is actually add the next char of the given string to different rows.
            # Don't really think how to move the cursor in the matrix.
            # It's really misleading way you think of this. Even it works, it's not efficient.
            index += step

        return ''.join(L)
