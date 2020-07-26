import sys

print('versie: ' + str(len(sys.version_info)))
print('-----')
for i in range(len(sys.version_info)):
    print('versie: ' + str(sys.version_info[i]))
print('-----')
print(*sys.version_info)
