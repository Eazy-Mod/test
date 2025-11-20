n_m = input()
n_m_array =    list(map(int, n_m.strip("[]").split())) 
n_numb = n_m_array[1]
m_numb = n_m_array[0]

print("n"+str(n_numb))
print("m"+str(m_numb))


ai = input()
aix_array = list(map(int, ai.strip("[]").split()))

b1 = input()
b1x_array = list(map(int, b1.strip("[]").split()))

print(aix_array)
print(b1x_array)


nfix_index = []
mfix_index = []

ai_array = aix_array.copy()
#sort
tot2 = n_numb
for i in range(tot2):
    x = max(ai_array)
    index_of_arr = ai_array.index(x)
    nfix_index.insert(index_of_arr,nfix_index)
    mfix_index.insert(index_of_arr,mfix_index)

print(nfix_index)
print(mfix_index)

#operation


# total = n_numb
# strength = m_numb
# while total > 0:
#     continue




# s = "[1 2 3 4]"
# # Remove brackets and split by space
# numbers_str = s.strip("[]").split()
# my_list = list(map(int, numbers_str)) 

# for i in my_list:
#     print(i)

