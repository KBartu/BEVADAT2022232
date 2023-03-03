# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def contains_odd(input_list):
    if any(item % 2 == 1 for item in input_list):
        return True
    return False

# %%
contains_odd([0,2,4])

# %%
contains_odd([0,1,2,4])

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
    bool_list = []
    for i in input_list:
        if input_list[i] % 2 == 1:
            bool_list.append("True")
        else:
            bool_list.append("False")
    return bool_list


# %%
is_odd([0,1,2,3,4,5,6,7,8,9])

# %%
#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list1, input_list2):
    sum_list = []
    sum_list.append([sum(value) for value in zip(input_list1, input_list2)])
    return sum_list

# %%
element_wise_sum([12,23,5,8], [2,7,6,13])

# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict):
    dict_list = []
    for i in input_dict:
        k = (i, input_dict[i])
        dict_list.append(k)
    return dict_list

# %%
dict_to_list({'First': 10, 'Second': 12, 'Third': 31})

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo



