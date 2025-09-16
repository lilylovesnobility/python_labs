n = int(input())
onsite = 0
remote = 0
for _ in range(n):
    surname, name, age, form = input().split()
    if form == "True":
        onsite += 1
    else:
        remote += 1
print(onsite, remote)
