import itertools
__author__ = 'SinLapis'

def apriori(transactions, min_support, min_confidence):



    def count(ck, transactions):
        i = 0
        ck_support = []
        for ci in ck:
            support = 0
            for transaction in transactions:
                transaction_set = set(transaction)
                if transaction_set.issuperset(ci):
                    support += 1
            ck_support.append(support)
            i += 1
        return ck_support

    def cut(ck, ck_support, min_support):
        i = 0
        lk = []
        lk_support = []
        for ci_support in ck_support:
            if ci_support >= min_support:
                lk.append(ck[i])
                lk_support.append(ck_support)
            i += 1
        return lk, lk_support

    def connect(lk, k):
        ck_plus = []
        items = []
        for li in lk:
            for item in li:
                items.append(item)
        items = set(items)
        for ci_plus in itertools.combinations(items, k + 1):
            ci_set = set(ci_plus)
            flag = True
            for item in ci_set:
                ci_subset = ci_set - {item}
                if not ci_subset in lk:
                    flag = False
                    break
            if flag:
                ck_plus.append(ci_set)
        return ck_plus

    def associate(frequent_sets, c, c_support, min_confidence):
        frequent_subsets = []
        frequent_subsets_support = []
        for i in range(1, len(c)):
            for ci in c[i]:
                for frequent_set in frequent_sets:
                    if frequent_set.issuperset(ci):
                        frequent_subsets.append(ci)
                        frequent_subsets_support.append(c_support[i][c[i].index(ci)])
        frequent_subsets_confidence = []
        i = 0
        for frequent_item in frequent_subsets:
            for frequent_set in frequent_sets:
                frequent_set_support = (
                    frequent_subsets_support[frequent_subsets.index(frequent_set)])
                complement = frequent_set - frequent_item
                if complement != set():
                    frequent_item_support = (
                        frequent_subsets_support[frequent_subsets.index(frequent_item)])
                    confidence = frequent_set_support / frequent_item_support
                    if confidence >= min_confidence:
                        frequent_subsets_confidence.append([
                            frequent_item,
                            complement,
                            confidence
                        ])
        return frequent_subsets_confidence


    c = [[], []]
    c_support = [[], []]
    l = [[], []]
    l_support = [[], []]
    c_set = []
    for transaction in transactions:
        for item in transaction:
            c_set.append(item)

    c_set = set(c_set)
    for item in c_set:
        c[1].append(set(item))
        c_support[1].append(0)
    i = 1
    c.append([])
    while True:
        c_support[i] = count(c[i], transactions)
        c_support.append([])
        l[i], l_support[i] = cut(c[i], c_support[i], min_support)
        l.append([])
        l_support.append([])
        c[i + 1] = connect(l[i], i)
        if c[i + 1] == []:
            break
        c.append([])
        i += 1

    association_rules = associate(c[-2], c, c_support, min_confidence)
    for rule in association_rules:
            print("%s => %s: %f" % (rule[0], rule[1], rule[2]))

transactions = [
    ['A', 'C', 'D'],
    ['B', 'C', 'E'],
    ['A', 'B', 'C', 'E'],
    ['B', 'E']
]
min_support = 2
min_confidence = 0.5
apriori(transactions, min_support, min_confidence)




