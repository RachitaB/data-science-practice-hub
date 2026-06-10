class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            temp = 0
            val=x
            while x!=0:
                rem = x%10
                temp = temp * 10 + rem
                x=x//10
            if temp == val:
                return True
        return False
        