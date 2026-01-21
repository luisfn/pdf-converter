# HTML to PDF Converter CLI

A simple command-line tool to convert HTML files to PDF while preserving formatting.

## Features

- Preserves HTML formatting, CSS styles, colors, and layout
- Automatic output naming (same name as input file with .pdf extension)
- Custom output path support
- Verbose mode for detailed output
- Works with complex HTML documents including tables, images, and styling

## Requirements

- Python 3.7+
- WeasyPrint library
- System dependencies (automatically installed on macOS with Homebrew)

## Installation

### macOS

1. Install system dependencies:
   ```bash
   brew install gobject-introspection libffi pango
   ```

2. Set up the project:
   ```bash
   cd pdf-converter
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Docker (Recommended for macOS issues)

If you encounter dependency issues on macOS (like `OSError: cannot load library 'libgobject-2.0-0'`), use Docker to run the converter in a consistent environment.

#### 1. Build the Docker Image
Run this once to create the converter image:
```bash
docker build -t html2pdf .
```

#### 2. Run the Converter
Use this command to convert your files. It mounts your current folder so the container can access your HTML files:
```bash
# Example: Convert resume_english.html
docker run --rm -v "$(pwd):/app" html2pdf resume_english.html
```

The PDF will be generated in your current directory.

## Usage

### Basic Usage

Convert HTML to PDF with same name:
```bash
./html2pdf.py input.html
```

This creates `input.pdf` in the same directory.

### Custom Output

Specify custom output path:
```bash
./html2pdf.py input.html -o /path/to/output.pdf
```

### Verbose Mode

Enable detailed output:
```bash
./html2pdf.py input.html --verbose
```

### Full Example

```bash
# Activate virtual environment
source venv/bin/activate

# Convert with custom output and verbose mode
python3 html2pdf.py test.html -o converted/document.pdf --verbose
```

## Examples

### Converting a simple HTML file:
```bash
./html2pdf.py document.html
# Creates: document.pdf
```

### Converting with custom output:
```bash
./html2pdf.py report.html -o reports/monthly-report.pdf
# Creates: reports/monthly-report.pdf
```

## Features Preserved

- **Typography**: Fonts, sizes, weights, styles
- **Colors**: Text colors, backgrounds, borders
- **Layout**: Margins, padding, positioning
- **Tables**: Borders, colors, cell formatting
- **Images**: Embedded images and graphics
- **Lists**: Ordered and unordered lists with styling
- **CSS Styling**: Most CSS properties are preserved

## Troubleshooting

### macOS Issues

If you encounter library loading errors, ensure all dependencies are installed:

```bash
# Install required system libraries
brew install gobject-introspection libffi pango cairo glib

# Restart terminal and reactivate virtual environment
source venv/bin/activate
```

### Python Path Issues

Make sure you're using the virtual environment:
```bash
which python3  # Should show venv/bin/python3
```

## File Structure

```
pdf-converter/
├── html2pdf.py          # Main CLI script
├── requirements.txt     # Python dependencies
├── venv/               # Virtual environment
├── test.html           # Sample HTML file
├── test.pdf            # Generated PDF (example)
└── README.md           # This file
```