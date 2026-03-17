# ГЕНЕРАЦИЯ ДАННЫХ ИБ (Этап 1)
import json
import random
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("🔄 Генерируем 1000 событий ИБ...")

signatures = [
    "Brute Force Attack", "SQL Injection", "XSS Attempt", "DDoS Attack", 
    "Malware Detection", "Phishing Attempt", "Privilege Escalation",
    "Data Exfiltration", "Buffer Overflow", "CSRF Attack"
]

data = []
base_time = datetime.now()
for i in range(1000):
    data.append({
        "timestamp": (base_time - timedelta(minutes=random.randint(0, 10000))).isoformat(),
        "source_ip": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
        "destination_ip": f"10.{random.randint(1,10)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "signature": random.choice(signatures),
        "severity": random.choice(["low", "medium", "high", "critical"]),
        "event_id": i
    })

# СОЗДАНИЕ JSON ФАЙЛА (Этап 1 ✅)
with open("events.json", "w") as f:
    json.dump(data, f, indent=2)

df = pd.DataFrame(data)
print(f"✅ Загружено {len(df)} событий в Pandas DataFrame!")
print("\n📋 Пример:")
print(df[['signature', 'severity']].head())
