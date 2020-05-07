# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import sys
from docx import Document


# %%
def convert(doc_name):
    doc = Document(f'{doc_name}.docx')
    paragraph_break = "\n"
    doc_content = ""
    for p in doc.paragraphs:
        doc_content += f"{p.text}{paragraph_break}"

    with open(f'{doc_name}.md', 'w') as file:
        file.write(doc_content)


# %%
terminal_prompt = sys.argv
filenames = terminal_prompt[1:]
for f in filenames:
    convert(f)
