# Python program for KMP Algorithm
# Time Complexity : O(m + n)
def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)

	lps = [0]*M
	j = 0 # index for pat[]

	# Calculate lps[] array
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print ("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1

txt = "ABABDABACDABCDABCABAB"
pat = "ABCDABCA"
KMPSearch(pat, txt)
