class Job:
    def __init__(self, start_time, finish_time, weight):
        self.start_time = start_time
        self.finish_time = finish_time
        self.weight = weight


def binary_search(jobs, start_index):
    low = 0
    high = start_index - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid].finish_time <= jobs[start_index].start_time:
            if jobs[mid + 1].finish_time <= jobs[start_index].start_time:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def job_scheduler(jobs):
    n = len(jobs)
    total_weight = [0 for i in range(n)]
    total_weight[0] = jobs[0].weight
    for i in range(1, n):
        current_weight = jobs[i].weight
        pre_index = binary_search(jobs, i)
        if pre_index != -1:
            current_weight += total_weight[pre_index]
        total_weight[i] = max(current_weight, total_weight[i - 1])
    return total_weight[n - 1]


with open("input1.txt","r") as f:
    jobs=[]
    for line in f.readlines():
        data=line.split()
        jobs.append(Job(int(data[0]),int(data[1]),int(data[2])))
    jobs=sorted(jobs,key=lambda y: y.finish_time)
print job_scheduler(jobs)
