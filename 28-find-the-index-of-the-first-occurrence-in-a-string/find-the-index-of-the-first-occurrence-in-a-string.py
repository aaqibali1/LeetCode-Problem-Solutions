class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h_length = len(haystack)
        n_length = len(needle)

        # reducing outer loop iterations for haystack string
        # also ensuring remaining string in haystack meets needle length
        for i in range(h_length - n_length + 1):
            n_pointer = 0  # resetting n_pointer to 0 on each iteration

            while n_pointer < n_length and haystack[i + n_pointer] == needle[n_pointer]:
                n_pointer += 1
                # print(i + n_pointer)

            if n_pointer == n_length:
                return i

        return -1