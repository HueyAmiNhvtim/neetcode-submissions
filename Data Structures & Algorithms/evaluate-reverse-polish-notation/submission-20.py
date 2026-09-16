class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_dict = dict()
        
        op_dict["+"] = lambda x, y: x + y
        op_dict["*"] = lambda x, y: x * y
        op_dict["-"] = lambda x, y: x - y
        op_dict["/"] = lambda x, y: x / y

        if not tokens:
            return 0
        for i in range(0, len(tokens)):
            char = tokens[i]
            if char not in op_dict:
                stack.append(int(char))
            else:
                first_val = float(stack.pop())
                second_val = float(stack.pop())
                op_res = int(op_dict[char](second_val, first_val))
                stack.append(op_res)
        return stack.pop()