pandoc -s answers.md \
  -o answers.pdf \
  -f markdown \
  -t pdf \
  --natbib \
  --pdf-engine=latexmk \
  --template=latex-ms.tex
