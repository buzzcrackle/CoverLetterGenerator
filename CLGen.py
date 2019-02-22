from docx import Document
import pyperclip
import sys

doc = Document('./CoverLetterTemplate.docx')

if len(sys.argv) == 4:
    entireBody = ""
    for p in doc.paragraphs:
        if 'COMPANY_NAME' in p.text:
            inline = p.runs
            for i in range(len(inline)):
                if 'COMPANY_NAME' in inline[i].text:
                    text = inline[i].text.replace('COMPANY_NAME', sys.argv[1])
                    inline[i].text = text
                if 'JOB_TITLE' in inline[i].text:
                    text = inline[i].text.replace('JOB_TITLE', sys.argv[2])
                    inline[i].text = text
        entireBody = entireBody + "\n" +  p.text

    pyperclip.copy(entireBody)
    print(entireBody)
    doc.save('./' + sys.argv[3] + '.docx')
else:
    print("3 arguments required, company name, job, your name")
