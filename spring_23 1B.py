def process_groceries(data):
    reversed_data=list(reversed(data))
    sorted_data=sorted(reversed_data)
    return sorted_data
groceries=[181,178,187,182,192,189,202,201]
preocessed_data=process_groceries(groceries)
print(preocessed_data)