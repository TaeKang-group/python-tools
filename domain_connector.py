import os

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
IP = "192.168.9.173"
DOMAIN = "taekang.admin"
ENTRY = f"{IP}\t{DOMAIN}"

def ensure_entry():
    try:
        with open(HOSTS_PATH, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            if any(DOMAIN in line for line in lines):
                print(f"[=] 이미 {DOMAIN} 항목이 존재합니다.")
                return
            f.write("\n" + ENTRY + "\n")
            print(f"[+] {ENTRY} 항목을 추가했습니다.")
    except PermissionError:
        print("[!] 관리자 권한으로 실행해야 합니다.")
    except Exception as e:
        print(f"[!] 오류 발생: {e}")

if __name__ == "__main__":
    ensure_entry()
