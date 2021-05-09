class Solution:

    # code_list     -> list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
    # shopping_cart  -> a list of strings representing the order in which a customer purchases fruit.
    # returns 1 if customer is winnner, otherwise 0

    # loop through shopping cart
    # all codes in code list must be satisfied in order

    # loop
    # 2 vars lookahead and callback
    # look ahead
    # compares item at this index with item in code list iterates
    # maybe slice list and send to another method for verify
    # call back
    # base index that we return to after an unsuccessful verify w/ lookahead
    # iterates after unsuccessful verify
    # jumps after successful verify

    def code_check(self, code_list: [[str]], shopping_cart: [str]) -> int:

        if not code_list:
            return 1

        def equals(code_fruit, cart_fruit):
            if code_fruit == 'anything' or (code_fruit == cart_fruit ):
                return True
            else:
                return False

        def list_equals(code, cart):
            for i in range(len(code)):
                if not equals(code[i], cart[i]):
                    return False
            return True

        start = 0
        code_itr = 0

        while len(shopping_cart) >= len(code_list[code_itr]) and start < len(shopping_cart):

            if equals(code_list[code_itr][0], shopping_cart[start]):

                stop = start + len(code_list[code_itr])
                if list_equals(code_list[code_itr], shopping_cart[start:stop]):
                    code_itr += 1
                    if code_itr == len(code_list):
                        return 1
                    else:
                        shopping_cart = shopping_cart[stop:]
                        start = 0
                        continue
            start += 1
        return 0

    def test(self):
        result = self.code_check([['apple', 'apple'], ['banana', 'anything', 'banana']], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana'])
        print('Success = ' + str(result))

        result = self.code_check([['apple', 'apple'], ['banana', 'anything', 'banana']], ['banana', 'orange', 'banana', 'apple', 'apple'])
        print('Success = ' + str(result))

        result = self.code_check([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'banana', 'apple', 'banana', 'orange', 'banana'])
        print('Success = ' + str(result))

        result = self.code_check([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'apple', 'apple', 'banana'])
        print('Success = ' + str(result))


tester = Solution()
tester.test()
