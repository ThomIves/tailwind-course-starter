def solution(s):
    length = len(s)
    my_L = []
    
    for i in range(0, length, 2):
        my_L.append(f"{s[i]}{s[i + 1]}")
        
    count = 1
    result = ""
    i = 0
    
    while i < len(my_L) - 1:
        now = my_L[i]
        print(now)
        next = my_L[i + 1]
        print(next)
        
        if now == next:
            count += 1
            
        if next != now:
            result += f"{now}{count}"
            count = 1

        if next != now and i == len(my_L) - 2:
            result += f"{next}{count}"
            
        i += 1
        print(result)
        print()
            
    return result
        
    
print(solution("aaabbabbababacab"))

# def encode_rle(s):
#     groups = []
#     current_group_char = None
#     current_group_length = 0

#     for char in s:
#         if char.isdigit() or char.isalpha():
#             if char == current_group_char:
#                 current_group_length += 1
#             else:
#                 if current_group_char is not None:
#                     groups.append((current_group_char, current_group_length))
#                 current_group_char = char
#                 current_group_length = 1
#     if current_group_char is not None:
#         groups.append((current_group_char, current_group_length))
    
#     return groups

# def encode_rle(s):
#     rle = ""
#     current_group_char = None
#     current_group_length = 0

#     for char in s:
#         if char.isdigit() or char.isalpha():
#             if char == current_group_char:
#                 current_group_length += 1
#             else:
#                 if current_group_char is not None:
#                     rle += f"{current_group_char}{current_group_length}"
#                 current_group_char = char
#                 current_group_length = 1
#     if current_group_char is not None:
#         rle += f"{current_group_char}{current_group_length}"
    
#     return rle
    
    
# print(encode_rle("aaa@@bb!!c#d**e"))