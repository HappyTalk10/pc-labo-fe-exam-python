def two_complement(n: int, bits: int = 8) -> int:
    """8ビット2進正数nに対して、2の補数で-nを求める"""
    mask = (1 << bits) - 1        # 11111111（XORに使うマスク）
    inverted = n ^ mask           # ① 全ビットを反転する（XOR）
    result = inverted + 1         # ② 1を加算する
    return result & mask          # 8ビットの範囲に収める


def main():
    print("=== 2の補数を求める ===")
    for n in [1, 5, 100, 127]:
        neg_n = two_complement(n)
        print(f"n = {n:3d} (0b{n:08b})  ->  -n = {neg_n:3d} (0b{neg_n:08b})")

    print()
    print("=== n + (-n) が8ビットでは0に戻ることを確認 ===")
    for n in [1, 5, 100, 127]:
        neg_n = two_complement(n)
        total = (n + neg_n) & 0xFF  # 8ビットに収めてから確認
        print(f"n={n:3d} + (-n)={neg_n:3d}  ->  8ビットでは {total}")


if __name__ == "__main__":
    main()
