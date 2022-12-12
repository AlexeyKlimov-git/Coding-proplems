def generateParenthesis(n):
    ans = []

    def backtrack(S=[], left=0, right=0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(")")
            backtrack(S, left, right + 1)
            S.pop()

    backtrack()
    return ans

print(generateParenthesis(3))


class Solution:
    def generateParenthesis(self, n: int):
        rv = []
        stack = [("(", n - 1, n)]

        while stack:
            item = stack.pop()

            s = item[0]
            o = item[1]
            c = item[2]

            if o == 0 and c == 0:
                rv.append(s)
            else:
                if o != 0:
                    stack.append([s + "(", o - 1, c])

                if o < c:
                    stack.append([s + ")", o, c - 1])

        return rv

a = Solution()
print(a.generateParenthesis(3))