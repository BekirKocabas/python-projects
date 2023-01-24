''' 
Import statements: 
    1. Imported the built-in json python package
    2. From employee.py, imported the details function and the employee_name, age, title variables
'''

import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    """ Created a dictionary that stores an employee's information  
        1. Returned a dictionary that maps "first_name" to name, "age" to age, and "title" to title
    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee
    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
               name, age, and title arguments, respectively.
    """
    return {"first_name":name, "age":int(age), "title":title}
    
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    """ Written json string to file 
        1. Opened a new file defined by output_file
        2. Written json_obj to the new file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
    """
    try:
        newfile = open(output_file, mode="w")
        newfile.write(json_obj)
    
        newfile.close()
    except Exception as e:
        raise NotImplementedError()

def main():
    # Printed the contents of details()
    details()

    # Created employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    ''' 
    Used a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''    
    # In the line below replace the None keyword with my code. 
    # The format should look like: variable = json.dumps(dict)
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Written out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()