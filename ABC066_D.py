from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="066"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc077_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  mod=10**9+7
  n=int(input())
  A=list(map(int,input().split()))
  tmp=[-1]*n
  for i in range(n+1):
    if tmp[A[i]-1]==-1: tmp[A[i]-1]=i
    else: m=i-tmp[A[i]-1]-1
  F=[1]
  for i in range(n+1):
      F.append(F[-1]*(i+1)%mod)
  I=[pow(F[i],mod-2,mod) for i in range(n+2)]
  for k in range(n+1):
    ans=(F[n+1]*I[k+1]*I[n-k])%mod
    if k<=n-m-1: ans=(ans-F[n-m-1]*I[k]*I[n-m-k-1])%mod
    print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])