def selection_sort(input_list):
    for i in range (len (input_list)):
        min_x=i
        for j in range (i +1,len(input_list)):
            if input_list[min_x]>input_list[j]:
                mid_x=j
        input_list[x] ,input_list[min_x]=input_list[min_x],input_list[x]
l=[19,2,31,45,30,11,121,27]
selection_sort(1)
print(1)