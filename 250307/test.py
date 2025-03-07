arr =  ['022']
string = ''
info = {'0':'1111', '2':'2222'}
for i in range(1):
    for c in arr[i]:
        string += info[c]
print(string)