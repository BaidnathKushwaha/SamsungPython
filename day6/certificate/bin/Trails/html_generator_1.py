import pandas as pd
from jinja2 import Template
import os
import base64

# Function to encode images to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

# Function to read CSV file
def read_csv(file_path):
    return pd.read_csv(file_path)

# Updated A4-sized HTML template
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
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-family: 'Helvetica', sans-serif;
            background-color: #f5f5f5;
            overflow: auto; /* Allow scrolling */
        }
        .page-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            min-height: 100%; /* Adjust for scrolling */
            background-color: #ffffff;
            padding: 20px;
            box-sizing: border-box;
        }
        .border-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            background-color: #ffffff;
            border: 20px solid #ffffff;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        .certificate {
            width: 100%;
            max-width: 1400px;
            height: auto;
            padding: 50px;
            background-color: white;
            border: 2px solid black;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-image: url('{{ background_image_base64 }}');
            background-size: cover;
            background-position: center;
        }
        h1 {
            font-family: 'Futura', sans-serif;
            font-size: 48px;
            font-weight: bold;
            letter-spacing: 2px;
            text-align: center;
        }
        h2 {
            font-family: 'Merriweather', serif;
            font-size: 28px;
            text-align: center;
            margin-bottom: 30px;
        }
        .details {
            font-family: 'Times New Roman', serif;
            font-size: 2rem;
            font-weight: bold;
            text-align: center;
        }
        .usn {
            font-size: 1.8rem;
            font-weight: bold;
        }
        p {
            font-size: 1.1rem;
            line-height: 1.5;
            text-align: center;
        }
        .signature {
            font-family: 'Roboto Slab', serif;
            text-align: center;
            margin-top: 50px; /* Slightly move the whole signature block down if needed */
            position: relative;
        }
        .signature img {
            position: relative;
            top: -5px; /* Move the image up */
            max-height: 75px;
            margin-top: 5px;
        }
        .fw-bold {
            font-family: 'Playfair Display', serif; /* Change the font for "Nithin N" */
            font-size: 22px;
            margin-top: 20px; /* Adjust the spacing above the name */
            margin-bottom: 8px; /* Add some space below the name */
        }
        .signature .position {
            font-family: 'Playfair Display',serif;;
            font-size: 18px;
            color: #333;
            text-align: center; /* Ensure text is centered */
            margin-top: -12px; /* Adjust the spacing to position the text below "Nithin N" */ /* Change font style for "Managing Director" */
        }
        .address-footer {
            font-family: 'Times New Roman', serif;
            font-size: 14px;
            text-align: center;
            position: relative; /* Add this line */
            top: 65px; /* Adjust this value to move the address section down */
        }
        .contact {
            font-weight: bold;
            font-size: 16px;
            position: relative;
            top: -8px
            
        }
    </style>
</head>
<body>
    <div class="page-container">
        <div class="border-container">
            <div class="certificate">
                <div class="text-center mb-4">
                    <img src="{{ org_logo_base64 }}" alt="Organization Logo" class="img-fluid mb-2">
                    <p style="font-family: 'Helvetica', sans-serif; color: #00008B; font-size: 14px; font-weight: bold;margin-top: -30px;">www.mtdn.co.in</p>
                </div>
                <p>&nbsp;</p>
                <h1>CERTIFICATE</h1>
                <h2>of Internship to</h2>
                <p class="details">{{ name }} <span class="usn">({{ usn }})</span></p>
                <p>&nbsp;</p>
                <p style="font-family: 'Roboto Slab', serif; font-weight: bold; font-size: 1.2em; color: #000000;">
                    has successfully completed the training and workshop of 10 days held in December 2024
                </p>
                <p style="font-family: 'Roboto Slab', serif; font-weight: bold; font-size: 1.2em; color: #000000;">
                    covering key concepts and practical skills in Python programming With Database integration.
                </p>
                <p style="font-family: 'Roboto Slab', serif; font-weight: bold; font-size: 1.2em; color: #000000;">
                    Participants gained valuable skills in building data-driven applications using Python.
                </p>
                <div class="text-center mt-5">
                    <div class="signature">
                        <img src="{{ signature_image_base64 }}" alt="Signature" class="img-fluid">
                        <p class="fw-bold">Nithin N</p>
                        <p class="position">Managing Director, MTD, Mysuru</p>
                    </div>
                </div>
                <div class="address-footer">
                    <p><strong>#185/1, Vithala Nilaya, Srirampura, 2nd Cross, Pampapati Road, Near New Ashokapuram Railway Station, Mysuru 570023</strong></p>
                    <p class="contact">Contact: 9480273090</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>


"""

# Function to generate certificates
def generate_certificate(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # Encode images to Base64
    background_image_base64 = encode_image_to_base64("bg.png")
    org_logo_base64 = encode_image_to_base64("mtd.png")
    signature_image_base64 = encode_image_to_base64("my_sign.png")
    
    for index, row in data.iterrows():
        name = row['name']
        usn = row['usn']
        
        # Render HTML
        template = Template(html_template)
        rendered_html = template.render(
            name=name,
            usn=usn,
            background_image_base64=background_image_base64,
            org_logo_base64=org_logo_base64,
            signature_image_base64=signature_image_base64
        )
        
        # Save as HTML file
        html_file_path = os.path.join(output_dir, f"{name}_{usn}.html")
        with open(html_file_path, "w", encoding="utf-8") as file:
            file.write(rendered_html)
        print(f"Generated: {html_file_path}")

# Main function
if __name__ == "__main__":
    input_csv = "data.csv"  # Path to CSV file
    output_directory = "certificates"  # Output directory
    
    # Read data and generate certificates
    data = read_csv(input_csv)
    generate_certificate(data, output_directory)