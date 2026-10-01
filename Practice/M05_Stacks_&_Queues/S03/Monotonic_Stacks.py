def monotonic_increase(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack 
arr = [1, 3, 2, 4, 5]
print(monotonic_increase(arr))  

def monotonic_decrease(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack
arr = [5, 3, 4, 2, 1]
print(monotonic_decrease(arr))  

def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result
arr = [5,3,50,2,25]
print(next_greater_element(arr))