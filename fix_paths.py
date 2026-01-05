#!/usr/bin/env python3
"""
Script to fix paths in notebooks to use relative paths from submission folder.
All CSV files are assumed to be in the submission folder.
"""

import json
import re
from pathlib import Path

def fix_paths_in_notebook(notebook_path):
    """Fix paths in a notebook file."""
    print(f"Processing: {notebook_path}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    changes_made = False
    
    # Patterns to replace
    replacements = [
        # Absolute paths
        (r'/Users/[^"\']+', '.'),
        (r'Y:\\[^"\']+', '.'),
        (r'C:\\[^"\']+', '.'),
        
        # Path construction patterns
        (r"notebook_dir\s*=\s*Path\.cwd\(\)\.resolve\(\)", "notebook_dir = Path('.').resolve()"),
        (r"data_path\s*=\s*\(notebook_dir\s*/\s*'\.\.'\s*/\s*['\"]Data['\"]\)\.resolve\(\)", "data_path = Path('.').resolve()"),
        (r"data_path\s*=\s*\(notebook_dir\s*/\s*'\.\.'\s*/\s*'\.\.'\s*/\s*['\"]Data['\"]\)\.resolve\(\)", "data_path = Path('.').resolve()"),
        (r"plots_dir\s*=\s*\(notebook_dir\s*/\s*'\.\.'\s*/\s*['\"]plots['\"]\)\.resolve\(\)", "plots_dir = Path('.').resolve()"),
        (r"DATA_DIR\s*=\s*r?[\"'][^\"']+[\"']", "DATA_DIR = '.'"),
        (r"DATA_DIR\s*=\s*\(notebook_dir\s*/\s*'\.\.'\s*/\s*['\"]Data['\"]\)\.resolve\(\)", "DATA_DIR = Path('.').resolve()"),
        
        # Base path patterns
        (r"base_path\s*=\s*Path\.cwd\(\)", "base_path = Path('.').resolve()"),
        (r"if base_path\.name == 'code':\s*base_path = base_path\.parent", "if False:  # Always use current directory"),
        (r"data_path\s*=\s*base_path\s*/\s*'Data'", "data_path = Path('.').resolve()"),
        (r"ecg_data_path\s*=\s*data_path\s*/\s*'time-series-project2025'", "ecg_data_path = Path('.').resolve() / 'time-series-project2025'"),
        
        # Output paths
        (r"'\.\./plots/", "'./plots/"),
        (r'"\.\./plots/', '"./plots/'),
        (r"'\.\./Data/", "'./"),
        (r'"\.\./Data/', '"./'),
        
        # Print statements with paths
        (r"print\(f[\"']Working directory:[^\"']+[\"']\)", "print(f'Working directory: {Path.cwd()}')"),
        (r"print\(f[\"']Data path:[^\"']+[\"']\)", "print(f'Data path: {data_path}')"),
        (r"print\(f[\"']Plots path:[^\"']+[\"']\)", "print(f'Plots path: {plots_dir}')"),
    ]
    
    # Process each cell
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                source_text = ''.join(source)
            else:
                source_text = source
            
            original_text = source_text
            
            # Apply replacements
            for pattern, replacement in replacements:
                source_text = re.sub(pattern, replacement, source_text)
            
            if source_text != original_text:
                changes_made = True
                # Update source
                cell['source'] = source_text.splitlines(keepends=True)
                if not cell['source'][-1].endswith('\n'):
                    cell['source'][-1] += '\n'
    
    if changes_made:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"  ✓ Fixed paths in {notebook_path.name}")
    else:
        print(f"  - No changes needed in {notebook_path.name}")
    
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
    print(f"✓ Made changes to {total_changes} notebooks")

if __name__ == '__main__':
    main()

