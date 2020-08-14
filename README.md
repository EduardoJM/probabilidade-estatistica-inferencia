# Introdução

## Compilando

Atualmente, o processo pra compilar o arquivo consiste de executar os comandos shell diretamente, na seguinte ordem:

### Compilando completo

```bash
cd src
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
makeindex book.idx -s StyleInd.ist
biber book
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
```

### Compilando rápido

Para uma compilação rápida, após a compilação completa, utiliza-se apenas o comando pdflatex

```bash
cd src
pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book
```

### Gulp

Utilizando o **NodeJS** e o **gulp**, pode-se "automatizar" o processo, com as tarefas do arquivo `gulpfile.js`.
