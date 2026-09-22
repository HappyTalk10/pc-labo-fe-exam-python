# 04_message_ninshou

[#04_message_ninshou](#04_message_ninshou)

基本情報技術者試験問題に挑戦しよう！「メッセージ認証」の確認用コード。

記事: https://pc-labo.online/2024/01/19/try-fe-exam-sample-questions-32-message-authentication/

## 問題

メッセージ認証符号の利用目的に該当するものはどれか。

ア メッセージが改ざんされていないことを確認する。
イ メッセージの暗号化方式を確認する。
ウ メッセージの概要を確認する。
エ メッセージの秘匿性を確保する。

正解：ア

## このフォルダでやっていること

`mac_demo.py` は、「鍵とメッセージを連結してSHA-256でハッシュ化するだけ」の
簡易MAC関数を作り、次の3つを実際に値を出して確認する。

1. メッセージを1文字変えるとMACが変わる（改ざん検知）
2. 鍵が違うと正しいMACが作れない（なりすまし対策）
3. 同じ鍵・同じメッセージなら常に同じMACになる（検証が成立する理由）

最後に、Python標準ライブラリの `hmac` モジュール（本物のHMAC）でも同じ実験を行い、
自作の簡易MACとの違い（length extension攻撃への耐性など）に触れる。

## 実行方法

```bash
cd 04_message_ninshou
python3 mac_demo.py
```

## 実行結果の例

```
=== 基本のMAC計算 ===
元のメッセージ : 10000円を送金します
MAC            : 56c825134dbfd7f047f444b16e7d3ca5913bf84f60540e08aa5d1a8e6a49ffcc

=== 実験1: メッセージを改ざんしてみる ===
改ざん後メッセージ: 90000円を送金します
MAC              : 52bd7d350319a711278f8949f7fb668367bd9b1220e964662ee7d14bcb78add3
MACは一致する？   : False

=== 実験2: 鍵が違うとどうなるか（なりすまし対策） ===
別の鍵で計算したMAC: 7d6eff38d36d79dea2d044a4f552150947dfa2ae29658981f6b8c0235e1744a5
MACは一致する？    : False

=== 実験3: 同じ鍵・同じメッセージなら何度計算しても同じMAC ===
再計算したMAC: 56c825134dbfd7f047f444b16e7d3ca5913bf84f60540e08aa5d1a8e6a49ffcc
MACは一致する？: True

=== 本物のHMACとの比較 ===
HMAC(元メッセージ) : a5ac69186540f85cbc22a0992a2e32f52c1f664ef38dcebb6265787e88c25094
HMAC(改ざん後)     : c018bc7cfef689be241208f7dc533c0c75730ac307a9ba30994ee52376fcb70c
```

## 動作環境

- Python 3.x（標準ライブラリのみ使用: `hashlib`, `hmac`）
