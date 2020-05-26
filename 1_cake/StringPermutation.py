def checkInclusion(self, s1: str, s2: str) -> bool:
    d = {}
    l = len(s1)
    for char in s1:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    def check(i):
        d_temp = d
        for j in range(l):
            if s2[j + i] in d_temp:
                if d_temp[s2[j + i]] > 0:
                    d_temp[s2[j + i]] -= 1
                    continue
            return False
        return True

    print(d)
    for i in range(len(s2)):
        if s2[i] in d:
            if check(i):
                return True
    return False

