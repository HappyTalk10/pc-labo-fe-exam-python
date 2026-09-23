import sqlite3


def main():
    conn = sqlite3.connect(":memory:")  # ファイルを作らず、メモリ上にDBを作る
    cur = conn.cursor()

    # --- 3. SQLiteでテーブルを作る（設問の表Xをそのまま再現） -------------------
    cur.execute("""
    CREATE TABLE 商品 (
        商品番号 TEXT PRIMARY KEY,
        商品名   TEXT NOT NULL,
        価格     INTEGER NOT NULL,
        数量     INTEGER NOT NULL
    )
    """)

    # --- 5. データを登録する（表Xの5行） ----------------------------------------
    cur.executemany(
        "INSERT INTO 商品 (商品番号, 商品名, 価格, 数量) VALUES (?, ?, ?, ?)",
        [
            ("A01", "カメラ",   13000, 20),
            ("A02", "テレビ",   58000, 15),
            ("B01", "冷蔵庫",   65000, 8),
            ("B05", "洗濯機",   48000, 10),
            ("B06", "乾燥機",   35000, 5),
        ],
    )

    # 結合の練習用に、仕入先テーブルを追加する（設問には無い、発展的な例）
    cur.execute("""
    CREATE TABLE 仕入先 (
        商品番号 TEXT PRIMARY KEY,
        仕入先名 TEXT NOT NULL
    )
    """)
    cur.executemany(
        "INSERT INTO 仕入先 (商品番号, 仕入先名) VALUES (?, ?)",
        [
            ("A01", "サンプル商会"),
            ("A02", "サンプル商会"),
            ("B01", "家電卸センター"),
            ("B05", "家電卸センター"),
            ("B06", "家電卸センター"),
        ],
    )
    conn.commit()

    def show(title, rows):
        print(f"=== {title} ===")
        for row in rows:
            print(row)
        print()

    # --- 6. 射影をSQLで試す（設問の表Yを再現） ----------------------------------
    cur.execute("SELECT 商品番号, 数量 FROM 商品")
    show("射影：商品番号と数量だけを取り出す（表Yと同じになるはず）", cur.fetchall())

    # --- 7. 選択をSQLで試す ------------------------------------------------------
    cur.execute("SELECT * FROM 商品 WHERE 価格 >= 50000")
    show("選択：価格が50,000円以上の商品だけを取り出す", cur.fetchall())

    # --- 8. 結合をSQLで試す ------------------------------------------------------
    cur.execute("""
    SELECT 商品.商品名, 仕入先.仕入先名
    FROM 商品
    JOIN 仕入先 ON 商品.商品番号 = 仕入先.商品番号
    """)
    show("結合：商品名と仕入先名をつなげる", cur.fetchall())

    conn.close()


if __name__ == "__main__":
    main()
