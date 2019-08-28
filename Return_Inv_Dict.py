original_dict = { "key1" : "value1", "key2" : "value2", "key3" : "value1" }

def invert_dict(original_dict):
    print(original_dict)
    inverted_dict = {}
    for key, value in original_dict.items():

        if value not in inverted_dict.keys():
            a=[]
            a.append(key)
            inverted_dict[value]=a
        else:
            b=inverted_dict[value]
            b.append(key)
            inverted_dict[value]=b        
    
    return( inverted_dict)



print(invert_dict(original_dict))

