import spacy
!pip install docx2txt
import docx2txt
!pip install PyPDF2
import PyPDF2

#!pip install -U spacy
!python -m spacy download en_core_web_md
#!python -m spacy download ar_core_web_md

# Load the English SpaCy model
nlp_en = spacy.load("en_core_web_md")
# Upload the file
filepath = input("Please enter the file path:")

# Get the file extension
extension = filepath.split(".")[-1].lower()

# Open and read the file based on its extension
if extension == "txt":
    with open(filepath, 'r') as file:
        story = file.read()
elif extension == "docx":
    story = docx2txt.process(filepath)
elif extension == "pdf":
    pdf_file = open(filepath, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    story = ""
    for page in range(len(pdf_reader.pages)):
        story += pdf_reader.pages[page].extract_text()
    pdf_file.close()
else:
    print(f"Sorry, {extension} files are not supported.")
    exit()

# Process the text with SpaCy
doc = nlp(story)

# Create a set to store the named characters
characters = set()

# Iterate over the entities in the Doc and add named characters to the set (English)
for ent in doc.ents:
     if ent.label_ == "PERSON":
        characters.add(ent.text)

# Iterate over the entities in the Doc and add named characters to the set (Arabic)
for ent in doc.ents:
     if ent.label_ == "PER":
        characters.add(ent.text)

Num = 1
print("Characters:")
for Char in characters:
    print(str(Num) + ": " + Char)
    Num += 1
