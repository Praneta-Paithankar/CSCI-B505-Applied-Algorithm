import random, os, errno


# To create unique random numbers
def create_input_unique(max_number):
    input_list = random.sample(range(1, max_number + 1), max_number)
    return input_list


# To create random numbers with repetition
def create_input_with_repetition(max_number):
    input_list = [random.randint(1, max_number) for x in range(1, max_number)]
    return input_list


# To create random numbers with repetition(non-decreasing numbers)
def create_non_decreasing_input_using_sort(max_number):
    input_list = create_input_with_repetition(max_number)
    input_list.sort()
    return input_list


# To create random numbers with repetition(non-increasing numbers)
def create_non_increasing_input_using_sort(max_number):
    input_list = create_input_with_repetition(max_number)
    input_list.sort(reverse=True)
    return input_list


# To create folder
def create_folder(foldername):
    try:
        os.mkdir(foldername)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
    return


# To create file
def create_file():
    for x in range(500, 10500, 500):
        file_name = "Input/{0}random.txt".format(x)
        with open(file_name, "w") as f:
            for i in range(10):
                number = create_input_with_repetition(x+1)
                f.write(str(number))
                f.write('\n')
        file_name = "Input/{0}nondecreasing.txt".format(x)
        with open(file_name, "w") as f:
            number = create_non_decreasing_input_using_sort(x+1)
            f.write(str(number))
            f.write('\n')
        file_name = "Input/{0}nonincreasing.txt".format(x)
        with open(file_name, "w") as f:
            number = create_non_increasing_input_using_sort(x+1)
            f.write(str(number))
            f.write('\n')
    return


def main():
    # Create Input Folder
    create_folder("Input")
    # create random files
    create_file()
    print "Files are created successfully."
    return


if __name__ == '__main__':
    main()
