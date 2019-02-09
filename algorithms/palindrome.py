import re


class Solution:
    def is_palindrom(self, p):
        """
        Input: 1 string. p (string)
        Output: boolean (whatever is a palindrom or not)
        Constrains: 
            - the Input (p) is allways a string
            - case insensitive
        Edge Cases:
            - empty string is a palindrom
            - can be nubmbers inside the string
            - special characters

        Time Complexity: regular expression against a string is O(n)
        Space Complexity: N
        """
        p = re.sub(r'[^\w|0-9]', '', p)
        p = p.replace('_', '').lower()
        p = p.replace('|', '').lower()

        return p == p[::-1]


if __name__ == '__main__':
    print(
        '''
        Should not be a palindrome: {} Palindrome
        Should be a palindrome: {} Palindrome

        *more tests and edge cases in tests
        Run:
            python -m algorithms.palindrome_tests -v
        '''.format(
            Solution().is_palindrom("Hello World"),
            Solution().is_palindrom("A Toyota’s a Toyota"),
        )
    )
