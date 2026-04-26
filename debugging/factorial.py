# 1. Düzgün kodu fayla yazırıq
cat <<EOF > factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(factorial(int(sys.argv[1])))
EOF

# 2. Fayla icra icazəsi (chmod +x) veririk
chmod +x factorial.py

# 3. Dəyişiklikləri GitHub-a push edirik
git add factorial.py
git commit -m "Fix logic and execution permissions"
git push
