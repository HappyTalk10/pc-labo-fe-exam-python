"""
基本情報技術者試験問題に挑戦しよう！「メッセージ認証」
連動リポジトリ: pc-labo-fe-exam-python
記事: https://pc-labo.online/2024/01/19/try-fe-exam-sample-questions-32-message-authentication/

「メッセージ認証符号(MAC)は改ざん検知に使う」を、実際にMACの値を
計算しながら確認するスクリプト。

実行方法:
    python3 mac_demo.py
"""

import hashlib
import hmac as hmac_lib


def simple_mac(key: str, message: str) -> str:
    """鍵とメッセージを連結してSHA-256でハッシュ化する簡易MAC。

    ※ 仕組みの理解用の実装。実務ではこのまま使わず、
      標準ライブラリの hmac モジュール（本物のHMAC）を使うこと。
    """
    data = (key + message).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def real_hmac(key: str, message: str) -> str:
    """Python標準ライブラリのHMAC(HMAC-SHA256)。"""
    return hmac_lib.new(
        key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256
    ).hexdigest()


def main() -> None:
    key = "himitsu-no-kagi"
    message = "10000円を送金します"

    print("=== 基本のMAC計算 ===")
    mac1 = simple_mac(key, message)
    print("元のメッセージ :", message)
    print("MAC            :", mac1)
    print()

    print("=== 実験1: メッセージを改ざんしてみる ===")
    tampered = "90000円を送金します"
    mac2 = simple_mac(key, tampered)
    print("改ざん後メッセージ:", tampered)
    print("MAC              :", mac2)
    print("MACは一致する？   :", mac1 == mac2)
    print()

    print("=== 実験2: 鍵が違うとどうなるか（なりすまし対策） ===")
    wrong_key = "chigau-kagi-desu"
    mac3 = simple_mac(wrong_key, message)
    print("別の鍵で計算したMAC:", mac3)
    print("MACは一致する？    :", mac1 == mac3)
    print()

    print("=== 実験3: 同じ鍵・同じメッセージなら何度計算しても同じMAC ===")
    mac4 = simple_mac(key, message)
    print("再計算したMAC:", mac4)
    print("MACは一致する？:", mac1 == mac4)
    print()

    print("=== 本物のHMACとの比較 ===")
    print("HMAC(元メッセージ) :", real_hmac(key, message))
    print("HMAC(改ざん後)     :", real_hmac(key, tampered))


if __name__ == "__main__":
    main()
