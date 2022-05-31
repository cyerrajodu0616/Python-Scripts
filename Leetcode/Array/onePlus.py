from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        print(digits)
        out = []

        one_plus = digits[0] + 1
        carry_forward = 0

        if one_plus > 9:
            out.append(one_plus - 10)
            carry_forward = 1
        else:
            out.append(one_plus)

        for i in digits[1:]:
            one_plus = i + carry_forward
            carry_forward = 0

            if one_plus > 9:
                out.append(one_plus - 10)
                carry_forward = 1
            else:
                out.append(one_plus)

        if carry_forward != 0:
            out.append(carry_forward)

        out.reverse()
        return out


sol = Solution()
print(Solution.plusOne(sol, [ 9]))
