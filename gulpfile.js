const gulp = require('gulp');
const shell = require('gulp-shell');
const path = require('path');

const opts = {
    shell: '/bin/bash',
    quiet: true
};
const root = path.join(__dirname, 'src');
const pdflatex = 'pdflatex --shell-escape -synctex=1 -interaction=nonstopmode book\n';

gulp.task('build', shell.task([
    `cd ${root}\n` +
    pdflatex +
    'makeindex book.idx -s StyleInd.ist\n' +
    'biber book\n' +
    'cd ../' +
    pdflatex +
    pdflatex
], opts));

gulp.task('watch', () => {
    gulp.watch('src/*.tex', shell.task([
        `cd ${root}\n` +
        pdflatex
    ], opts));
});

gulp.task('default', gulp.series('build', 'watch'));
