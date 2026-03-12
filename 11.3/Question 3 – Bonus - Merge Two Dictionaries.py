def merge_dictionaries(dict1, dict2):
    result = dict1.copy()

    for key, value2 in dict2.items():
        if key in result:
            value1 = result[key]
            if len(value2) > len(value1):
                result[key] = value2
        else:
            result[key] = value2

    return result



d1 = {"name": "Dan", "city": "Tel Aviv", "job": "Dev"}
d2 = {"name": "Daniel", "city": "TA", "country": "Israel"}

merged = merge_dictionaries(d1, d2)
print(merged)
