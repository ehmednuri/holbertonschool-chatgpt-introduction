# 1. Kodu yenidən və təmiz şəkildə yazaq
echo '#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(factorial(int(sys.argv[1])))' > factorial.py

# 2. GİT-Ə ƏMR VERİRİK Kİ, BU FAYLI "İCRA OLUNAN" KİMİ QEYD ETSİN
git update-index --chmod=+x factorial.py

# 3. GÖNDƏRİRİK
git add factorial.py
git commit -m "Final permission fix with update-index"
git push
