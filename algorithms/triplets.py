class Solution:
    def get_triplets(self, s):
        """
        Input: 1 array. s (array)
        Output: maxtrix: len(output) == N and len(output[0]) == 3.
            (whatever output[n][0] + output[n][1] + output[n][2] = 0)
        Constrains: 
            - s -> array well formated
            - s -> array of numbers
        Edge Cases:
            - not found any element with the condition in the array
            - len(s) < 3

        The first solution that came to my mind was a O(n^3) but after
        the first iteration I realiced the following solution:

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        s.sort()
        self.solution = []

        for key, val in enumerate(s):
            left = key + 1
            right = len(s) - 1

            while(left < right):
                left, right = self.next_value(left, right, val, s)

        return self.solution

    def next_value(self, left, right, val, s):
        """
        Helper function to get the next value
        """
        if val + s[left] + s[right] == 0:
            self.solution.append([val, s[left], s[right]])

            return left + 1, right - 1
        elif val + s[left] + s[right] < 0:
            return left + 1, right
        else:
            return left, right - 1


if __name__ == '__main__':
    S = [-4, -2, -1, 0, 1, 3, 4]
    solution = [[-4, 1, 3], [-4, 0, 4], [-2, -1, 3], [-1, 0, 1]]
    solution.sort()

    case1 = Solution().get_triplets(S)

    print(
        '''
        Should be equals: {}

        Expected:
        {}
        Output:
        {}

        *more tests and edge cases in tests
        Run:
            python -m algorithms.triplets_tests -v
        '''.format(
            solution == case1,
            solution,
            case1,
        )
    )
