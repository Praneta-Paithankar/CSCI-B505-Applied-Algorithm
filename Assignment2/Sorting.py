import FileOperations,time
import sys


def partition(numbers, start, end):
    pivot = numbers[end]
    i = start - 1
    for j in range(start, end):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    i += 1
    numbers[i], numbers[end] = numbers[end], numbers[i]
    return i


def quick_sort(numbers, start, end):
    if start < end:
        pi = partition(numbers, start, end)
        quick_sort(numbers, start, pi - 1)
        quick_sort(numbers, pi + 1, end)
    return


def merge(numbers, start, mid, end):
    lindex = start
    rindex = mid + 1
    arr = [0] * (end -start + 1)
    k = 0
    for i in range(start, end + 1):
        if lindex > mid:  # checks if left part comes to an end or not
            arr[k] = numbers[rindex]
            k += 1
            rindex += 1
        elif rindex > end:  # checks if second part comes to an end or not
            arr[k] = numbers[lindex]
            k += 1
            lindex += 1
        elif numbers[lindex] < numbers[rindex]:
            arr[k] = numbers[lindex]
            k += 1
            lindex += 1
        else:
            arr[k] = numbers[rindex]
            k += 1
            rindex += 1
    for i in range(k):
        numbers[start] = arr[i]
        start += 1
    return


def merge_sort(numbers, l, r):
    if r > l:
        mid = (l + r) / 2
        merge_sort(numbers, l, mid)
        merge_sort(numbers, mid + 1, r)
        merge(numbers, l, mid, r)
    return


#sort numbers using insertion sort
def insertion_sort(numbers):
    for j in xrange(1,len(numbers)-1):
        key = numbers[j]
        i = j-1
        while i >= 0 and numbers[i]>key:
            numbers[i+1] = numbers[i]
            i=i-1
        numbers[i+1] = key
    return numbers


# get input
def get_input(file_name):
    input_list = []
    with open(file_name) as f:
        for line in f:
            numbers = map(int, line[1:-2].split(","))
            input_list.append(numbers)
    return input_list


# Read data from file and use merge sort for sorting random numbers
def run_merge_sort():
    with open("Output/mergesortOutput.csv", "w") as csvfile:
        #f.write("Number of input : average time \n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            time_list=[]
            file_name = "Input/{0}random.txt".format(x)
            input = get_input(file_name)
            for numbers in input:
                start_time = time.time()
                merge_sort(numbers,0,len(numbers)-1)
                end_time=time.time()
                time_list.append(end_time-start_time)
                # print numbers
            print time_list
            avg_time=sum(time_list)/len(time_list)
            print avg_time
            csvfile.write("{0},{1}\n".format(x, avg_time))
    return


# Read data from file and use quick sort for sorting random numbers
def run_quick_sort():
    with open("Output/quicksortOutput.csv", "w") as csvfile:
        #f.write("Number of input : average time \n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            time_list=[]
            file_name = "Input/{0}random.txt".format(x)
            input = get_input(file_name)
            for numbers in input:
                start_time = time.time()
                quick_sort(numbers,0,len(numbers)-1)
                end_time=time.time()
                time_list.append(end_time-start_time)
                #print numbers
            print time_list
            avg_time=sum(time_list)/len(time_list)
            print avg_time
            csvfile.write("{0},{1}\n".format(x, avg_time))
    return


#Read data from file and use insertion sort for sorting random numbers
def run_insertionsort():
    with open("Output/insertionsortOutput.csv", "w") as f:
        #f.write("Number of input :average time\n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            time_list=[]
            file_name = "Input/{0}random.txt".format(x)
            input = get_input(file_name)
            for numbers in input:
                start_time = time.time()
                sorted_numbers= insertion_sort(numbers)
                end_time=time.time()
                time_list.append(end_time-start_time)
                #print sorted_numbers
            print time_list
            avg_time = sum(time_list) / len(time_list)
            print avg_time
            f.write("{0},{1}\n".format(x, avg_time))


#Read data from file and use insertion sort for sorting non-decreasing random numbers
def run_non_decreasing_insertionsort():
    with open("Output/NonDecreasingInsertionSort.csv", "w") as f:
        #f.write("Number of input : time\n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nondecreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = insertion_sort(numbers)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return


#Read data from file and use insertion sort for sorting non-increasing random numbers
def run_non_increasing_insertionsort():
    with open("Output/NonIncreasingInsertionSort.csv", "w") as f:
        #f.write("Number of input :time \n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nonincreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = insertion_sort(numbers)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return


#Read data from file and use quick sort for sorting non-decreasing random numbers
def run_non_decreasing_quicksort():
    with open("Output/NonDecreasingQuickSort.csv", "w") as f:
        #f.write("Number of input : time\n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nondecreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = quick_sort(numbers,0,len(numbers)-1)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return


#Read data from file and use quick sort for sorting non-increasing random numbers
def run_non_increasing_quicksort():
    with open("Output/NonIncreasingQuickSort.csv", "w") as f:
        #f.write("Number of input :time \n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nonincreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = quick_sort(numbers,0,len(numbers)-1)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return


#Read data from file and use merge sort for sorting non-decreasing random numbers
def run_non_decreasing_mergesort():
    with open("Output/NonDecreasingMergeSort.csv", "w") as f:
        #f.write("Number of input : time\n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nondecreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = merge_sort(numbers,0,len(numbers)-1)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return


#Read data from file and use merge sort for sorting non-increasing random numbers
def run_non_increasing_mergesort():
    with open("Output/NonIncreasingMergeSort.csv", "w") as f:
        #f.write("Number of input :time \n")
        for x in xrange(500, 10500, 500):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nonincreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = merge_sort(numbers,0,len(numbers)-1)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return

def main():
    sys.setrecursionlimit(20000)
    FileOperations.create_folder("Output")
    print "random quick sort"
    run_quick_sort()
    print "random merge sort"
    run_merge_sort()
    print "random insertion  sort"
    run_insertionsort()
    print "non-increasing insertion sort"
    run_non_decreasing_insertionsort()
    print "non-increasing insertion sort"
    run_non_increasing_insertionsort()
    print "non-increasing quick sort"
    run_non_decreasing_quicksort()
    print "non-increasing quick sort"
    run_non_increasing_quicksort()
    print "non-increasing merge sort"
    run_non_decreasing_mergesort()
    print "non-increasing merge sort"
    run_non_increasing_mergesort()
    print "Operations completed"
    return

if __name__ == "__main__":
    main()
