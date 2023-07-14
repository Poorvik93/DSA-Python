# swap the elements to forward(side) if it is greater than next number

def bubble_operation(A):
    iteration =0
    for i in range (len(A)):
        for j in range (len(A)-i-1):
            iteration +=1
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1] ,A[j]
    return A,iteration

A =[9,8,7,6,5,4,3,2,1]
print(bubble_operation(A))