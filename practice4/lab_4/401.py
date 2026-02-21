def count_up_to(n):
  count = 1
  while count <= n:
    yield count*count
    count += 1
n=int(input())
for i in count_up_to(n):
  print(i)