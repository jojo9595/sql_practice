import numpy as np

msg = "hello"
print(msg)
print(np.random.randint(1,9))
print('\\\n\\')
print('I\'m learning\nPython.')
print(r'\\\t\\')

arr = ['python', 'java', ['asp', 'php'], 'c']
print(arr)
# 从数组 nums 中读取下标为 i 的数据元素值
def value(nums, i):
    if 0 <= i <= len(nums) - 1:
        print(nums[i])
        
arr = [0, 5, 2, 3, 7, 1, 6]
print('从数组 nums 中读取下标为 i 的数据元素值')
value(arr, 3)

# 从数组 nums 中查找元素值为 val 的数据元素第一次出现的位置
def find(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1

arr = [0, 5, 2, 3, 7, 1, 6]
print('从数组 nums 中查找元素值为 val 的数据元素第一次出现的位置')
print(find(arr, 5))

#在数组第i个位置上插入值为val 的元素

arr = [0, 5, 2, 3, 7, 1, 6]
i, val = 2, 4
arr.insert(i, val)
print(arr)

#将数组中第i个元素值改为val
def change(nums, i, val):
    if 0 <= i <= len(nums) - 1:
        nums[i] = val
        
arr = [0, 5, 2, 3, 7, 1, 6]
i, val = 2, 4
change(arr, i, val)
print(arr)

#删除数组尾部元素
arr = [0, 5, 2, 3, 7, 1, 6]
arr.pop()
print(arr)

#删除数组第 i 个位置上的元素
arr = [0, 5, 2, 3, 7, 1, 6]
i = 4
arr.pop(i)
print(arr)

#基于条件删除元素
arr = [0, 5, 2, 3, 7, 1, 6]
arr.remove(5)
print(arr)

