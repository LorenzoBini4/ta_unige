import subprocess

tex_file = 'handout_tp1.tex'

# Compile the LaTeX file to generate the PDF
subprocess.run(['pdflatex', tex_file])

# Rename the generated PDF file
subprocess.run(['mv', tex_file.replace('.tex', '.pdf'), 'handout_tp1.pdf'])

