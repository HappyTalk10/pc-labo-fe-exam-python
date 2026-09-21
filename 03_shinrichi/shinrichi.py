from itertools import product

def check(P, Q, R):
    cond1 = P                       # 命題Pの真理値は真
    cond2 = (not P) or Q            # (not P) or Q が真
    cond3 = (not Q) or R            # (not Q) or R が真
    return cond1 and cond2 and cond3

print("P     Q     R     -> 条件をすべて満たすか")
for P, Q, R in product([True, False], repeat=3):
    ok = check(P, Q, R)
    mark = "◯" if ok else ""
    print(f"{str(P):<5} {str(Q):<5} {str(R):<5} {mark}")

print()
print("=== 条件をすべて満たす組み合わせ ===")
for P, Q, R in product([True, False], repeat=3):
    if check(P, Q, R):
        print(f"P={P}, Q={Q}, R={R}")
