#!/bin/bash
# LaTeX compilation script
# Compiles Chapters 3, 5, and 6 (Time Series chapters) for preview

TEMP_FILE="preview_timeseries_chapters.tex"
OUTPUT_FILE="preview_timeseries_chapters.pdf"

echo "Creating temporary LaTeX file for Chapters 3, 5, and 6 preview..."

# Create a minimal document with Chapters 3, 5, and 6
cat > "$TEMP_FILE" << 'EOF'
\documentclass[11pt,a4paper]{report}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{geometry}
\usepackage{subcaption}
\usepackage{float}

% Page geometry
\geometry{
    a4paper,
    margin=2.5cm,
    headheight=15pt
}

% Title information
\title{Time Series Analysis Preview: Chapters 3, 5, and 6}
\author{Preview}
\date{\today}

\begin{document}

%\maketitle

%\tableofcontents
%\listoffigures
%\listoftables

% Allow chapters to start on same page if space permits (for preview only)
% Remove this line for final document to maintain standard chapter formatting
\let\cleardoublepage\clearpage

% Include Chapters 3, 5, and 6
\include{code/3.1_timeseries_chapter}
\include{code/5_ts_clustering_chapter}
\include{code/6_ts_classification_chapter}

\end{document}
EOF

echo "Compiling Chapters 3, 5, and 6 preview..."
pdflatex -interaction=nonstopmode "$TEMP_FILE" > /dev/null 2>&1
echo "First pass complete. Resolving cross-references..."
pdflatex -interaction=nonstopmode "$TEMP_FILE" > /dev/null 2>&1
echo "Compilation complete! Output: $OUTPUT_FILE"

# Clean up temporary LaTeX file and all auxiliary files
rm -f "$TEMP_FILE" \
    preview_timeseries_chapters.aux \
    preview_timeseries_chapters.log \
    preview_timeseries_chapters.out \
    preview_timeseries_chapters.toc \
    preview_timeseries_chapters.lof \
    preview_timeseries_chapters.lot \
    preview_timeseries_chapters.synctex.gz \
    code/*.aux \
    code/*.log \
    code/*.out \
    code/*.toc \
    code/*.lof \
    code/*.lot \
    code/*.synctex.gz \
    *.aux \
    *.log \
    *.out \
    *.toc \
    *.lof \
    *.lot \
    *.synctex.gz \
    *.bbl \
    *.blg \
    *.fdb_latexmk \
    *.fls \
    *.nav \
    *.snm \
    *.vrb

echo "Cleanup complete. All temporary files removed."

