# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index):
    subset_list = []
    for i in range(start_index ,end_index):
        subset_list.append(input_list[i])
    return subset_list
subset([1,2,3,4,5,6,7,8,9], 3, 8)

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list, step_size):
    nth_list = []
    for i in range(0, len(input_list), step_size):
        nth_list.append(input_list[i])
    return nth_list
every_nth([0,1,2,3,4,5,6,7,8,9],3)

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(c in special_characters for c in input_list):
        return True
    else:
        return False
unique(["a","b","c","$"])

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    flat_list = [num for sublist in input_list for num in sublist]
    return flat_list
flatten([[1], [2, 3], [4, 5, 6, 7]])

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    return_list = []
    for arg in args:
        return_list.extend(arg)
    return return_list

# %%
merge_lists([1,2,3,4],[5,6,7],[8,9])

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    return [tuple(reversed(tup)) for tup in input_list]

# %%
reverse_tuples([(1,2),(3,4)])

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_duplicates(input_list):
    return_list = []
    for i in range(len(input_list)):
        if input_list[i] not in return_list:
            return_list.append(input_list[i])
    return return_list

# %%
remove_duplicates([1,2,3,4,5,5,6,6,1])

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    rez = [[input_list[j][i] for j in range(len(input_list))] for i in range(len(input_list[0]))]
    return rez

# %%
transpose([[1,2],[3,4],[5,6]])

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list, chunk_size):
    return_list = []
    for i in range(0, len(input_list), chunk_size):
        return_list.append(input_list[i:i+chunk_size])
    return return_list


# %%
split_into_chunks([1,2,3,4,5,6,7,8,9], 3)

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    d = {}
    for i in dict:
        d.update(i)
    return d

# %%
merge_dicts({'Laci':15, 'Jani':20},{'Sanyi':12,'Karcsi':32},{'Ica':19,'Marcsi':24})

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%

def by_parity(input_list):
    even_list = []
    odd_list = []
    for i in range(len(input_list)):
        if input_list[i] % 2 == 1:
            odd_list.append(input_list[i])
        else:
            even_list.append(input_list[i])
    return {"even":even_list,"odd":odd_list}

# %%
by_parity([1,2,3,4])

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    for i in input_dict.keys():
        k = 0
        for j in input_dict[i]:
            k += j
        input_dict[i] = int(k/len(input_dict[i]))
    return input_dict

# %%
mean_key_value({'First':[1,2,3],'Second':[3,4,5],'Third':[5,6,7]})

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


