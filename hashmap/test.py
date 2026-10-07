class Solution:
    def replaceEveryCharWithLast(self, s: str) -> str:
        s_split = s.split()
        lst = []

        for word in s_split:
            word = word[-1:] + word[1:-1] + word[0:1]
            lst.append(word)

        final_string = " ".join(lst)
        return final_string

    def convertFirstCharToUpper(self, s: str) -> str:
        


sol = Solution()
print(sol.replaceEveryCharWithLast("Hello How Are you?"))
