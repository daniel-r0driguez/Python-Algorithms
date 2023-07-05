# This is a string algorithm which searchs a pattern that may be in another string. Kind of like using CTRL-F on Google. 
def KMPSearch(pat, txt):
    N = len(txt)
    M = len(pat)

    lps = [0] * M
    computeLPSArray(pat, M, lps)
    print(lps)
    i = 0
    j = 0
    while (N - i) >= (M - j):
        print("Comparing pat[" + str(j) + "]: " + str(pat[j]) + " and txt[" + str(i) + "]: " + str(txt[i]))
        if pat[j] == txt[i]:
            i += 1
            j += 1
            print("They match so i = " + str(i) + " and j = " + str(j))
        if j == M:
            print("Found pattern at index " + str(i - j))
            print("(INDEX " + str(j - 1) + " of lps)", end="")
            j = lps[j - 1]
            print(" is what j is reset to, which is = " + str(j))
        elif i < N and pat[j] != txt[i]:
            print("mismatch between pat[" + str(j) + "]: " + str(pat[j]) + " and txt[" + str(i) + "]: " + str(txt[i]))
            if j != 0:
                print("(index " + str(j - 1) + " of lps)", end="")
                j = lps[j-1]
                print(" is what j is reset to, which is = " + str(j))
            else:
                i += 1
                print("j was equal to 0. i = " + str(i))

def computeLPSArray(pat, M, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def main():
    pattern = "m" # abababaaabababa
    string = "December 25, 2021"
    KMPSearch(pattern, string)
    return 0
main()