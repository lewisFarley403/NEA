class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        steps = 0
        for char in key:
            # print(ring)
            pos = []
            dist = 10000000000
            index = None
            for i, letter in enumerate(ring):
                #print(ring[0], char)
                if letter == char:
                    if abs(i - len(ring)) < abs(dist):
                        dist = i-len(ring)
                        index = i
                    if i < abs(dist):
                        print(i, char)
                        dist = i
                        index = i
                dire = -1 if dist < 0 else 1
            for _ in range(abs(dist)):
                # print(ring)
                ring = self.rotate(ring, dire)
            #print(abs(dire), char)
            steps += abs(dist)+1
        return steps

    def rotate(self, ring, direction):
        # 1 left, -1 right
        if direction == 1:
            return ring[1:]+ring[0]
        return ring[-1]+ring[:-1]


s = Solution()
print(s.findRotateSteps('godding', 'godding'))
