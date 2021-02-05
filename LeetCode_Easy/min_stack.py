# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# Methods pop, top and getMin operations will always be called on non-empty stacks.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> None:
        self.array.pop(-1)

    def top(self) -> int:
        return self.array[len(self.array) - 1]

    def getMin(self) -> int:
        min = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] < min:
                min = self.array[i]
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()