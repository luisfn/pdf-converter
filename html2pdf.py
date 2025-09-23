#!/usr/bin/env python3
"""
HTML to PDF Converter CLI

A simple command-line tool to convert HTML files to PDF while preserving formatting.
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from weasyprint import HTML
except ImportError:
    print("Error: weasyprint is not installed. Install it with: pip install weasyprint")
    sys.exit(1)


def convert_html_to_pdf(input_file, output_file=None):
    """
    Convert HTML file to PDF.

    Args:
        input_file (str): Path to input HTML file
        output_file (str, optional): Path to output PDF file

    Returns:
        str: Path to the generated PDF file
    """
    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    if not input_path.suffix.lower() in ['.html', '.htm']:
        raise ValueError("Input file must be an HTML file (.html or .htm)")

    # Determine output file path
    if output_file is None:
        output_path = input_path.with_suffix('.pdf')
    else:
        output_path = Path(output_file)
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Convert HTML to PDF
        html_doc = HTML(filename=str(input_path))
        html_doc.write_pdf(str(output_path))

        return str(output_path)

    except Exception as e:
        raise RuntimeError(f"Failed to convert HTML to PDF: {e}")


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Convert HTML files to PDF while preserving formatting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.html                    # Creates input.pdf in same directory
  %(prog)s input.html -o output.pdf      # Creates output.pdf
  %(prog)s input.html -o /path/to/doc.pdf # Creates doc.pdf at specified path
        """
    )

    parser.add_argument(
        'input',
        help='Input HTML file path'
    )

    parser.add_argument(
        '-o', '--output',
        help='Output PDF file path (optional). If not specified, saves as input.pdf'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    try:
        if args.verbose:
            print(f"Converting {args.input} to PDF...")

        output_path = convert_html_to_pdf(args.input, args.output)

        print(f"Successfully converted to: {output_path}")

    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()