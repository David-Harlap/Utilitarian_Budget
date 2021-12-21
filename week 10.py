def utilitarian_budget(total: float, subject: list[str], pref: list[list[str]]):
    d = total / len(pref)
    sum_pay = {i: 0 for i in subject}
    matrix = [[0 for x in range(len(pref))] for y in range(len(subject))]
    count_subject = {i: 0 for i in subject}
    for citiz in pref:
        for sub in citiz:
            count_subject[sub] = count_subject[sub] + 1
    print(count_subject)

    for citiz in pref:
        temp = count_subject
        temp1 = list(filter(lambda x: x in citiz, temp.keys()))  # maximum value
        max_value = max(list([temp[x] for x in temp if x in temp1]))
        max_keys = [k for k, v in count_subject.items() if v == max_value]
        pay = d / len(max_keys)
        print("Citizen {} should donate:".format(pref.index(citiz)), end=" ")
        for sub in max_keys:
            sum_pay[sub] = sum_pay[sub] + pay
            print("{} to {}".format(pay, sub), end=" ")
        print()

    print("\nsum of all is: ", sum_pay)


if __name__ == '__main__':
    utilities = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['a']]
    utilitarian_budget(500, ['a', 'b', 'c', 'd'], utilities)
"""
Citizen 0 should donate: 100.0 to a 
Citizen 1 should donate: 100.0 to a 
Citizen 2 should donate: 100.0 to a 
Citizen 3 should donate: 50.0 to b 50.0 to c 
Citizen 4 should donate: 100.0 to a 

sum of all is:  {'a': 400.0, 'b': 50.0, 'c': 50.0, 'd': 0}
"""