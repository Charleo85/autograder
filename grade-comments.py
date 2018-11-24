import pandas as pd
import re, csv, zipfile
import os.path

response_file = "response.csv"
grades_file = "input.csv"
gradebook_folder = "./MP2/"
output_file = gradebook_folder+"grades.csv"

response = pd.read_csv(response_file, header=0)
grades = pd.read_csv(grades_file, header=2, error_bad_lines=False)

def format_comment(s1, s2, rest):
	output = ""
	if s1 == 0: output += "-10 Wrong implementation for MAP.\n"
	if s2 == 0: output += "-10 Wrong implementation for NDCG@10.\n"
	for line in str(rest).rstrip().split('. '):
		if line == '' or line == ' ': continue
		output += line
		output += '.\n'
	return output

response["Comment"] = response["Comment"].fillna('').astype(str)

num_not_matched = 0
for idx, row in response.iterrows():
	computing_id = row["Computing ID"]
	grade = row["final score"]
	# print(row["Comment"])
	comment = format_comment(row["MAP"], row["NDCG@10"], row["Comment"] )

	# check if match succeed
	if computing_id is None or grade is None:
		print("row {} with email {}, score {}".format(idx, row["Email Address"], row["Score"]) )
		num_not_matched += 1

	if len(grades.loc[grades["ID"] == computing_id, "grade"].values) == 0: 
		print("computing id {} not found in gradebook".format(computing_id) )
		continue

	# update score
	grades.loc[grades["ID"] == computing_id, "grade"] = float(grade)

	# update comment
	last_name = grades.loc[grades["ID"] == computing_id]["Last Name"].values[0]
	first_name = grades.loc[grades["ID"] == computing_id]["First Name"].values[0]
	comment_filename = gradebook_folder + '{}, {}({})/comments.txt'.format(last_name, first_name, computing_id)
	if not os.path.isfile(comment_filename): 
		print("computing id {} not found in comment folder".format(computing_id) )
	else:
		with open(comment_filename, 'w') as f:
			f.write(comment)

print("%d rows unable to auto grade"%(num_not_matched))

with open(output_file, 'w') as out, open(grades_file, 'r') as inf:
	for i in range(2):
		out.write(inf.readline())
grades.to_csv(output_file, float_format='%.2f', index=False, quoting=csv.QUOTE_ALL, mode='a')