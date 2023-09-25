def jump(nums): 
    to_arrive = len(nums) - 1
    for i in range(to_arrive - 1, -1, -1):
        if nums[i] >= to_arrive - i:
            to_arrive = i
    print(to_arrive)
    return to_arrive == 0

print(jump([0,3,0,0,4]))
print(jump([10,0,2,0,4]))
    
