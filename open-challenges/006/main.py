import fileinput
import time

def exist_and_index(subsequence, matching_letter):
	for i, l in enumerate(subsequence):
		if l == matching_letter:
			return True, i
	return False, -1

def main():
	for line in fileinput.input():
		line = line.rstrip()
		if len(line) == 0:
			continue
		ls, rs = line.split(';')

		longest_subsequence = ""
		ls_len = len(ls)
		rs_len = len(rs)
		i = 0
		while i < ls_len:
			subsequence = ls[i:]

			for j in range(rs_len):
				matching_letter = rs[j:j+1]

				letter_exists, letter_index = exist_and_index(subsequence, matching_letter)
				print("checking {} againsg {}".format(subsequence, matching_letter))
				print(subsequence, matching_letter, letter_exists, letter_index)
				if letter_exists:
					longest_subsequence += matching_letter
					i = letter_index
					print("i is no {}, and tmp longest subsequence is now {}".format(str(i), longest_subsequence))
					time.sleep(2)
					break
				time.sleep(2)

			print("new longest subsequence: {}".format(longest_subsequence))
			i += 1


main()
