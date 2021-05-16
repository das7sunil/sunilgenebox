from collections import deque

def find_target(values, target):
    dq = deque(sorted([(val,idx) for idx, val in enumerate(values)]))
    print(dq)
    while True:
        if len(dq)< 2:
            raise ValueError("No match Found")

        val_sum = dq[0][0]+dq[-1][0]
        
        if val_sum > target:
            dq.pop()
        elif val_sum < target:
            dq.popleft()    
        else:
            break
    return dq[0], dq[-1]




int_array = [23, 5, 55, 11, 2, 12, 26, 16]
target = 27

result = find_target(int_array, target)
print(result)