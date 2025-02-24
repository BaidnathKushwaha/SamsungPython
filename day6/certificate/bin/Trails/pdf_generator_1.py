import os
from weasyprint import HTML

# Function to wrap HTML content with a template
def wrap_with_template(content, orientation="landscape"):
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Certificate</title>
            <link href="https://fonts.googleapis.com/css2?family=Futura:wght@700&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Helvetica:wght@300&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Merriweather&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
            <style>
                @page {{
                    size: A4 {orientation};
                    margin: 1.5cm;
                }}
                body, html {{
                    margin: 0;
                    padding: 0;
                    font-family: 'Helvetica', sans-serif;
                    background-color: #f5f5f5;
                }}
                .border-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 98vh;
                    background-color: #ffffff;
                    border: 20px solid #ffffff;
                }}
                .certificate {{
                    width: 100%;
                    max-width: 1400px;
                    padding: 50px;
                    background-color: white;
                    border: 2px solid black;
                    background-image: url('D:/final/bg4.png');
                    background-size: cover;
                    background-position: center;
                }}
                h1 {{
                    font-family: 'Futura', sans-serif;
                    font-size: 48px;
                    text-align: center;
                    letter-spacing: 2px;
                }}
                h2 {{
                    font-family: 'Merriweather', serif;
                    font-size: 28px;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .details {{
                    font-size: 2rem;
                    text-align: center;
                    font-family: 'Times New Roman', serif;
                }}
                .footer {{
                    font-size: 14px;
                    text-align: center;
                    margin-top: 30px;
                }}
                .footer .contact {{
                    font-weight: bold;
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>
            <div class="border-container">
                <div class="certificate">
                    <div class="text-center mb-4">
                        <img src="D:/final/mtd.png" alt="Organization Logo" width="200">
                        <p style="font-family: 'Helvetica', sans-serif; font-size: 14px;">www.mtdn.co.in</p>
                    </div>
                    <h1>CERTIFICATE</h1>
                    <h2>of Internship to</h2>
                    {content}  <!-- Dynamic content from HTML file -->
                </div>
            </div>
        </body>
        </html>
    """

# Function to generate a PDF from an HTML string
def html_to_pdf(html_content, output_path):
    try:
        HTML(string=html_content).write_pdf(output_path)
        print(f"Generated PDF: {output_path}")
    except Exception as e:
        print(f"Error generating PDF: {e}")

# Function to process all HTML files in a directory
def process_html_directory(input_dir, output_dir, orientation="landscape"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".html"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.pdf")

            # Read individual HTML file content
            with open(input_path, "r", encoding="utf-8") as file:
                content = file.read()  # Raw content of the HTML file

            # Wrap raw content in the full certificate template
            wrapped_content = wrap_with_template(content, orientation)

            # Convert to PDF
            html_to_pdf(wrapped_content, output_path)

# Main execution
if __name__ == "__main__":
    input_directory = "D:/final/certificates"
    output_directory = "D:/final/pdf_certificates"
    orientation = "landscape"

    # Process all HTML files and generate PDFs
    process_html_directory(input_directory, output_directory, orientation)