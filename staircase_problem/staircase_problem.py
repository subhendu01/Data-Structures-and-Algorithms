# At a time you can take 1 step or 2 step (total stairase - 4) then you can cover with 2 or 4 steps.
# num_ways(N) = num_ways(N-1) + num_ways(N-2)
# num_ways(0) = 1
# num_ways(1) = 1

def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

# more efficient way
def num_ways_buttom_up(n):
    if n == 0 or n == 1: return 1
    nums = []
    nums.append(1)
    nums.append(1)
    for i in range(2, n):
        nums[i] = nums[i-1] + nums[i-2]
    return nums

if __name__ == "__main__":
    print(num_ways_buttom_up(4))