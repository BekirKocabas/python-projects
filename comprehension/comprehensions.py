# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings
      1. Used the map() method to apply mod() to all elements in employee_list
   Args:
      employee_list: list of employee objects
   Returns:
      list - A list of strings consisting of name + department.
   """
   map_emp = map(mod, employee_list)
   return list(map_emp)

   raise NotImplementedError()

def generate_usernames(mod_list):
   """ Generates a list of usernames  
   1. Used list comprehension and the replace() function to replace space
      characters with underscores   
   Args:
      mod_list: list of employee-department strings
   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """
   
   def replace_funk(str_item):
      str_new = str_item.replace(" ", "_" )
      return str_new

   underscore_list = [replace_funk(item) for item in mod_list]

   return underscore_list

   raise NotImplementedError()

def map_id_to_initial(employee_list):
   """ Maps employee id to first initial  
   1. Used dictionary comprehension to map each employee's id (value) to the first letter in their name (key)
   Dictionary comprehension looks like:
      dict = { key : value for <item> in <list> }
   Args:
      employee_list: list of employee objects
   Returns:
      dict - A dictionary mapping an employee's id (value) to their first initial (key).
   """   
   list_ids = []

   for i in range(len(employee_list)):
      list_ids.append(employee_list[i]["id"])

   list_names_first = []
   for i in range(len(employee_list)):
      list_names_first.append(employee_list[i]["name"][0])

   dict_first_id = {key : value for (key, value) in zip(list_names_first, list_ids)}
   
   d = {i['name'][0]:i['id'] for i in employee_list} #tek satir kisa yol
   return dict_first_id

   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()