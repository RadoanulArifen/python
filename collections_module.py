import collections

fruits=['apple','banana','apple','orange']
print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(2))