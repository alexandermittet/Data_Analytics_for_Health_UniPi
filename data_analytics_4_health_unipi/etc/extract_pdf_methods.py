"""
Extract time series methods from course PDF slides.

This script extracts text from PDF files to identify time series analysis methods
and approaches recommended in the course materials.
"""

import pdfplumber
import re
from pathlib import Path
from typing import List, Dict


def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extract all text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text as a string
    """
    text_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Processing {pdf_path.name} ({len(pdf.pages)} pages)...")
            
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    text_content.append(f"\n--- Page {page_num} ---\n")
                    text_content.append(text)
                    
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return ""
    
    return "\n".join(text_content)


def search_key_terms(text: str, terms: List[str]) -> Dict[str, List[str]]:
    """
    Search for key terms in the extracted text and return context.
    
    Args:
        text: Text to search
        terms: List of terms to search for
        
    Returns:
        Dictionary mapping terms to list of context lines
    """
    results = {}
    lines = text.split('\n')
    
    for term in terms:
        results[term] = []
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        
        for i, line in enumerate(lines):
            if pattern.search(line):
                # Get context (2 lines before and after)
                start = max(0, i - 2)
                end = min(len(lines), i + 3)
                context = '\n'.join(lines[start:end])
                results[term].append(context)
    
    return results


def extract_time_series_methods(text: str) -> Dict[str, any]:
    """
    Extract information about time series methods from text.
    
    Args:
        text: Extracted text from PDF
        
    Returns:
        Dictionary with extracted information
    """
    methods_info = {
        'preprocessing': [],
        'approximation': [],
        'similarity': [],
        'feature_extraction': [],
        'key_concepts': []
    }
    
    # Key terms to search for
    preprocessing_terms = [
        'preprocessing', 'pre-process', 'normalization', 'standardization',
        'scaling', 'smoothing', 'filtering', 'interpolation', 'resampling'
    ]
    
    approximation_terms = [
        'SAX', 'Symbolic Aggregate Approximation', 'PAA', 'Piecewise Aggregate Approximation',
        'DFT', 'Discrete Fourier Transform', 'DWT', 'Discrete Wavelet Transform',
        'approximation', 'compression', 'dimensionality reduction'
    ]
    
    similarity_terms = [
        'DTW', 'Dynamic Time Warping', 'Euclidean', 'similarity', 'distance',
        'correlation', 'alignment'
    ]
    
    feature_terms = [
        'feature extraction', 'statistical features', 'mean', 'variance', 'std',
        'min', 'max', 'trend', 'seasonality'
    ]
    
    # Search for each category
    methods_info['preprocessing'] = search_key_terms(text, preprocessing_terms)
    methods_info['approximation'] = search_key_terms(text, approximation_terms)
    methods_info['similarity'] = search_key_terms(text, similarity_terms)
    methods_info['feature_extraction'] = search_key_terms(text, feature_terms)
    
    # Extract sections that might contain key concepts
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if any(keyword in line.lower() for keyword in ['univariate', 'multivariate', 'time series', 'workflow', 'approach']):
            if len(line.strip()) > 10:  # Filter out very short lines
                methods_info['key_concepts'].append(line.strip())
    
    return methods_info


def main():
    """Main function to extract methods from PDFs."""
    # Define paths
    base_path = Path(__file__).parent.parent
    slides_path = base_path.parent / 'slides'
    output_path = base_path / 'code' / 'extracted_pdf_content'
    output_path.mkdir(exist_ok=True)
    
    # PDF files to process
    pdf_files = [
        '8_time_series_similarity_2024.pdf',
        '5-data-understanding_ts.pdf'
    ]
    
    all_results = {}
    
    for pdf_file in pdf_files:
        pdf_path = slides_path / pdf_file
        
        if not pdf_path.exists():
            print(f"Warning: {pdf_path} not found. Skipping...")
            continue
        
        print(f"\n{'='*60}")
        print(f"Processing: {pdf_file}")
        print(f"{'='*60}")
        
        # Extract text
        text = extract_text_from_pdf(pdf_path)
        
        if not text:
            print(f"No text extracted from {pdf_file}")
            continue
        
        # Save full text
        output_file = output_path / f"{pdf_file.replace('.pdf', '_full_text.txt')}"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved full text to: {output_file}")
        
        # Extract methods information
        methods_info = extract_time_series_methods(text)
        all_results[pdf_file] = {
            'full_text': text,
            'methods': methods_info
        }
        
        # Save methods summary
        summary_file = output_path / f"{pdf_file.replace('.pdf', '_methods_summary.md')}"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# Methods Summary: {pdf_file}\n\n")
            
            for category, results in methods_info.items():
                if category == 'key_concepts':
                    f.write(f"## Key Concepts\n\n")
                    for concept in results[:50]:  # Limit to first 50
                        f.write(f"- {concept}\n")
                    f.write("\n")
                else:
                    f.write(f"## {category.replace('_', ' ').title()}\n\n")
                    for term, contexts in results.items():
                        if contexts:
                            f.write(f"### {term}\n\n")
                            # Show first 3 contexts
                            for ctx in contexts[:3]:
                                f.write(f"```\n{ctx}\n```\n\n")
                    f.write("\n")
        
        print(f"Saved methods summary to: {summary_file}")
    
    # Create combined summary
    summary_file = output_path / "time_series_methods_summary.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# Time Series Methods Summary\n\n")
        f.write("This document summarizes the time series methods found in the course slides.\n\n")
        
        for pdf_file, data in all_results.items():
            f.write(f"## {pdf_file}\n\n")
            methods = data['methods']
            
            # List found methods
            f.write("### Found Methods:\n\n")
            
            if methods['approximation']:
                f.write("**Approximation Methods:**\n")
                for term in methods['approximation'].keys():
                    if methods['approximation'][term]:
                        f.write(f"- {term}\n")
                f.write("\n")
            
            if methods['similarity']:
                f.write("**Similarity Methods:**\n")
                for term in methods['similarity'].keys():
                    if methods['similarity'][term]:
                        f.write(f"- {term}\n")
                f.write("\n")
            
            if methods['preprocessing']:
                f.write("**Preprocessing Methods:**\n")
                for term in methods['preprocessing'].keys():
                    if methods['preprocessing'][term]:
                        f.write(f"- {term}\n")
                f.write("\n")
            
            if methods['feature_extraction']:
                f.write("**Feature Extraction Methods:**\n")
                for term in methods['feature_extraction'].keys():
                    if methods['feature_extraction'][term]:
                        f.write(f"- {term}\n")
                f.write("\n")
            
            f.write("\n---\n\n")
    
    print(f"\n{'='*60}")
    print(f"Summary saved to: {summary_file}")
    print(f"{'='*60}\n")
    print("Extraction complete!")


if __name__ == "__main__":
    main()


