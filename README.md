# FileSplitProject

***Description***

I need help with a task at work. Details below.	

Given file A with x number of records, split the file into y number of smaller files containing equal number of records.	

Notes:	
* Records are can only be identified by the line starting with "GROUP"	
* ALL text is surrounded by quotes ("")	
* All text is delimited by semicolon (;)	
* All text ends in a new line	
* All files end in a newline	
* All quotes and delimiters must remain intact. 	
* Just splitting the file as is, no other changes. Keeping order.	
* File may contain any number of records - primarily used for files with >10k records	
* Records lengths vary by number of (new)lines	
* All files will not have the same order of body text between records and may end with different text; the only marker of a new record is a line beginning with "GROUP"	
* Input_Text_Sample.txt holds the sample text. It holds 20050 'records' (Lines that start with group - all text after until the next 'Group' is part of the same 'record')	

Input: path to file 	

Output: N number of files each with y number of records	
	
EXAMPLE:	
Input_Text_Sample.txt holds 20050 records. I add the path to the sample text in the R script or Notebook. I enter the number of resulting files I want. The script determines how many records should approximately be in each file, some left over in the last file is okay. If I enter 5 for the number of output files I want, the script should return 5 files, each with 4010 records. If I enter 6 for the number of output files, the script should return 5 files with 3340 records and the 6th would hold the remainder.	
	
***Summary and 'pseudocode'***	

Count number of records	
Identify records	
Find the number of records (y) that would split closest to evenly to result in user defined number of output files with y records in each	

For line in notice_line:	
	For the number of lines in notice_line	
	If a line starts with "Group", Create an empty file	
	Name the empty file File_n , n for line number in notice_line	
	Put the line in the empty record	
	If the line is not group 	
	Add the line to the existing file	
	Until the file has the number of records that would make all resulting files have approximately y number of records, where y is the number of resulting files the user would like to have outputted	
