import itertools
__author__ = 'SinLapis'

def apriori(transactions, min_support):

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

    def cut(ck, ck_support, lk, lk_support, min_support):
        i = 0
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
        for ci_plus in itertools.combinations(items, k):
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


    c = [0, []]
    c_support = [0, []]
    l = [0, []]
    l_support = [0, []]
    c_set = []
    for transaction in transactions:
        for item in transaction:
            c_set.append(item)

    c_set = set(c_set)
    for item in c_set:
        c[1].append(set(item))
        c_support[1].append(0)




