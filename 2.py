valid = 0

with open(".\\inputfiles\\2.txt") as file:
    lines = file.readlines()

def is_increasing(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def is_decreasing(lst):
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def has_valid_differences(lst):
    return all(1 <= abs(lst[i] - lst[i - 1]) <= 3 for i in range(1, len(lst)))

for line in lines:
    line = line.strip() 
    line = line.split()  
    line = list(map(int, line))  
    
    if (is_increasing(line) or is_decreasing(line)) and has_valid_differences(line):
        valid += 1
    else:
        safe_after_removal = False
        for i in range(len(line)):
            modified_line = line[:i] + line[i+1:]  
            if (is_increasing(modified_line) or is_decreasing(modified_line)) and has_valid_differences(modified_line):
                safe_after_removal = True
                break
       
        if safe_after_removal:
            valid += 1

print(valid)
