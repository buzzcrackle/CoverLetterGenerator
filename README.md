# Cover Letter Generator

Python script to generate cover letters. Made for when you send cover letters to many different companies and want to replace the names on each cover letter.

Built on Python version 2.7.15

## How to use:

1. In the same folder/directory as the python file, place a docx file with your cover letter template, named "CoverLetterTemplate.docx".

2. Replace the all occurances in the txt file of the name of the company with "COMPANY_NAME". Then, replace all occurances in the txt file of the job title with "JOB_TITLE".

3. Finally, you can run the script with the following command:
      
    python CLGen.py "INSERT COMPANY NAME" "INSERT JOB TITLE" "INSERT FILE NALE"

    Note: the file name DOES NOT include the .docx extension.

    Ex: python CLGen.py "Google" "Software Developer" "John_Doe_Cover_Letter"

4. There will be a .docx file created with the information given in the command. The cover letter text will be automatically copied onto your clipboard, but it will also be printed out onto the terminal.
