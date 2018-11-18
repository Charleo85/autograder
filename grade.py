import pandas as pd
import re, csv, zipfile

response_file = "response.csv"
grades_file = "input.csv"
output_file = "grades.csv"

response = pd.read_csv(response_file, header=0)
grades = pd.read_csv(grades_file, header=2, error_bad_lines=False)

email2id_regex = re.compile('(\w+)@virginia.edu')
score2grade_regex = re.compile('(\d+)/(\d+)')

def email2id(email):
	matched = email2id_regex.match(email.strip().lower())
	if matched: return matched.group(1)
	return None

def score2grade(score):
	matched = score2grade_regex.match(score.replace(' ', '').strip())
	if matched: return matched.group(1)
	return None

num_not_matched = 0
for idx, row in response.iterrows():
	computing_id = email2id(row["Email Address"])
	grade = score2grade(row["Score"])

	# check if match succeed
	if computing_id is None or grade is None:
		print("row {} with email {}, score {}".format(idx, row["Email Address"], row["Score"]) )
		num_not_matched += 1

	# update score
	grades.loc[grades["ID"] == computing_id, "grade"] = float(grade)

print("%d rows unable to auto grade"%(num_not_matched))

with open(output_file, 'w') as out, open(grades_file, 'r') as inf:
	for i in range(2):
		out.write(inf.readline())
grades.to_csv(output_file, float_format='%.2f', index=False, quoting=csv.QUOTE_ALL, mode='a')

with zipfile.ZipFile('grade.zip', 'w') as f:
    f.write(output_file)