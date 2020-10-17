import strutils
import sequtils

proc selectionSort(A: var seq, N:int): seq =
  var num_of_exchange:int = 0
  for i in 0..N-1:
    var minj = i
    for j in i..N-1:
      if A[j] < A[minj]:
        minj = j
        swap(A[i], A[minj])
        num_of_exchange += 1
  echo (num_of_exchange)
  return A

var A = readLine(stdin).split().map(parseInt)
let N:int = len(A)

let ans = selectionSort(A,N)
echo ans
