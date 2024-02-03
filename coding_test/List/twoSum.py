# Two Pointer 활용
# nlogn인 오름차순 정렬 활용 
# 양 끝에 포인터 두 개 두고 더함 → target보다 크면 오른쪽 포인터 왼쪽으로 옮김, 작으면 왼쪽 포인터 오른쪽으로 한 칸 옮김 → 점점 target에 가까워짐 → 포인터 같은 곳 가리키기 전까지

def twoSum(nums, target):
    nums.sort()
    l, r=0, len(nums)-1
    
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return True
    return False

print(twoSum(nums = [4,1,9,7,5,3,16], target=14))
            
            
    