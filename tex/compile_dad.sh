#!/bin/bash
# LaTeX compilation script for DAD Project
# Compiles main.tex into dad_project.pdf
# Run from project root directory

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Get the project root directory (parent of tex/)
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

# Change to tex directory
cd "$SCRIPT_DIR"

OUTPUT_FILE="dad_project.pdf"
MAIN_FILE="main.tex"

echo "Compiling $MAIN_FILE into $OUTPUT_FILE..."

# First pass
echo "First pass..."
pdflatex -interaction=nonstopmode "$MAIN_FILE" > /dev/null 2>&1

# Second pass for cross-references
echo "Resolving cross-references..."
pdflatex -interaction=nonstopmode "$MAIN_FILE" > /dev/null 2>&1

# Third pass to ensure all references are resolved
echo "Final pass..."
pdflatex -interaction=nonstopmode "$MAIN_FILE" > /dev/null 2>&1

# Rename output to dad_project.pdf
if [ -f "main.pdf" ]; then
    mv "main.pdf" "$OUTPUT_FILE"
    echo "Compilation complete! Output: $OUTPUT_FILE"
else
    echo "Error: main.pdf was not generated. Check the log file for errors."
    exit 1
fi

# Clean up auxiliary files (keep .pdf and .tex files)
echo "Cleaning up auxiliary files..."
rm -f *.aux *.log *.out *.toc *.lof *.lot *.synctex.gz *.bbl *.blg \
    *.fdb_latexmk *.fls *.nav *.snm *.vrb

echo "Done!"


