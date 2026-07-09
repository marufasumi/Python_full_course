"""
Q101. File Type Check

Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx,
or .txt and print the file type.
"""

filename = "report.mp3"
if filename.endswith(".pdf") or filename.endswith(".docx") or filename.endswith(".txt"):
    print("Valid file")
else:
    print("Invalid file")
