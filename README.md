# autograder
A python3 script to bulk upload score from csv form to collab

# brief instruction
1. rename the csv file with score to `response.csv`
2. download the skeleton gradebook from collab:
*"Grade > Download All > Grade file (file at top level of archive) > CSV format, file grades.csv"*.
select *"Feedback comments (comments.txt file if available in student's folder. Comments are put into the Instructor Comments field for each student's submission)"* if you also need to upload comments
Also select *"Include students who have not yet submitted"* so it skeleton will include all students
3. `unzip && cp grades.csv {scipt_dir}/input.csv` 
4. `python3 grade.py ## if needs comments use grade-comment.py`
5. upload the graded file `grade.zip` to collab:
*Grade > Upload All > Grade file (file at top level of archive) > CSV format, file grades.csv*
select *"Feedback comments (comments.txt file if available in student's folder. Comments are put into the Instructor Comments field for each student's submission)"* if you also need to upload comments

