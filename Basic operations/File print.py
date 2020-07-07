import sys
temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print('hello')
print(1,2,3)
sys.stdout.close()
sys.stdout = temp

print('back here')
print(open('log.txt').read())

log = open('log.txt','a')
print('world', file=log)
print('happy')

log.close()