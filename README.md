# pc-labo-fe-exam-python

基本情報技術者試験（科目A）のサンプル問題を、Pythonの短いプログラムを通して理解するための学習用リポジトリである。

pc-labo.online の「基本情報技術者試験問題に挑戦しよう！」シリーズと連動しており、記事ごとにフォルダを分けて、確認用のPythonコードを置いている。

## 方針

- 1記事＝1フォルダとし、`01_xxx`, `02_xxx` のように連番で管理する
- 各フォルダには、問題の内容を確かめるための最小限のPythonスクリプトのみを置く
- 環境構築なしで、Python標準ライブラリのみで動くコードにする（`python3 xxx.py` で即実行できる状態を保つ）

## 記事内のコードについて（注意）

各記事内で紹介しているPythonプログラムは、説明のために、コードが変更・追加部分のみを示している場合があり、そのままコピーしても実行できないことがある。実際に動作する完全版のコードは、このリポジトリの各フォルダに置いている。

## フォルダ構成

| フォルダ | 記事タイトル | 内容 |
| --- | --- | --- |
| [01_2no_hosu](./01_2no_hosu) | [基本情報技術者試験問題に挑戦しよう！（２の補数）](https://pc-labo.online/2023/12/24/lets-try-fe-exam-questions-2no-hosu/) | XORとビット反転による2の補数の求め方をコードで確認する |
| [02_2bun_tansaku_gi](./02_2bun_tansaku_gi) | [基本情報技術者試験問題に挑戦しよう！「2分探索木」](https://pc-labo.online/2023/12/28/lets-try-fe-exam-sample-a-05-binary-search-tree/) | 木を組み立てて2分探索木の条件を満たすかをコードで判定する |
| [03_shinrichi](./03_shinrichi) | [基本情報技術者試験問題に挑戦しよう！「命題の真理値」](https://pc-labo.online/2023/12/26/lets-try-fe-exam-sample-a-03-shinrichi/) | P・Q・Rの全パターンを総当たりして条件を満たす真偽の組み合わせを確認する |
|[04_message_ninshou](./04_message_ninshou)	|[基本情報技術者試験問題に挑戦しよう！「メッセージ認証」](https://pc-labo.online/2024/01/19/try-fe-exam-sample-questions-32-message-authentication/)|MACの値を実際に計算し、改ざん・鍵違い・再計算で値がどう変わるかを確認する|

## 動作環境

- Python 3.x（標準ライブラリのみ使用）

## 関連ブログ

- [PC-LABO（つくって学ぶ体験型ブログ）](https://pc-labo.online/)
