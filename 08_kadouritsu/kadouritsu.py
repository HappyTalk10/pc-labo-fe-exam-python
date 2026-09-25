import random


def theoretical_rate(a, b, c):
    client_ok = 1 - (1 - b) ** 3
    printer_ok = 1 - (1 - c) ** 2
    return a * client_ok * printer_ok


def simulate_system(a, b, c, trials):
    success = 0
    for _ in range(trials):
        server_up = random.random() < a
        client_up = any(random.random() < b for _ in range(3))
        printer_up = any(random.random() < c for _ in range(2))
        if server_up and client_up and printer_up:
            success += 1
    return success / trials


def main():
    random.seed(42)  # 実行するたびに結果が変わらないよう、乱数の種を固定する

    A = 0.99
    B = 0.9
    C = 0.95
    TRIALS = 100_000

    theory = theoretical_rate(A, B, C)
    sim = simulate_system(A, B, C, TRIALS)

    print(f"計算式による稼働率                     : {theory:.4f}")
    print(f"シミュレーションによる稼働率（試行{TRIALS}回）: {sim:.4f}")
    print(f"差                                      : {abs(theory - sim):.4f}")


if __name__ == "__main__":
    main()
