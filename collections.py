from collections import defaultdict

citiMap = defaultdict(list)
citiMap["US"] = ["New York", "DC"]
citiMap["Canada"] = ["Toronto"]
citiMap["India"] = ["Mumbai"]

print(citiMap.keys())
print(citiMap.values())