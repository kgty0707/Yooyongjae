import requests

url = f"http://localhost:8000/login"

data = {
    "user_name": "earthquake",
    "password": "pass123word123"
}

resp = requests.post(url=url, json=data)

print(f"status_code: {resp.status_code}")
print(f"content: {resp.content}")
print(f"headers: {resp.headers}")