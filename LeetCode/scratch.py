import timeit
import random

# time = 357.3 len 501
def last_ind1():
    rand_nums = [random.randint(0, 100) for x in range(80)]
    rand_val = random.randint(0, 79)
    return ''.join(str(rand_nums)).rindex(str(rand_nums[rand_val]))

# time = 313.9 len 501
def last_ind2():
    rand_nums = [random.randint(0, 100) for x in range(80)]
    rand_val = random.randint(0, 79)
    return len(rand_nums) - 1 - rand_nums[::-1].index(rand_nums[rand_val])

# time = 342.6 len 501
def last_ind3():
    rand_nums = [random.randint(0, 100) for x in range(80)]
    rand_val = random.randint(0, 79)
    return max(ind for ind,v in enumerate(rand_nums) if v == rand_nums[rand_val])


# print(timeit.timeit("last_ind1()", setup="from __main__ import last_ind1"))
# print(timeit.timeit("last_ind2()", setup="from __main__ import last_ind2"))
# print(timeit.timeit("last_ind3()", setup="from __main__ import last_ind3"))


c = "()()()"
c.replace("()", "")
print(c)