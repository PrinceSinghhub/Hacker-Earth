Str = input()
ans = ""
for i in Str:
    if i.isupper():
        ans+=i.lower()
    if i.islower():
        ans+=i.upper()
print(ans)