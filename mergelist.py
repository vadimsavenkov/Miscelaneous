def lists_merge(list1, list2):
 merged_list = []
 while len(list1)>0 and len(list2)>0:
    if list1[0] < list2[0]: #Take whichever element is smaller.
      merged_list.append(list1.pop(0))
    else:
      merged_list.append(list2.pop(0))
 if len(list1) == 0: 
      merged_list.append(list2.pop(0))
 elif len(list2) == 0:      
      merged_list.append(list1.pop(0))
 return merged_list

list1=["aa","xx","zz"]
list2=["bb","cc"]
x=lists_merge(list1,list2)
print(x)

def lists_merge(list1, list2):
  
  merged_list = list1 + list2
  merged_list.sort()

  return merged_list

list1 = ['aa', 'xx', 'zz']
list2 = ['bb', 'cc'] 
x=lists_merge(list1,list2)

print (x)