try: # I reality, I would probeably check if the variable has a certain type, instead of try and except
    first_experiment_id : int = int(input("First experiment id:"))
except ValueError:
    print("Please enter a valid number")
    exit()
    
experiment_list : list = []
name : str = "Moritz Mattes"
date : str = "11.03.2025"

try:
    for experiment_id in range(first_experiment_id,first_experiment_id + 10):
            experiment_list.append({"id" :experiment_id,"name": name, "date" : date})

except TypeError:
    print("Please enter a valid number")
    exit()

count : int = 0

for experiment in experiment_list:
    if experiment["id"] % 2 == 0:
        count += 1

print("Number of experiments with even id:", count)

for i in experiment_list[:5]:
    print(i)
