def solution(nums):
    return len(set(nums)) if len(set(nums)) < (len(nums)/2) else int(len(nums)/2)
