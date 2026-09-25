def transmission_time(data_bytes, bandwidth_bps, efficiency=1.0):
    """
    data_bytes    : 転送するデータ量（バイト）
    bandwidth_bps : 回線の伝送速度（ビット/秒）
    efficiency    : 伝送効率（0〜1。例: 50%なら0.5）
    戻り値         : 伝送時間（秒）
    """
    data_bits = data_bytes * 8            # バイト -> ビットに変換
    effective_bandwidth = bandwidth_bps * efficiency  # 伝送効率を反映した実効速度
    return data_bits / effective_bandwidth


def main():
    # 設問の条件で計算する
    DATA_BYTES = 12 * 10**6      # 12Mバイト
    BANDWIDTH_BPS = 1.5 * 10**6  # 1.5Mビット/秒
    EFFICIENCY = 0.5              # 伝送効率50%

    time_sec = transmission_time(DATA_BYTES, BANDWIDTH_BPS, EFFICIENCY)
    print(f"伝送時間: {time_sec:.0f}秒")
    print()

    print("=== 伝送効率を変えて比較する ===")
    for eff_percent in [25, 50, 75, 100]:
        eff = eff_percent / 100
        t = transmission_time(DATA_BYTES, BANDWIDTH_BPS, eff)
        print(f"伝送効率{eff_percent:3d}% -> {t:6.1f}秒")

    print()
    print("=== 選択肢の値と比較する ===")
    choices = {"ア": 16, "イ": 32, "ウ": 64, "エ": 128}
    for label, value in choices.items():
        mark = " <- 設問の条件（効率50%）での正解" if value == round(time_sec) else ""
        print(f"{label}: {value}秒{mark}")


if __name__ == "__main__":
    main()
