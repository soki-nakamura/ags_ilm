import strutils
import sequtils

proc bubbleSort(A:var seq, N:int):seq =
  var flag = true
  var num_of_exchange:int = 0
  var i = 0
  while flag:
    flag = false
    for j  in countdown(N-1,i+1):
      if A[j] < A[j-1]:
        swap(A[j], A[j-1])
        num_of_exchange += 1
        flag = true
    i += 1
  echo (num_of_exchange)
  return A

var A = readLine(stdin).split().map(parseInt)
let N:int = len(A)

let ans = bubbleSort(A,N)
echo ans
