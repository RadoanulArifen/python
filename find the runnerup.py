n=int(input())
arr =(map(int, input().split()))

uni_scores = list(set(arr))
uni_scores.sort(reverse=True)
print(uni_scores[1])