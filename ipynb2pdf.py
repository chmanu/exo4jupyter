import os
import nbformat
from nbconvert.exporters.webpdf import WebPDFExporter

def convert_notebook_to_pdf(notebook_path, output_path=None, hide_code=False):
    """
    Convert a Jupyter notebook to PDF using nbconvert library

    Args:
        notebook_path: Path to the notebook file
        output_path: Path for the output PDF file (optional)
        hide_code: If True, code cells will be hidden in the output (optional)

    Returns:
        Path to the generated PDF file
    """
    # Check if file exists
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook file '{notebook_path}' not found.")

    print(f"Converting notebook: {notebook_path} to PDF...")

    # Read the notebook
    with open(notebook_path, "r", encoding="utf-8") as file:
        notebook_content = nbformat.read(file, as_version=4)

    # Create the exporter with parameters
    pdf_exporter = WebPDFExporter(
        allow_chromium_download=True,
        exclude_input=hide_code  # This parameter hides code cells
    )

    # Export to PDF
    pdf_data, resources = pdf_exporter.from_notebook_node(notebook_content)

    # Determine output path
    if output_path is None:
        output_path = os.path.splitext(notebook_path)[0] + ".pdf"

    # Save the PDF
    with open(output_path, "wb") as file:
        file.write(pdf_data)

    print(f"✓ Conversion successful! PDF saved to: {output_path}")
    if hide_code:
        print("Note: Code cells have been hidden in the PDF.")
    return output_path

convert_notebook_to_pdf('NS_student_exo-1.ipynb', output_path='ex-1.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-2.ipynb', output_path='ex-2.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-3.ipynb', output_path='ex-3.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-4.ipynb', output_path='ex-4.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-5.ipynb', output_path='ex-5.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-6.ipynb', output_path='ex-6.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-7.ipynb', output_path='ex-7.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-8.ipynb', output_path='ex-8.pdf', hide_code=False)
convert_notebook_to_pdf('NS_student_exo-9.ipynb', output_path='ex-9.pdf', hide_code=False)
