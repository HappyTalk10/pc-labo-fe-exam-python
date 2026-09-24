import socket
import threading

SERVER_PORT = 8080  # 80番の代わりに、特権なしで使えるポートを使う


def run_server(ready_event, result):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", SERVER_PORT))
    server_sock.listen(1)
    ready_event.set()  # 準備完了をクライアントに知らせる

    conn, _ = server_sock.accept()
    result["server_local"] = conn.getsockname()    # サーバー自身のアドレスとポート
    result["server_remote"] = conn.getpeername()   # 接続してきたクライアントのアドレスとポート
    conn.close()
    server_sock.close()


def run_client(ready_event, result):
    ready_event.wait()  # サーバーの準備ができるまで待つ
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("localhost", SERVER_PORT))
    result["client_local"] = client_sock.getsockname()   # クライアント自身のアドレスとポート（OSが自動割り当て）
    result["client_remote"] = client_sock.getpeername()  # 接続先のサーバーのアドレスとポート
    client_sock.close()


def main():
    ready_event = threading.Event()
    result = {}

    server_thread = threading.Thread(target=run_server, args=(ready_event, result))
    server_thread.start()

    run_client(ready_event, result)
    server_thread.join()

    print("=== クライアント（PC）側から見た通信 ===")
    print(f"送信元（自分のポート、OSが割り当て）: {result['client_local']}")
    print(f"宛先（サーバーのポート）        : {result['client_remote']}")
    print()
    print("=== サーバー（Webサーバー）側から見た通信 ===")
    print(f"自分のポート（＝クライアントからの宛先）: {result['server_local']}")
    print(f"クライアントのポート（＝クライアントの送信元）: {result['server_remote']}")
    print()
    print("=== 戻りのパケットで使われるポート番号 ===")
    print(f"送信元ポート（サーバー自身）: {result['server_local'][1]}")
    print(f"宛先ポート（クライアントのポート）: {result['server_remote'][1]}")


if __name__ == "__main__":
    main()
