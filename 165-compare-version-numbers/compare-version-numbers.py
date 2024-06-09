class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            one, two = 0, 0
            while i < len(version1) and version1[i] != '.':
                one = one*10 + int(version1[i])
                i += 1
            while j < len(version2) and version2[j] != '.':
                two = two*10 + int(version2[j])
                j += 1
            if one < two:
                return -1
            elif one > two:
                return 1
            i += 1
            j += 1
        return 0