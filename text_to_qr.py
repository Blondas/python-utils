import pyqrcode
import png
import sys


def text_to_qr(input_file, output_file):
    # Read the content of the text file
    with open(input_file, 'r') as file:
        text = file.read()

    # Generate QR code
    qr = pyqrcode.create(text)

    # Save the image
    qr.png(output_file, scale=8)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_text_file> <output_qr_code.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    text_to_qr(input_file, output_file)
    print(f"QR code generated and saved as {output_file}")