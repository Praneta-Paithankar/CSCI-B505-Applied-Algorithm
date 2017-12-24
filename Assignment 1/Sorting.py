import time,FileOperations

#Sort numbers using bubble sort
def bubble_sort(numbers):
    for i in xrange(0, len(numbers)-1):
        for j in xrange(len(numbers)-1, i, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
    return numbers

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

#get input
def get_input(file_name):
    input_list = []
    with open(file_name) as f:
        for line in f:
            numbers = map(int, line[1:-2].split(","))
            input_list.append(numbers)
    return input_list

#Read data from file and use bubble sort for sorting random numbers
def run_bubblesort():
    with open("Output/bubblesortOutput.csv", "w") as csvfile:
        #f.write("Number of input : average time \n")
        for x in xrange(400, 10000, 400):
            print "No of inputs:{0}\n".format(x)
            time_list=[]
            file_name = "Input/{0}random.txt".format(x)
            input = get_input(file_name)
            for numbers in input:
                start_time = time.time()
                sorted_numbers= bubble_sort(numbers)
                end_time=time.time()
                time_list.append(end_time-start_time)
                #print sorted_numbers
            print time_list
            avg_time=sum(time_list)/len(time_list)
            print avg_time
            csvfile.write("{0},{1}\n".format(x, avg_time))
    return

#Read data from file and use insertion sort for sorting random numbers
def run_insertionsort():
    with open("Output/insertionsortOutput.csv", "w") as f:
        #f.write("Number of input :average time\n")
        for x in xrange(400, 10000, 400):
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

#Read data from file and use bubble sort for sorting non-decreasing random numbers
def run_non_decreasing_bubblesort():
    with open("Output/NonDecreasingBubbleSort.csv","w") as f:
        #f.write("Number of input : time\n")
        for x in xrange(400, 10000, 400):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nondecreasing.txt".format(x)
            input = get_input(file_name)
            numbers= input[0]
            start_time = time.time()
            sorted_numbers = bubble_sort(numbers)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return

#Read data from file and use bubble sort for sorting non-increasing random numbers
def run_non_increasing_bubblesort():
    with open("Output/NonIncreasingBubbleSort.csv","w") as f:
        #f.write("Number of input : time \n ")
        for x in xrange(400, 10000, 400):
            print "No of inputs:{0}\n".format(x)
            file_name = "Input/{0}nonincreasing.txt".format(x)
            input = get_input(file_name)
            numbers = input[0]
            start_time = time.time()
            sorted_numbers = bubble_sort(numbers)
            end_time = time.time()
            runtime = end_time - start_time
            #print sorted_numbers
            print runtime
            f.write("{0},{1}\n".format(x, runtime))
    return

#Read data from file and use insertion sort for sorting non-decreasing random numbers
def run_non_decreasing_insertionsort():
    with open("Output/NonDecreasingInsertionSort.csv", "w") as f:
        #f.write("Number of input : time\n")
        for x in xrange(400, 10000, 400):
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
        for x in xrange(400, 10000, 400):
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


def main():
    FileOperations.create_folder("Output")
    print "random bubble sort"
    run_bubblesort()
    print "random insertion  sort"
    run_insertionsort()
    print "non-decreasing bubble sort"
    run_non_decreasing_bubblesort()
    print "non-increasing insertion sort"
    run_non_decreasing_insertionsort()
    print "non-decreasing bubble sort"
    run_non_increasing_bubblesort()
    print "non-increasing insertion sort"
    run_non_increasing_insertionsort()
    print "Operations completed"

if __name__ == '__main__':
    main()
