import sys
input = sys.stdin.readline

string_A = '0' + input().rstrip()
string_B = '0' + input().rstrip()

LCS = [[0]*len(string_B) for i in range(len(string_A))]

for i in range(len(string_A)):
    for j in range(len(string_B)):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[len(string_A)-1][len(string_B)-1])