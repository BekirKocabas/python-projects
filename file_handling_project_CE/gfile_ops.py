def read_file(file_name):
    """ Reads in a file.    
        1. Opened and read the given file into a variable 
        2. Printed the contents of the file
        3. Returned the contents of the file    
    """    

    with open(file_name, mode='r') as f: #open the given file
        f_text = f.read() #read the given file into a variable 
        print(f_text) # Print the contents of the file
        return f_text #Return the contents of the file
    
    #raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list   
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list
    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.    """
    
    f = open(file_name, mode='r')
    content_list = f.readlines()
    return content_list

    #raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.   
        1. Get the first line of file_contents
        2. write the first line into a file with the name from output_filename    
    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """           
    content = file_contents.split("\n")
    first_linie_string = content[0]
    with open(output_filename, 'w') as w_file:
         w_file.write(first_linie_string)    
  
    #raise NotImplementedError() 


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file    
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list
    Args:
        file_name: the name of the file to be read
    Returns:
        list: a list of the even-numbered lines of the file
    """   
    file = open(file_name, mode="r")
    file_list = file.readlines()
    even_list =[]
    for i in range(len(file_list)):
        if i % 2:
            even_list.append(file_list[i])
    return even_list
    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order    
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list
    Args:
        file_name: the name of the file to be read
    Returns:
        list: list of the lines of the file in reverse order.
    """    
    file = open(file_name, mode="r")
    file_list = file.readlines()
    file_list_reverse = file_list[::-1]
    print(file_list_reverse)
    return file_list_reverse
    raise NotImplementedError()

def main():
    file_contents = read_file("sampletext.txt")   
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()