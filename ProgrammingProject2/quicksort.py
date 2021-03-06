#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohbock 

#QuickSort pulled from online repository 
# """https://gist.github.com/anirudhjayaraman/897ca0d97a249180a48b50d62c87f239"""


def quicksort(lista,start,end):
   i = start
   j = end
   pivote = lista[(start + end)//2]

   swap_count = 0
   while i <= j:
      while lista[i] < pivote:
         i += 1
      while pivote < lista[j]:
         j -= 1
      if i <= j:
         aux = lista[i]
         lista[i] = lista[j]
         lista[j] = aux
         swap_count += 1
         i += 1
         j -= 1

   if start < j:
      swap_count += quicksort(lista, start, j)
   if i < end:
      swap_count += quicksort(lista, i, end)

   return swap_count

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
count = quicksort(alist, 0, len(alist)-1)
print("Swaps: ", count)
print(alist)

