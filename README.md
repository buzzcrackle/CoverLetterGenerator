# Cover Letter Generator

Python script to generate cover letters. Made for when you send cover letters to many different companies and want to replace the names on each cover letter.

Built on Python version 2.7.15

## How to use:

1. In the same folder/directory as the python file, place a txt file with your cover letter template, named "coverletter.txt".

2. Replace the all occurances in the txt file of the name of the company with the following text, "COMPANY_NAME". Then, replace all occurances in the txt file of the job title with the following text, "JOB_TITLE".

3. Finally, you can run the script with the following command:
	
	python CLGen.py "INSERT COMPANY NAME" "INSERT JOB TITLE"
   
   For example:
   
   	python CLGen.py "Google" "Software Engineer"

4. The cover letter text will be automatically copied onto your clipboard, but it will also be printed out onto the terminal.
