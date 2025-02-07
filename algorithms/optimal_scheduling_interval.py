# max task scheduling problem
# loop over list -> find the task with the first finishing time -> remove the task and the previous tasks
def first_finishing_time(arr: list[list[int]]) -> int:
    end_time = arr[0][1]
    pos = 0
    for ind, interval in enumerate(arr):
        if interval[1] < end_time:
            end_time = interval[1]
            pos = ind
    return pos

def remove_intervals(ind: int, arr: list[list[int]]) -> list[list[int]]:
    start_time, end_time = arr[ind][0], arr[ind][1]
    new_arr = []
    for st, en in arr:
        if st >= end_time and en > end_time:
            new_arr.append([st, en])
    return new_arr

def optimal_scheduling_intervals(arr: list[int])-> list[int]:
    arr.sort()
    answer = []
    while arr:
       ind = first_finishing_time(arr)
       answer.append(arr[ind])
       arr = remove_intervals(ind, arr)
    return answer

intervals = [[1,2], [1,3], [2,3], [3,4]]

print(optimal_scheduling_intervals(intervals))