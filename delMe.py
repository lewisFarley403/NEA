class Solution:
    def romanToInt(self, s: str) -> int:
        symbolMap = {'M': 1000, 'D': 500, 'C': 100,
                     'L': 50, 'X': 10, 'V': 5, 'I': 1}
        previousSymbol = s[0]
        total = 0
        run = []
        for symbol in s:

            if symbolMap[symbol] <= symbolMap[previousSymbol]:
                run.append(symbol)
            else:
                reverseRun = run[::-1]
                for i, sym in enumerate(reverseRun):
                    if symbolMap[sym] >= symbolMap[symbol]:
                        break
                sub = 0
                for notSub in reverseRun[i:]:
                    if len(reverseRun) > 1:
                        total += symbolMap[notSub]
                for symb in reverseRun[:i] if i != 0 else [reverseRun[0]]:
                    sub += symbolMap[symb]
                total += (symbolMap[symbol]-sub)
                run = []
            previousSymbol = symbol
        for i in run:
            total += symbolMap[i]
        return total


s = Solution()
print(s.romanToInt(
    "MCMXCIV"))
