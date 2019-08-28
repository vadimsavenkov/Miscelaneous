import pandas as pd

sample = pd.DataFrame({"Year":[2015, 2020], "Month":[1,6], "Day":[24,23]})

sample['Month'] = pd.to_datetime(sample['Month'], format = '%b').dt.month

print(sample)

result = pd.to_datetime(sample)


print(result)

'''
defination=np.dtype([('blah', int), ('eow', str), ('wow', float)])
sample= np.ndarray(([1,"a", 2.4]), dtype=[int, str, []])
print(sample)
