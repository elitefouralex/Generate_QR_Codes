import qrcode
import os

# Prompt the user to enter a URL
url = input("Enter the URL to generate a QR code: ")

# Define the path to save the QR code
save_directory = os.path.expanduser('~/Pictures/QR_Codes')

# Define the file path for the output QR code
output_file = os.path.join(save_directory, 'qrcode_output.png')

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Width of the border (4 is the default)
)

# Add the URL data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
qr_image = qr.make_image(fill='black', back_color='white')

# Save the QR code image in the ~/Pictures/QR_Codes directory
qr_image.save(output_file)

print(f"QR code generated and saved to {output_file}")
