def SpecialSort(myDict):
    print(sorted(myDict.items(), key=lambda kv: (kv[1], kv[0])))

# SpecialSort({
#     1: 40, 3: 2, 4: 2, -1: 1})
