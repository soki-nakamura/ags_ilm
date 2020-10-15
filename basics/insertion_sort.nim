import strutils
import sequtils

proc insertionSort(A: var seq, N:int): seq =
  for i in 1..N-1:
    var v = A[i]
    var j = i-1

    while j >= 0 and A[j] > v:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = v
    echo A
  return A


var A = readLine(stdin).split().map(parseInt)
let N:int = len(A)

let ans = insertionSort(A,N)
echo ans
