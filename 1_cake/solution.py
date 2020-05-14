def solution(s):
    # Your code here
    l = len(s)
    if l == 1:
        return 1

    def get_sub(length, string):
        return string[:length]

    piece = 1
    while piece <= l // 2:
        sub = get_sub(piece, s)
        if sub[0] == s[piece]:
            c = s.count(sub)
            if c * len(sub) == l:
                return c
        piece += 1
    return 1


def test():
    out = solution("abcabcabcabc")
    print('case: "abcabcabcabc"')
    print('expected = 4')
    print('actual = ' + str(out))
    print('passed = ' + str(4 == out))

    out = solution("abccbaabccba")
    print('case: "abccbaabccba"')
    print('expected = 2')
    print('actual = ' + str(out))
    print('passed = ' + str(2 == out))

    out = solution("abccbasdvfs4ghwfbhscfbewtjndfnabccba")
    print('case: "abccbasdvfs4ghwfbhscfbewtjndfnabccba"')
    print('expected = -1')
    print('actual = ' + str(out))
    print('passed = ' + str(-1 == out))


test()
