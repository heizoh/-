x = input("整数xを入力してください。")
y = input("整数yを入力してください。")
z = input("整数zを入力してください。")
i = 0
a = []
if int(x)%2 == 1:
    a.append(int(x))
    i = i +1
if int(y)%2 ==1:
    a.append(int(y))
    i = i +1
if int(z)%2 == 1:
    a.append(int(z))
    i = i +1
if i == 3:
    ans = max(a[0],a[1],a[2])
elif i == 2:
    ans = max(a[0],a[1])
elif i ==1:
    ans = a[0]
else:
    print('入力された数字はすべて偶数でした。')
    exit
print('最大値は' + str(ans) + 'です。')