def Nminelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        min1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > min1: 
                min1 = list1[j]; 
                  
        list1.remove(min1); 
        final_list.append(min1) 
          
    print(final_list)
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
N = 2
Nminelements(list1, N)
