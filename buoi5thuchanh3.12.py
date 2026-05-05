from collection import Counter

S1 = input("Emter S1: ")
S2 = input("Enter S2: ")

counter1 = Counter(S1)
counter2 = Counter(S2)

#a)
common_Chars = counter1 & counter2
print(f"\na) Character in both S1 and S2: {set(common_Chars.key())}")

#b
only_in_s1 = counter1 - counter2
only_in_s2 = counter2 - counter1

print(f"\nb) Count of chars only in S1 (not in S2): {len(only_in_s1)}")
print(f"   Count of chars only in S2 (not in S1): {len(only_in_s2)}")

#c
exclusive_s1 = {ch for ch in s1 if ch not in counter2}  # in S1, not in S2
exclusive_s2 = {ch for ch in s2 if ch not in counter1}  # in S2, not in S1

print(f"\nc) Chars only in S1: {exclusive_s1 if exclusive_s1 else 'None'}")
print(f"   Chars only in S2: {exclusive_s2 if exclusive_s2 else 'None'}")