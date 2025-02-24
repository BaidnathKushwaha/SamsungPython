import os
from jinja2 import Template
from weasyprint import HTML
import base64

# Function to encode images to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

# Updated A4-sized HTML template with smaller font size for placeholders
html_template = """
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
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap" rel="stylesheet">

    <style>
        @page {
            size: A4 landscape;
            margin: 0;
        }
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            background-color: #f5f5f5;
        }
        .border-container {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 20px solid #ffffff;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .certificate {
            width: 100%;
            height: 100%;
            background-image: url('{{ background_image_base64 }}');
            background-size: cover;
            background-position: center;
            text-align: center;
            color: #fff;
            box-sizing: border-box;
            padding: 30px;
        }
        .header img { 
        margin-bottom: -10px; /* Adjust this value to move it upwards */ 
        }
        h1 {
            font-family: 'Futura', sans-serif;
            font-size: 48px;
            margin: 0;
            font-weight: bold;
            letter-spacing: 2px;
            color: #000;
        }
        h3 {
            font-family: 'Merriweather', serif;
            font-size: 1.5em;
            color: #C0C0C0;
            margin: 10px 0;
        }
        p {
            font-size: 1.2em;
            margin: 5px 0;
            color: #000000;
        }
        .details {
            font-family: 'Times New Roman', serif;
            font-size: 1.8em; /* Increase font size */
            color: #000000;
            text-align: center;
            margin-top: 30px;
            font-weight: bold;
        }
        .usn {
            font-family: 'Times New Roman', serif;
            font-size: 0.8em; /* Slightly smaller than the name */
            color: #000000; /* Darker blue for USN */
            margin-top: 0;
            font-weight: bold; /* Remove bold styling */
        }
        .footer {
            position: absolute;
            bottom: 40px;
            width: 90%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .signature {
            font-family: 'Roboto Slab', serif;
            padding: 5px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            position: relative;
        }

        .signature img {
            max-height: 70px;
            position: relative;
            top: -55px; /* Adjust value to move the image up */
            left: 28px; /* Adjust value to move the image right */
        }

        .signature p { 
            font-family: 'Playfair Display',serif; /* Bold sans-serif font for name */ 
            color: #000000; /* Adjust text color */ 
            font-size: 23px; /* Size for the name */ 
            font-weight: bold; /* Bold for the name */ 
            margin-top: -40px; /* Adjust margin to move the text vertically */ 
            margin-left: 50px;
            text-align: center;
        }

        .signature .position {
            font-family: 'Playfair Display',serif; /* Serif font for position */ 
            font-size: 19px; /* Size for the position */ 
            color: #333; /* Adjust position color */ 
            margin-top: -35px; /* Adjust margin to move the text vertically */
            margin-left: 40px; 
            text-align:center;
        }
        .footer {
            /* Optional: You can style other footer content here */
        }

        .address-footer {
            position: absolute;
            bottom: 8px; /* 20px from the bottom of the page */
            left: 50%;
            transform: translateX(-50%); /* This centers it horizontally */
            text-align: center;
            font-family: 'Times New Roman', serif;
            font-size: 14px;
            color: #000;
            white-space: nowrap
        }

        .address-footer p {
            margin: 1px 0;
            overflow: hidden;
            text-overflow: ellipsis; /* In case the text is too long */
            white-space: nowrap; 
        }

        .contact {
            font-weight: bold;
            font-size: 16px;
            padding-top: 10px;
        }

    </style>
<head>
<body>
    <div class="border-container">
        <div class="certificate">
            <div class="header" style="display: flex; justify-content: center; flex-direction: column; align-items: center; position: relative; top: -15px;text-align: center;">
                <img src="{{ org_logo_base64 }}" alt="Organization Logo" style="max-width: 200px;">
                <p style="color: #00008B; font-weight: bold; margin-top: -16px; letter-spacing: 1px; font-size: 0.9em;">www.mtdn.co.in</p>
            </div>
            <h1 style="color: #000000; font-family: 'Futura', sans-serif; font-size: 50px; font-weight: bold; margin-top: 0; margin-bottom: 0; text-align: center; letter-spacing: 10px;">CERTIFICATE</h1>
            <h2 style="color: #000000; font-family: 'Helvetica', sans-serif; font-size: 16x; font-weight: normal; margin-top: 1px; text-align: center; letter-spacing: 2px;">of Internship to</h2>
            <p class="details">{{ name }} <span class="usn">({{ usn }})</span></p>
            <p>&nbsp;</p>
            <p style="font-family: 'Roboto Slab', serif; font-weight: bold; font-size: 1.1em; color: #000000;">
                has successfully completed the training and workshop of 10 days held in December 2024
            </p>
            <p style="font-family: 'Roboto Slab', serif; font-weight: bold; font-size: 1.1em; color: #000000;">
                covering key concepts and practical skills in Python programming With Database integration.
            </p>
            <p style="font-family: 'Roboto Slab', serif; font-weight: bold; font-size: 1.1em; color: #000000;">
                Participants gained valuable skills in building data-driven applications using Python.
            </p>
            <div class="footer">
                <div class="signature">
                    <img src="{{ signature_image_base64 }}" alt="Signature">
                    <p>Nithin N</p> <!-- Name below the signature -->
                    <p class="position">Managing Director, MTD, Mysuru</p> 
                </div>
            </div>
            <div class="address-footer">
                <p><b>#185/1, Vithala Nilaya, Srirampura, 2nd Cross, Pampapati Road Near New Ashokapuram Railway Station, Mysuru 570023</b></p>
                <p class="contact">Contact: 9480273090</p>
            </div>
        </div>
    </div>
</body>
"""

# Function to process HTML files from a directory and generate PDFs
def generate_certificates_from_html(input_html_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    
    # Encode images to Base64
    background_image_base64 = encode_image_to_base64("bg.png")
    org_logo_base64 = encode_image_to_base64("mtd.png")
    signature_image_base64 = encode_image_to_base64("my_sign.png")
    
    # Loop through all files in the HTML directory
    for filename in os.listdir(input_html_directory):
        if filename.endswith(".html"):
            input_html_path = os.path.join(input_html_directory, filename)

            # Extract name and usn from the filename (or adapt this part based on how data is represented)
            name = filename.split('_')[0]  # Example: Extracting name from filename
            usn = filename.split('_')[1].split('.')[0]  # Example: Extracting USN from filename
            
            # Render HTML from template
            template = Template(html_template)
            rendered_html = template.render(
                name=name,
                usn=usn,
                background_image_base64=background_image_base64,
                org_logo_base64=org_logo_base64,
                signature_image_base64=signature_image_base64
            )
            
            # Output PDF path
            pdf_file_path = os.path.join(output_directory, f"{name}_{usn}.pdf")
            
            # Generate PDF from HTML
            HTML(string=rendered_html, base_url=os.getcwd()).write_pdf(pdf_file_path)
            print(f"Generated: {pdf_file_path}")

# Main function
if __name__ == "__main__":
    input_html_directory = "D:/final/html_certificates" # Path to the directory with HTML files
    output_directory = "pdf_certificates"  # Output directory for PDFs

    # Generate certificates from HTML files
    generate_certificates_from_html(input_html_directory, output_directory)
