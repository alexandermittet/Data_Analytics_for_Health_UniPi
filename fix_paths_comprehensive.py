#!/usr/bin/env python3
"""
Comprehensive script to fix all paths in notebooks to use relative paths.
All CSV files are assumed to be in the submission folder (current directory).
"""

import json
import re
from pathlib import Path

def fix_paths_in_notebook(notebook_path):
    """Fix paths in a notebook file."""
    print(f"Processing: {notebook_path.name}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    changes_made = False
    
    # Process each cell
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                source_text = ''.join(source)
            else:
                source_text = source
            
            original_text = source_text
            
            # Fix DATA_DIR patterns
            source_text = re.sub(
                r"DATA_DIR\s*=\s*\(notebook_dir\s*/\s*['\"]\.\.['\"]\s*/\s*['\"]\.\.['\"]\s*/\s*['\"]Data['\"]\)\.resolve\(\)",
                "DATA_DIR = Path('.').resolve()",
                source_text
            )
            source_text = re.sub(
                r"DATA_DIR\s*=\s*\(notebook_dir\s*/\s*['\"]\.\.['\"]\s*/\s*['\"]Data['\"]\)\.resolve\(\)",
                "DATA_DIR = Path('.').resolve()",
                source_text
            )
            
            # Fix OG_DATA_DIR patterns
            source_text = re.sub(
                r"OG_DATA_DIR\s*=\s*\(notebook_dir\s*/\s*['\"]\.\.['\"]\s*/\s*['\"]\.\.['\"]\s*/\s*['\"]Data['\"]\)\.resolve\(\)",
                "OG_DATA_DIR = Path('.').resolve()",
                source_text
            )
            source_text = re.sub(
                r"OG_DATA_DIR\s*=\s*\(notebook_dir\s*/\s*['\"]\.\.['\"]\s*/\s*['\"]Data['\"]\)\.resolve\(\)",
                "OG_DATA_DIR = Path('.').resolve()",
                source_text
            )
            
            # Fix output paths - change ../plots/ to ./plots/
            source_text = re.sub(r"'\.\./plots/", "'./plots/", source_text)
            source_text = re.sub(r'"\.\./plots/', '"./plots/', source_text)
            source_text = re.sub(r"'\.\./plots", "'./plots", source_text)
            source_text = re.sub(r'"\.\./plots', '"./plots', source_text)
            
            # Fix paths in print statements that reference old absolute paths
            # Remove print statements that show old paths (they'll be regenerated)
            source_text = re.sub(
                r"print\(f[\"']\s*Correlation matrix saved to:[^\"']*[\"']\)",
                "# Path updated to relative",
                source_text
            )
            source_text = re.sub(
                r"print\(f[\"']\s*Boxplots saved to:[^\"']*[\"']\)",
                "# Path updated to relative",
                source_text
            )
            source_text = re.sub(
                r"print\(f[\"']\s*Clustered data saved to:[^\"']*[\"']\)",
                "# Path updated to relative",
                source_text
            )
            
            # Fix os.path.join with DATA_DIR to use Path
            # Keep os.path.join but ensure DATA_DIR is relative
            # Actually, os.path.join('.', 'file.csv') works fine, so leave those
            
            # Fix data_dir parameter in function calls
            source_text = re.sub(
                r"data_dir\s*=\s*DATA_DIR",
                "data_dir = Path('.')",
                source_text
            )
            
            # Fix paths that use f-strings with old absolute paths
            source_text = re.sub(
                r"f[\"']\{[^}]*\}Y:\\\\[^\"']*[\"']",
                "f'{Path.cwd()}'",
                source_text
            )
            
            # Fix any remaining absolute path references in string outputs
            # These are usually in output cells, but we can clean source cells
            source_text = re.sub(
                r"Y:\\\\[^\"'\s]*",
                ".",
                source_text
            )
            
            if source_text != original_text:
                changes_made = True
                # Update source
                cell['source'] = source_text.splitlines(keepends=True)
                if cell['source'] and not cell['source'][-1].endswith('\n'):
                    cell['source'][-1] += '\n'
    
    if changes_made:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"  ✓ Fixed additional paths")
    else:
        print(f"  - No additional changes needed")
    
    return changes_made

def main():
    """Main function to process all notebooks."""
    submission_dir = Path(__file__).parent
    
    # Find all notebooks
    notebooks = list(submission_dir.rglob('*.ipynb'))
    
    print(f"Found {len(notebooks)} notebooks to process\n")
    
    total_changes = 0
    for notebook_path in notebooks:
        if fix_paths_in_notebook(notebook_path):
            total_changes += 1
    
    print(f"\n✓ Processed {len(notebooks)} notebooks")
    print(f"✓ Made additional changes to {total_changes} notebooks")

if __name__ == '__main__':
    main()

