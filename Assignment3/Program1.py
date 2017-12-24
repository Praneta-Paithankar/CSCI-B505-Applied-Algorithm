
def calculate_partition(n):
    partitions = [0, 1, 1, 2, 4]
    for i in range(5, n+1):
        val = (partitions[i - 1] + partitions[i - 3] + partitions[i-4])
        val=val%100000
        partitions.append(val)
    return partitions[n]


res=calculate_partition(11000)
print res