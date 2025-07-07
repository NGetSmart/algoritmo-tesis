from itertools import combinations, product

def powerSet2(n):
    return [list(subset) for k in range(2, n + 1) for subset in combinations(range(1, n + 1), k)]

def hSetsBuilder(n):
    if n < 3:
        return []
    H = [[[0, 1, 2]]]
    for i in range(3, n + 1):
        RV = [[] for _ in range(i - 1)]
        for j in range(i - 2):
            for A in H[j]:
                if 0 in A:
                    RV[i - j - 2].append([i - k for k in A])
        if i % 2 == 0:
            RV[i // 2 - 1].append([0, i // 2, i])
        for S in powerSet2(i - 1):
            l = len(S)
            partialSum = i
            for x in S:
                partialSum += x
            SS = [x * (l + 2) for x in S]
            if partialSum in SS:
                SSS = S + [0, i]
                RV[(partialSum // (l + 2)) - 1].append(SSS)
        for j in range(i - 2):
            RV[j].extend(H[j])
        H = RV
    return H

def hSetsCollectionsBuilder(H):
    HH = [h + [[]] for h in H]
    combinationList = [list(p) for p in product(*HH)]
    for B in combinationList:
        B[:] = [x for x in B if x]
    combinationList.remove([])
    return combinationList

def verifyProperty1(A, n):
    return set().union(*A) == set(range(n + 1))

def verifyProperty3(A):
    averages = {sum(hset) // len(hset) for hset in A}
    for i, j in combinations(range(len(A)), 2):
        if not (set(A[i]) & set(A[j])).issubset(averages):
            return False
    return True

def verifyProperty4(A):
    averages = [sum(hset) // len(hset) for hset in A]
    for i, j in combinations(range(len(A)), 2):
        if (averages[i] in set(A[j]) and averages[j] not in set(A[i])) or \
           (averages[j] in set(A[i]) and averages[i] not in set(A[j])):
            return False
    return True

def filterHSetsCollections(hSetsCollection, n):
    return [A for A in hSetsCollection if verifyProperty1(A, n) and verifyProperty4(A) and verifyProperty3(A)]

hSetsCollection=hSetsCollectionsBuilder(hSetsBuilder(n))
filtered=filterHSetsCollections(hSetsCollection, n)
print(f"n = {n}, {filtered}")
